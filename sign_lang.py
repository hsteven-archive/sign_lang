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
        
    def letter_D(self):
        thumb_tip = self.xyz[4]
        middle_dip = self.xyz[11]
        thumb_dip = self.xyz[3]
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        if distance(middle_dip,thumb_dip) < self.accuracy and palm(middle_tip) and palm(ring_tip):
            return True
        else
        return False
    
    def letter_C(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_tip = self.xyz[8]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        pinky_dip = self.xyz[19]
        thumb_dip = self.xyz[3]
        ring_dip = self.xyz[15]
        index_finger_dip = self.xyz[7]
        middle_dip = self.xyz[10]
        if distance(middle_tip,middle_dip) < self.accuracy and distance(index_finger_tip,index_finger_dip) < self.accuracy:
            if distance(thumb_tip, thumb_dip) < self.accuracy and distance(ring_tip, ring_dip) < self.accuracy:
                if distance(pinky_tip, pinky_pip) < self.accuracy:
                    return True
        else:
            return False

        
    def letter_A(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_pip = self.xyz[6]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        index_finger_mcp = self.xyz[5]
        thumb_ip = self.xyz[3]
        if palm(pinky_tip) and palm(ring_tip) and palm(middle_tip) and distance(index_finger_pip, index_finger_mcp) < self.accuracy:
            if distance(index_finger_mcp, thumb_ip) < self.accuracy:
                return true
        else:
            return false
        
        
    def letter_I(self):
         middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_pip = self.xyz[6]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        index_finger_mcp = self.xyz[5]
        thumb_ip = self.xyz[3]
        if and palm(ring_tip) and palm(middle_tip) and distance(index_finger_pip, index_finger_mcp) < self.accuracy:
            if  distance(index_finger_mcp, thumb_ip) < self.accuracy:
                return True
        else
            return False
        
    def letter_Y(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_pip = self.xyz[6]
        index_finger_mcp = self.xyz[5]
        if palm(middle_tip) and palm(ring_tip) and distance(index_finger_pip, index_finger_mcp) < self.accuracy:
            return True
        else
        return False
    
     #palm matrix touchscreen thing
    def palm(self,pt):
        # form a triangle from the key points indexed by 0, 5, 17
        self.triangle = np.array([self.xyz[0], self.xyz[5], self.xyz[17]])
        assert len(self.triangle) == 3
        vecs = self.triangle - pt
        cosines = np.zeros((3, )
        cosines[0] = np.sum(vecs[0] * vecs[1]) / (np.linalg.norm(vecs[0]) * np.linalg.norm(vecs[1])) 
        cosines[1] = np.sum(vecs[0] * vecs[2]) / (np.linalg.norm(vecs[0]) * np.linalg.norm(vecs[2]))
        cosines[2] = np.sum(vecs[1] * vecs[2]) / (np.linalg.norm(vecs[1]) * np.linalg.norm(vecs[2]))
        count = np.sum(cosines < 0)
        if count >= 2:
            return true
        else:
          return false
        
def distance(x, y):
    return np.linalg.norm(x - y)

if __name__ == "__main__":
    pass
