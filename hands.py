from sign_lang import Sign 
from utils import get_xyz
import PySimpleGUI as sg
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
sign = Sign()

hands = mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

def detect_hands(image, hands=hands):
    
    text = ''
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # ---------- XYZ location of the 21 hand landmarks
            xyz = get_xyz(hand_landmarks.landmark)
            # ---------- Output from the sign language detector
            text = sign.detect(xyz)

            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return image, text
