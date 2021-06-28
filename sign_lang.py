# ======================
# Sign language detection
# ======================

# @author: Qi He
# @date: 2021-05-14

# -*- coding:utf8 -*-

import numpy as np

class Sign():
    def __init__(self, accuracy = 0.15):
        self.accuracy = accuracy
        self.text = ''

    def detect(self, xyz):
                if self.letter_E():
            self.text = 'e'
        elif self.letter_Y():
            self.text = 'y'
        elif self.letter_Q():
            self.text = 'q'
        elif self.letter_G():
            self.text = 'g'
        elif self.letter_I():
            self.text = 'i'
        elif self.letter_N():
            self.text = 'n'
        elif self.letter_M():
            self.text = 'm'
        elif self.letter_K():
            self.text = 'k'
        elif self.letter_F():
            self.text = 'f'
        elif self.letter_D():
            self.text = 'd'
        elif self.letter_H():
            self.text = 'h'
        elif self.letter_U():
            self.text = 'u'
        elif self.letter_R():
            self.text = 'r'
        elif self.letter_V():
            self.text = 'v'
        elif self.letter_W():
            self.text = 'w'
        elif self.letter_A():
            self.text = 'a'
        elif self.letter_L():
            self.text = 'l'
        elif self.letter_B():
            self.text = 'b'
        elif self.letter_C():
            self.text = 'c'
        elif self.letter_P():
            self.text = 'p'
        elif self.letter_X():
            self.text = 'x'
        
        else:
            self.text = ''

        return self.text

        
    def letter_F(self):
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
        pinky_dip = self.xyz[19]
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        if distance(pinky_pip, pinky_mcp) < self.accuracy:
            if distance(pinky_dip, thumb_tip) < self.accuracy and not self.palm(middle_tip) and distance(middle_tip, ring_tip) > self.accuracy and not distance(pinky_dip, ring_tip) < self.accuracy:
                return True
        return False
        
    
    def letter_V(self):
        pinky_pip = self.xyz[18]
        pinky_mcp = self.xyz[17]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[16]
        ring_dip = self.xyz[15]
        ring_pip = self.xyz[14]
        ring_mcp = self.xyz[13]
        pinky_dip = self.xyz[19]
        middle_tip = self.xyz[12]
        middle_pip = self.xyz[10]
        index_pip = self.xyz[6]
        middle_tip = self.xyz[12]
        index_finger_tip = self.xyz[8]
        if distance(pinky_pip, pinky_mcp) < self.accuracy and distance(ring_pip, ring_mcp) < self.accuracy and distance(thumb_tip , pinky_dip) < self.accuracy and distance(thumb_tip, ring_dip) < self.accuracy and not self.palm(middle_tip) and distance(middle_tip, index_finger_tip) > self.accuracy:
            return True
        else:
            return False

        
    def letter_L(self):
        pinky_pip = self.xyz[18]
        pinky_mcp = self.xyz[17] 
        ring_tip = self.xyz[16]
        middle_pip = self.xyz[10]
        middle_mcp = self.xyz[9]
        if distance(pinky_pip, pinky_mcp) < self.accuracy and self.palm(ring_tip) and distance(middle_pip , middle_mcp) < self.accuracy:
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
        index_finger_pip = self.xyz[6]
        index_finger_mcp = self.xyz[5]
        if distance(middle_dip,thumb_tip) < self.accuracy and self.palm(middle_tip) and self.palm(ring_tip):
            return True
        else:
            return False
    
    def letter_C(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_tip = self.xyz[8]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        pinky_dip = self.xyz[19]
        pinky_pip = self.xyz[18]
        thumb_dip = self.xyz[3]
        ring_dip = self.xyz[15]
        index_finger_dip = self.xyz[7]
        middle_dip = self.xyz[10]
        if distance(middle_tip,middle_dip) < self.accuracy and distance(index_finger_tip,index_finger_dip) < self.accuracy:
            if distance(thumb_tip, thumb_dip) < self.accuracy and distance(ring_tip, ring_dip) < self.accuracy:
                if distance(pinky_tip, pinky_pip) < self.accuracy:
                    return True
        return False

        
    def letter_A(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_pip = self.xyz[6]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        index_finger_mcp = self.xyz[5]
        thumb_ip = self.xyz[3]
        if self.palm(pinky_tip) and self.palm(ring_tip) and self.palm(middle_tip) and distance(index_finger_pip, index_finger_mcp) < self.accuracy:
            if distance(index_finger_pip, thumb_ip) < self.accuracy:
                return True
        return False
        
        
    def letter_I(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_pip = self.xyz[6]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        index_finger_mcp = self.xyz[5]
        index_finger_dip = self.xyz[7]
        thumb_ip = self.xyz[3]
        pinky_pip = self.xyz[18]
        pinky_mcp = self.xyz[17]
        if self.palm(ring_tip) and self.palm(middle_tip) and distance(index_finger_pip, index_finger_mcp) < self.accuracy:
            if  distance(index_finger_dip, thumb_ip) < self.accuracy:
                return True
        return False
        
    def letter_Y(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_pip = self.xyz[6]
        index_finger_mcp = self.xyz[5]
        index_finger_dip = self.xyz[7]
        thumb_ip = self.xyz[3]
        if self.palm(middle_tip) and self.palm(ring_tip) and distance(index_finger_pip, index_finger_mcp) < self.accuracy and not distance(index_finger_dip, thumb_ip) < self.accuracy:
            return True
        return False
    
    def letter_K(self):
        ring_tip = self.xyz[16]
        pinky_tip = self.xyz[20]
        ring_dip = self.xyz[15]
        thumb_tip = self.xyz[4]
        index_pip = self.xyz[6]
        middle_pip = self.xyz[10]
        if self.palm(ring_tip) and distance(pinky_tip, ring_dip) < self.accuracy and distance(thumb_tip, index_pip) < self.accuracy:
            if distance(thumb_tip, middle_pip) < self.accuracy:
                return True
        return False
    
    def letter_N(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_tip = self.xyz[8]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        pinky_dip = self.xyz[19]
        thumb_ip = self.xyz[3]
        ring_dip = self.xyz[15]
        index_finger_dip = self.xyz[7]
        middle_dip = self.xyz[10]
        ring_pip = self.xyz[14]
        if distance(middle_dip, pinky_dip) < self.accuracy and distance(thumb_tip, ring_pip) < self.accuracy and distance(thumb_ip, index_tip) < self.accuracy:
            if distance(thumb_ip, middle_tip) < self.accuracy and palm(ring_tip):
                return True
        return False
    
    def letter_U(self):
        middle_pip = self.xyz[10]
        index_pip = self.xyz[6]
        ring_tip = self.xyz[16]
        pinky_tip = self.xyz[20]
        ring_dip = self.xyz[15]
        thumb_tip = self.xyz[4]
        middle_tip = self.xyz[12]
        index_finger_tip = self.xyz[8]
        if distance(middle_pip, index_pip) < self.accuracy and distance(pinky_tip, ring_dip) < self.accuracy and distance(ring_dip,thumb_tip) < self.accuracy and not distance(middle_tip, index_finger_tip) > self.accuracy:
            if self.palm(ring_tip):
                return True
        return False
        
    def letter_E(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_tip = self.xyz[8]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        thumb_ip = self.xyz[3]
        thumb_mcp = self.xyz[2]
        if distance(middle_tip, thumb_ip) < self.accuracy and distance(index_finger_tip, thumb_mcp) < self.accuracy:
            if distance(ring_tip, thumb_tip) < self.accuracy and distance(pinky_tip, thumb_tip) < self.accuracy:
                return True
        return False
    
    def letter_M(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_tip = self.xyz[8]
        thumb_ip = self.xyz[3]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        pinky_dip = self.xyz[19]
        if distance(thumb_tip, pinky_dip) < self.accuracy and distance(thumb_ip, middle_tip) < self.accuracy and distance(thumb_ip, index_tip) < self.accuracy:
            if distance(thumb_tip, ring_tip) < self.accuracy:
                return True
        return False
    
    def letter_S(self):
        ring_tip = self.xyz[16]
        middle_tip = self.xyz[12]
        ring_pip = self.xyz[14]
        thumb_tip = self.xyz[4]
        thumb_mcp = self.xyz[2]
        index_dip = self.xyz[7]
        if distance(ring_pip, thumb_tip) < self.accuracy and distance(thumb_mcp, index_dip) and palm(ring_tip) and self.palm(middle_tip):
            return True
        return False
        
    def letter_T(self):
        index_tip = self.xyz[8]
        thumb_ip = self.xyz[3]
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        pinky_tip = self.xyz[20]
        if distance(index_tip, thumb_ip) < self.accuracy:
            if distance(pinky_tip, ring_tip) < self.accuracy:
                if distance(ring_tip, middle_tip) < self.accuracy:
                    return True
        return False
    
    def letter_P(self):
        wrist = self.xyz[0]
        index_mcp = self.xyz[5]
        pinky_mcp = self.xyz[17]
        ring_tip = self.xyz[16]
        pinky_tip = self.xyz[20]
        ring_dip = self.xyz[15]
        thumb_tip = self.xyz[4]
        index_pip = self.xyz[6]
        middle_pip = self.xyz[10]
        if self.palm_direction(wrist, index_mcp, pinky_mcp)[1] == "down":
            if distance(pinky_tip, ring_dip) < self.accuracy and distance(thumb_tip, index_pip) < self.accuracy:
                if distance(thumb_tip, middle_pip) < self.accuracy:
                    return True
        return False
    
    def letter_O(self):
        middle_tip = self.xyz[12]
        ring_tip = self.xyz[16]
        index_finger_tip = self.xyz[8]
        thumb_tip = self.xyz[4]
        pinky_tip = self.xyz[20]
        if distance(middle_tip, thumb_tip) < self.accuracy and distance(ring_tip, thumb_tip) < self.accuracy and distance(index_finger_tip, thumb_tip,) < self.accuracy and distance(pinky_tip, thumb_tip) < self.accuracy:
            return True
        else:
            return False
           
    def letter_R(self):
        index_pip = self.xyz[6]
        middle_pip = self.xyz[10]
        ring_tip = self.xyz[16]
        thumb_tip = self.xyz[4]
        pinky_dip = self.xyz[19]
        if self.palm(ring_tip) and distance(index_pip, middle_pip) < self.accuracy and distance(thumb_tip, pinky_dip) < self.accuracy:
            return True
        else:
            return False
        
    def letter_X(self):
        ring_tip = self.xyz[16]
        middle_tip = self.xyz[12]
        ring_pip = self.xyz[14]
        pinky_pip = self.xyz[18]
        thumb_tip = self.xyz[4]
        index_pip = self.xyz[6]
        index_dip = self.xyz[7]
        if self.palm(ring_tip) and self.palm(middle_tip) and distance(pinky_pip, ring_pip) < self.accuracy and distance(thumb_tip, ring_pip) < self.accuracy:
            if distance(index_pip, index_dip) < self.accuracy:
                return True
        else:
            return False
        
        
    def letter_G(self):
        thumb_tip = self.xyz[4]
        index_tip = self.xyz[8]
        wrist = self.xyz[0]
        index_mcp = self.xyz[5]
        pinky_mcp = self.xyz[17]
        if self.palm_direction(wrist, index_mcp, pinky_mcp)[0] == "right":
            if distance(index_tip, thumb_tip) < self.accuracy:
                return True
        return False
    def letter_Q(self):
        thumb_tip = self.xyz[4]
        index_tip = self.xyz[8]
        wrist = self.xyz[0]
        index_mcp = self.xyz[5]
        pinky_mcp = self.xyz[17]
        if self.palm_direction(wrist, index_mcp, pinky_mcp)[1] == "down":
            if distance(index_tip, thumb_tip) < self.accuracy:
                return True
        return False
    
     #palm matrix touchscreen thing
    def palm(self,pt):
        # form a triangle from the key points indexed by 0, 5, 17
        self.triangle = np.array([self.xyz[0], self.xyz[5], self.xyz[17]])
        assert len(self.triangle) == 3
        vecs = self.triangle - pt
        cosines = np.zeros((3))
        cosines[0] = np.sum(vecs[0] * vecs[1]) / (np.linalg.norm(vecs[0]) * np.linalg.norm(vecs[1])) 
        cosines[1] = np.sum(vecs[0] * vecs[2]) / (np.linalg.norm(vecs[0]) * np.linalg.norm(vecs[2]))
        cosines[2] = np.sum(vecs[1] * vecs[2]) / (np.linalg.norm(vecs[1]) * np.linalg.norm(vecs[2]))
        count = np.sum(cosines < 0)
        if count >= 2:
            return True
        else:
            return False
            
    def palm_direction(self,palm1, palm2, palm3):
        palm_average = (palm2 + palm3)/2
        verticalDirection = ""
        horizontalDirection = ""
        if palm_average[1] < palm1[1]:
            verticalDirection = "up"
        elif palm_average[1] > palm1[1]:
            verticalDirection = "down"
        if palm_average[0] < palm1[0]:
            horizontalDirection = "left"
        elif palm_average[0] > palm1[0]:
            horizontalDirection = "right"
        return horizontalDirection, verticalDirection
        
                           
def distance(x, y):
    return np.linalg.norm(x - y)

if __name__ == "__main__":
    pass
