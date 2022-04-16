from sign_lang import Sign
from utils import get_xyz
import PySimpleGUI as sg
import cv2
import mediapipe as mp
import numpy as np

class hands:
    
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        #mp_hands
        
        self.sign = Sign(np.zeros((21, 3)))
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.85,
            min_tracking_confidence=0.85)

        self.landmark_drawing_spec = self.mp_drawing.DrawingSpec(color=(0,0,255), thickness=10, circle_radius=5) #BGR
        self.connection_drawing_spec = self.mp_drawing.DrawingSpec(color=(0,255,0), thickness=3, circle_radius=10)
        self.xyz_history = np.array([]).reshape((-1,21,3))
    def record_history(self):
        self.xyz_history = np.vstack((self.xyz_history, self.sign.xyz[None,:]))
    def detect_hands(self, image):
    
        text = ''
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = self.hands.process(image)

    # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

            # ---------- XYZ location of the 21 hand landmarks
                xyz = get_xyz(hand_landmarks.landmark)
                self.sign = Sign(xyz)
            # ---------- Output from the sign language detector
                text = self.sign.detect()
                self.mp_drawing.draw_landmarks(
                image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS, self.landmark_drawing_spec, self.connection_drawing_spec)
                self.record_history()
                
        return image, text

    def distance(self,x, y):
        return np.linalg.norm(x - y)
    def reset_sign(self):
        self.sign.reset()
