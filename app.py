from hands import detect_hands
import PySimpleGUI as sg
import cv2
import numpy as np

def main():

    sg.theme('DarkBlue1')

    # define the window layout
    layout = [[sg.Text('Sign Language Translator', size=(60, 1), justification='center', font='Helvetica 15')],
              [sg.Image(filename='', key='image')],
              [sg.Text('', size=(60, 5), key='output', font='Helvetica 15')],
              [sg.Button('Begin', size=(15, 1), font='Helvetica 15'),
               sg.Button('Stop', size=(15, 1), font='Helvetica 15'),
               sg.Button('Exit', size=(15, 1), font='Helvetica 15'), ]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration',
                       layout, location=(800, 400))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    recording = False

    message = ''

    while True:
        event, values = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == 'Begin':
            recording = True

        elif event == 'Stop':
            recording = False
            img = np.full((480, 640), 255)
            # this is faster, shorter and needs less includes
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['image'].update(data=imgbytes)

        if recording:
            ret, frame = cap.read()
            frame, text = detect_hands(frame)
            message = message + text
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
            window['image'].update(data=imgbytes)
            window['output'].update(message)


main()