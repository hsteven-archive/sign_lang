# ======================
# utilization function
# ======================

# @author: Qi He
# @date: 2021-05-14

# -*- coding:utf8 -*-

import numpy as np

def get_xyz(landmarks):
    xyz = np.zeros((21, 3))
    for i,l in enumerate(landmarks):
        xyz[i,0] = l.x
        xyz[i,1] = l.y
        xyz[i,2] = l.z
    return xyz

if __name__ == "__main__":
    pass