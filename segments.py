from sign_lang import Sign
from utils import get_xyz
import PySimpleGUI as sg
import cv2
import mediapipe as mp
import numpy as np

class segment:
    
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_selfie_segmentation = mp.solutions.selfie_segmentation
        #mp_hands
        
        self.sign = Sign(np.zeros((21, 3)))
        self.selfie_segmentation = self.mp_selfie_segmentation.SelfieSegmentation(
                    model_selection=1)

        # self.landmark_drawing_spec = self.mp_drawing.DrawingSpec(color=(0,0,255), thickness=10, circle_radius=5) #BGR
        # self.connection_drawing_spec = self.mp_drawing.DrawingSpec(color=(0,255,0), thickness=3, circle_radius=10)

    def seg(self, image):
        BG_COLOR = (192, 192, 192) # gray

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = self.selfie_segmentation.process(image)

    # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        condition = np.stack(
            (results.segmentation_mask,) * 3, axis=-1) > 0.1
        bg_image = np.zeros(image.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        output_image = np.where(condition, image, bg_image)
        output_image = cv2.flip(output_image, 1)
        return output_image

    def reset_sign(self):
        self.sign.reset()
