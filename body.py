from sign_lang import Sign
from utils import get_xyz
import PySimpleGUI as sg
import cv2
import mediapipe as mp
import numpy as np

class body:
    
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic
        
        self.sign = Sign(np.zeros((21, 3)))
        self.holistic = self.mp_holistic.Holistic(
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)

        self.landmark_drawing_spec = self.mp_drawing.DrawingSpec(color=(0,0,255), thickness=10, circle_radius=5) #BGR
        self.connection_drawing_spec = self.mp_drawing.DrawingSpec(color=(255,0,0), thickness=3, circle_radius=10)

    def detect_body(self, image):
    
        text = ''
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = self.holistic.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # self.mp_drawing.draw_landmarks(
        #     image, results.face_landmarks, self.mp_holistic.FACE_CONNECTIONS, self.landmark_drawing_spec, self.connection_drawing_spec)
        # self.mp_drawing.draw_landmarks(
        #     image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
        # self.mp_drawing.draw_landmarks(
        #     image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
        self.mp_drawing.draw_landmarks(
            image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS, self.landmark_drawing_spec, self.connection_drawing_spec)
        image = cv2.flip(image, 1)
        return image, text

    def reset_sign(self):
        self.sign.reset()
