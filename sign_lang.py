# ======================
# Sign language detection
# ======================

# @author: Qi He
# @date: 2021-05-14

# -*- coding:utf8 -*-

import numpy as np

class Sign():
    def __init__(self, accuracy = 0.1):
        self.accuracy = accuracy
        self.text = ''

    def detect(self, xyz):
        self.xyz = xyz
        if self.letter_O():
            self.text = 'o'
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
    
    def letter_W(self):
        pinky_pip = self.xyz[18]
        pinky_mcp = self.xyz[17]
        thumb_tip = self.xyz[4]
        if distance(pinky_pip, pinky_mcp) < self.accuracy:
            if distance(pinky_mcp, thumb_tip) < self.accuracy:
                return True
        else
            return False
        
    
    def letter_V(self):
        pinky_pip = self.xyz[18]
        pinky_mcp = self.xyz[17]
        thumb_tip = self.xyz[4]
        ring_dip = self.xyz[15]
        ring_pip = self.xyz[14]
        ring_mcp = self.xyz[13]
        if distance(pink_pip, pinky_mcp) < self.accuracy and distance(ring_pip, ring_mcp) < self.accuracy and distance(thumb_tip , ring_dip) < self.accuracy:
            return true
        else:
            return false
    
def distance(x, y):
    return np.linalg.norm(x - y)

if __name__ == "__main__":
    pass
