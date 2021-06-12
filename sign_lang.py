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
        elif self.letter_W():
            self.text = 'w'
        elif self.letter_V():
            self.text = 'v'
        elif self.letter_L():
            self.text = 'l'
        elif self.letter_B():
            self.text = 'b'
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
        else:
            return False
        
    
    def letter_V(self):
        pinky_pip = self.xyz[18]
        pinky_mcp = self.xyz[17]
        thumb_tip = self.xyz[4]
        ring_dip = self.xyz[15]
        ring_pip = self.xyz[14]
        ring_mcp = self.xyz[13]
        if distance(pinky_pip, pinky_mcp) < self.accuracy and distance(ring_pip, ring_mcp) < self.accuracy and distance(thumb_tip , ring_dip) < self.accuracy:
            return True
        else:
            return False

        
    def letter_L(self):
        pinky_pip = self.xyz[18]
        pinky_mcp = self.xyz[17] 
        ring_pip = self.xyz[14]
        ring_mcp = self.xyz[13]
        middle_pip = self.xyz[10]
        middle_mcp = self.xyz[9]
        if distance(pinky_pip, pinky_mcp) < self.accuracy and distance(ring_pip, ring_mcp) < self.accuracy and distance(middle_pip , middle_mcp) < self.accuracy:
            return True
        else:
            return False
        
    def letter_B(self):
        pinky_mcp = self.xyz[13]
        pinky_dip = self.xyz[19]
        ring_pip = self.xyz[14]
        thumb_tip = self.xyz[4]
        index_pip = self.xyz[6]
        middle_pip = self.xyz[10]
        if distance(pinky_mcp, thumb_tip) < self.accuracy and distance(ring_pip, pinky_dip) < self.accuracy and distance(middle_pip , index_pip) < self.accuracy:
            return True
        else:
            return False
        
def distance(x, y):
    return np.linalg.norm(x - y)

if __name__ == "__main__":
    pass
