# ======================
# Sign language detection
# ======================

# @author: Qi He
# @date: 2021-05-14

# -*- coding:utf8 -*-

import numpy as np

class Sign():
    def __init__(self, accuracy = 0.05):
        self.accuracy = accuracy
        self.text = ''

    def detect(self, xyz):
        self.xyz = xyz
        if self.letter_O():
            self.text = '0'
        else:
            self.text = ''

        return self.text
        
    def letter_O(self):
        thumb_tip = self.xyz[4]
        index_finger_tip = self.xyz[8]
        if distance(thumb_tip, index_finger_tip) < self.accuracy:
            return True
        else:
            return False

def distance(x, y):
    return np.linalg.norm(x - y)

if __name__ == "__main__":
    pass