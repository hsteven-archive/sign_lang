# ======================
# APP main entrance
# ======================

# @author: Qi He
# @date: 2021-06-05

# -*- coding:utf8 -*-

from hands import detect_hands
import PySimpleGUI as sg
import cv2
import numpy as np

def main():

    cap = cv2.VideoCapture(0)
    width, height = get_frame_resolutions(cap)
    
    sg.theme('DarkBlue1')

    # define the window layout
    layout = [[sg.Text('Sign Language Translator', size=(80, 1), justification='center', font='Helvetica 15')],
              [sg.Image(filename='', key='image')],
              [sg.Text('', size=(80, 10), key='output', font='Helvetica 15')],
              [sg.Button('Begin', size=(25, 1), font='Helvetica 15'),
               sg.Button('Stop', size=(25, 1), font='Helvetica 15'),
               sg.Button('Exit', size=(25, 1), font='Helvetica 15'), ]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration',
                       layout, location=(100, 100))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    recording = False

    message = ''

    while True:
        event, _ = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == 'Begin':
            recording = True

        elif event == 'Stop':
            recording = False
            img = np.full((height, width), 255)
            # this is faster, shorter and needs less includes
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['image'].update(data=imgbytes)

        if recording:
            _, frame = cap.read()
            frame, text = detect_hands(frame)
            message = message + text
            imgbytes = cv2.imencode('.png', resize(frame, (width, height)))[1].tobytes()  # ditto
            window['image'].update(data=imgbytes)
            window['output'].update(message)

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