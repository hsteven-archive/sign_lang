    # ======================

# Sign language detection

# ======================



# @author: me

# @date: 2022-19-2



# -*- coding:utf8 -*-

from traceback import print_stack

import numpy as np


class Sign():

    def __init__(self, xyz,accuracy=0.3 ):

        self.xyz = xyz

        #self.xyz_history = np.vstack((self.xyz_history, xyz[None,:]))

        self.accuracy=accuracy

        self.text = ''

        self.wrist = self.xyz[0]

        self.thumb_cmc = self.xyz[1]

        self.thumb_mcp = self.xyz[2]

        self.thumb_ip = self.xyz[3]

        self.thumb_tip = self.xyz[4]

        self.index_mcp = self.xyz[5]

        self.index_pip = self.xyz[6]

        self.index_dip = self.xyz[7]

        self.index_tip = self.xyz[8]

        self.middle_mcp = self.xyz[9]

        self.middle_pip = self.xyz[10]

        self.middle_dip = self.xyz[11]

        self.middle_tip = self.xyz[12]

        self.ring_mcp = self.xyz[13]

        self.ring_pip = self.xyz[14]

        self.ring_dip = self.xyz[15]

        self.ring_tip = self.xyz[16]

        self.pinky_mcp = self.xyz[17]

        self.pinky_pip = self.xyz[18]

        self.pinky_dip = self.xyz[19]

        self.pinky_tip = self.xyz[20]

            

    
    def record_history(self):
        self.xyz_history = np.vstack((self.xyz_history, xyz[None,:]))
    def reset(self):
        self.xyz_history = np.array([]).reshape((-1,21,3))



    def detect(self):

        #self.demo_xyz_history()
        if self.letter_Jend():
            self.text = 'j'
        elif self.letter_Zend():
            self.text = 'z'
        elif self.letter_N():
        
            self.text = 'n'
        elif self.letter_M():

            self.text = 'm'
        elif self.letter_E():

            self.text = 'e'

        elif self.letter_P():

            self.text = 'p'

        elif self.letter_X():

            self.text = 'x'

        elif self.letter_I():

            self.text = 'i'

        elif self.letter_Q():

            self.text = 'q'

        elif self.letter_G():

            self.text = 'g'

        elif self.letter_A():

            self.text = 'a'

        elif self.letter_S():

            self.text = 's'

        elif self.letter_T():

            self.text = 't'

        

        elif self.letter_O():

            self.text = 'o'

        

        elif self.letter_D():

            self.text = 'd'

        elif self.letter_Y():

            self.text = 'y'

        elif self.letter_K():

            self.text = 'k'
        elif self.letter_F():

            self.text = 'f'
        elif self.letter_R():

            self.text = 'r'
        elif self.letter_H():

            self.text = 'h'

        

        elif self.letter_U():

            self.text = 'u'

        elif self.letter_V():

            self.text = 'v'

        elif self.letter_W():

            self.text = 'w'

        elif self.letter_L():

            self.text = 'L'

        elif self.letter_B():

            self.text = 'b'

        elif self.letter_C():

            self.text = 'c'

        else:

            self.text = ''


        return self.text

        

        # tips = [self.palm(self.pinky_tip), self.palm(self.ring_tip), self.palm(self.middle_tip), self.palm(self.index_tip)]

        # print(tips)

        return self.text

        
    def letter_F(self):

        if self.touching(self.thumb_tip, self.index_tip,self.accuracy) and self.distance(self.index_tip,self.wrist) > self.distance(self.thumb_tip, self.wrist):
            if not self.palm(self.pinky_tip) and not self.palm(self.ring_tip) and not self.palm(self.middle_tip):
                return True

        else:

            return False

    def letter_H(self):

        if self.palm_direction(self.wrist, self.index_mcp, self.pinky_mcp)[0] == "left":
                if self.touching(self.index_tip, self.middle_tip, self.accuracy) and not self.touching(self.ring_tip,self.middle_tip,self.accuracy) and not self.touching(self.index_tip,self.middle_tip,self.accuracy*0.65):
                    return True

        return False

    def letter_W(self):

        if self.touching(self.pinky_pip, self.pinky_mcp, self.accuracy):

            if self.touching(self.pinky_dip, self.thumb_tip,  self.accuracy) and not self.palm(self.middle_tip) and not self.touching(self.pinky_dip, self.ring_tip, self.accuracy):

                return True

        return False

    

    def letter_L(self):

        if self.palm(self.ring_tip) and self.touching(self.middle_tip,self.ring_tip,self.accuracy) and not self.touching(self.ring_pip, self.thumb_tip,self.accuracy):
            if not self.palm(self.index_tip) and not self.palm(self.thumb_tip):
                return True

        else:

            return False

        

    def letter_B(self):

        if not self.palm(self.pinky_tip) and not self.palm(self.index_tip) and not self.palm(self.ring_tip) and not self.palm(self.middle_tip):
            if self.palm(self.thumb_tip):
                return True

        else:

            return False

        

    def letter_D(self):

        if self.touching(self.middle_tip, self.thumb_tip, self.accuracy) and not self.palm(self.index_tip):

            return True

        else:

            return False

    

    def letter_C(self):

        if not self.palm(self.pinky_tip) and not self.palm(self.index_tip) and not self.palm(self.ring_tip) and not self.palm(self.middle_tip) and not self.touching(self.thumb_tip, self.middle_tip, self.accuracy):
            if self.touching(self.pinky_tip, self.ring_tip, self.accuracy) and self.touching(self.index_tip,self.middle_tip,self.accuracy):
                if not self.palm(self.thumb_tip):
                    if self.palm_direction(self.wrist, self.index_mcp, self.pinky_mcp)[1] == "up":
                        return True

        return False



    def letter_V(self):

        if not self.touching(self.index_tip,self.middle_tip,self.accuracy*1.2):
            if self.touching(self.ring_tip,self.thumb_tip,self.accuracy):
                return True

        else:

            return False

    def letter_Jend(self):
        if self.pinky_tip[0] < self.thumb_tip[0]:
            return True
        return False

    def letter_A(self):

        if self.palm(self.pinky_tip) and self.palm(self.ring_tip) and self.palm(self.middle_tip):

            if self.distance(self.index_pip, self.thumb_tip) < self.accuracy:
                if self.touching(self.index_tip,self.middle_tip,self.accuracy):

                    return True

        return False

        

        

    def letter_I(self):
        if self.touching(self.thumb_tip, self.index_pip, self.accuracy *1.3) and self.palm_direction(self.wrist, self.index_mcp, self.pinky_mcp)[1] == "up":
            if not self.palm(self.pinky_tip):
                if self.palm(self.middle_tip):
                    return True

        return False

        

    def letter_Y(self):

        if not self.touching(self.pinky_tip,self.thumb_tip,self.accuracy*5):
            return True

        return False

    

    def letter_K(self):

        if self.palm(self.ring_tip):
            if self.touching(self.thumb_tip,self.middle_pip,self.accuracy*1.2):
                return True
        return False

    

    def letter_N(self):

        if self.touching(self.index_tip,self.thumb_ip,self.accuracy) and self.touching(self.middle_tip,self.thumb_ip,self.accuracy):
            if self.palm(self.ring_tip):
                return True

        return False

    

    def letter_U(self):

        if self.distance(self.ring_tip, self.thumb_tip) < self.accuracy and self.distance(self.index_tip, self.middle_tip) < self.accuracy and self.distance(self.pinky_tip, self.ring_tip) < self.accuracy:
            if self.palm_direction(self.wrist, self.middle_pip, self.index_pip)[1] != "down":
                if not self.touching(self.middle_tip, self.ring_tip, self.accuracy):
                    return True

        return False

        

    def letter_E(self):

        if self.touching(self.thumb_tip, self.pinky_tip, self.accuracy) and self.touching(self.thumb_ip, self.middle_tip,self.accuracy):
            return True
        return False

    

    def letter_M(self):

        if self.touching(self.middle_tip,self.thumb_ip,self.accuracy):
            if self.touching(self.index_tip,self.thumb_ip,self.accuracy):
                if self.palm(self.pinky_tip):

                    return True

        return False

    

    def letter_S(self):

        if self.touching(self.ring_pip, self.thumb_tip,self.accuracy) and self.palm(self.middle_tip):

            return True

        return False

        

    def letter_T(self):

        if self.touching(self.index_tip,self.thumb_ip,self.accuracy):
            if not self.touching(self.middle_tip,self.thumb_ip,self.accuracy):
                return True;
        return False

    

    def letter_P(self):
        if self.palm_direction(self.wrist, self.index_mcp, self.pinky_mcp)[1] == "down":

            if self.touching(self.thumb_tip,self.middle_pip,self.accuracy * 1.5) or self.touching(self.thumb_tip,self.middle_dip,self.accuracy * 1.5):
                if self.touching(self.middle_tip,self.index_tip,self.accuracy*2):
                    return True
        return False

    

    def letter_O(self):

        if self.touching(self.index_tip,self.thumb_tip,self.accuracy) and self.touching(self.middle_tip,self.thumb_tip,self.accuracy):

            return True

        else:

            return False

           

    def letter_R(self):
        if self.touching(self.index_tip,self.middle_tip,self.accuracy)  and self.touching(self.ring_tip, self.thumb_tip,self.accuracy):
            if self.index_tip[0]+0.02 >self.middle_tip[0]:
                return True

        else:

            return False

        

    def letter_X(self):

        if self.touching(self.middle_dip,self.thumb_tip,self.accuracy):
                if not self.palm(self.index_tip):
                    if self.palm(self.ring_tip):
                        return True

        else:

            return False

        

    def letter_Zend(self):
        if self.touching(self.middle_tip, self.thumb_tip, self.accuracy) and not self.palm(self.index_tip):
            if self.index_tip[0] > self.middle_pip[0]:
                return True

        else:

            return False

    def letter_G(self):

        if self.touching(self.thumb_tip,self.index_dip,self.accuracy) and self.palm_direction(self.wrist, self.index_mcp, self.pinky_mcp)[0] == "left":
            if not self.palm(self.index_tip):
                return True

        return False

        

    def letter_Q(self):

        if self.palm_direction(self.wrist, self.index_mcp, self.pinky_mcp)[1] == "down":

            if self.touching(self.index_dip, self.thumb_tip ,self.accuracy):

                return True

        return False



    # ------ Sample use xyz_history ------

    def demo_xyz_history(self):

        # Self.xyz_history the time series history of 21 key points within a fixed time frame

        # It is an array of shape (frames_num, 21, 3)

        # frames_num will increase with time goes by, which is also illustrate in GUI with extending dash lines '-'

        # frames_num will be reset when a new time frame begin, and the maximum number is 50

        pinky_tip_history_in_2D = self.xyz_history[:,20,:2]
        print('pinky_tip_history_in_2D shape: ', pinky_tip_history_in_2D.shape)

    

     #palm matrix touchscreen thing
    def touching(self, p1, p2, accuracy):
        if(self.distance(p1, p2) < accuracy):
            return True
        else:
            return False
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

        if palm_average[1] < palm1[1] :

            verticalDirection = "up"

        elif palm_average[1] > palm1[1]:

            verticalDirection = "down"

        if palm_average[0] < palm1[0]-0.1:

            horizontalDirection = "left"

        elif palm_average[0] > palm1[0]:

            horizontalDirection = "right"

        return horizontalDirection, verticalDirection

        
     
                           

    def distance(self,x, y):

        return np.linalg.norm(x - y)/np.linalg.norm(self.wrist-self.middle_mcp)

    

def check_dist():

    sign = Sign()

def _collinear(a,b,c):
        m1 = (b[1]-a[1])/(b[0]-a[0])
        m2 = (c[1]-b[1])/(c[0]-b[0])
        if np.abs(m1 - m2) <=0.05:

            return True

        else:

            return False



if __name__ == "__main__":

    pass