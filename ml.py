import torch
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np

from ml.sign_lang_model import SignLangModel

# define a video capture object
vid = cv2.VideoCapture(0)
gray = None
model = SignLangModel()
model.load_state_dict(torch.load('ml/model_trained.pt'))
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = ToTensor()
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    out = model(gray)
    probs, label = torch.topk(out, 25)
    pred = out.max(1, keepdim=True)[1]
    print(chr(97+pred))
    
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

