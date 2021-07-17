# ======================
# APP main entrance
# ======================

# @author: Qi He
# @date: 2021-06-05

# -*- coding:utf8 -*-
from hands import hands
import PySimpleGUI as sg
import cv2
import numpy as np

step = 50

def main():
    Hands = hands()
    cap = cv2.VideoCapture(0)
    width, height = get_frame_resolutions(cap)
    
    sg.theme('DarkBlue')

    # define the window layout
    layout = [[sg.Text('Sign Language Translator', size=(80, 1), justification='center', font='Arial 15')],
              [sg.Image(filename='', key='image'), sg.Text('', size=(2, 1), key='single_letter', font='Arial 300', justification='center')],
              [sg.Text('', size=(step, 1), key='bar', font='Arial '+str(int(2000/step)))],
              [sg.Text('Text', size=(10, 1), font='Arial 20')],
              [sg.Text('', size=(40, 2), key='output', font='Arial 40')],
              [sg.Button('Begin', size=(40, 1), font='Arial 15'),
               sg.Button('Stop', size=(40, 1), font='Arial 15'),
               sg.Button('Exit', size=(40, 1), font='Arial 15'), ]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration',
                       layout, location=(100, 100))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    recording = True
    bar_time = 0
    Hands.reset_sign()

    message = ''
    all_message = ''

    while True:
        event, _ = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == 'Begin':
            recording = True
            bar_time = 0
            message = ''

        elif event == 'Stop':
            recording = False
            img = np.full((height, width), 255)
            # this is faster, shorter and needs less includes
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['image'].update(data=imgbytes)

        if recording:
            _, frame = cap.read()
            frame, text = Hands.detect_hands(frame)
            message += text
            if bar_time > step:
                if message:
                    message = message[int(len(message)/4.0):] # Remove the transition period
                    all_message += max(message, key=message.count)
                bar_time = 0
                message = ''
                reset_sign()
            else:
                bar_time += 1
            imgbytes = cv2.imencode('.png', resize(frame, (width, height)))[1].tobytes()  # ditto
            window['image'].update(data=imgbytes)
            window['single_letter'].update(text)
            window['output'].update(all_message)
            window['bar'].update('-'*bar_time)

def get_screen_resolutions():
    import tkinter as tk

    root = tk.Tk()
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.destroy()

    return width, height

def get_camera_resolutions(cap):
    _, frame = cap.read()
    width = int(frame.shape[1])
    height = int(frame.shape[0])

    return width, height

def get_frame_resolutions(cap):
    screen_width, screen_height = get_screen_resolutions()
    cam_width, cam_height = get_camera_resolutions(cap)
    resize_ratio = min(screen_height/2.0/cam_height, screen_width/2.0/cam_width)
    width = int(cam_width * resize_ratio)
    height = int(cam_height * resize_ratio)

    return width, height

def resize(img, dim):
    img_resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return img_resized

if __name__ == "__main__":
    main()
