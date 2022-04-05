import torch
import torchvision
import torchvision.transforms as T
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np


class SignLangModel(nn.Module):
  def __init__(self):	
    super(SignLangModel, self).__init__()
    
    self.conv1 = nn.Sequential(
        nn.Conv2d(1,80,kernel_size=5),
        nn.BatchNorm2d(80),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2,stride=2)
    )
    
    self.conv2 = nn.Sequential(     
        nn.Conv2d(80,80,kernel_size=5),
        nn.BatchNorm2d(80),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2,stride=2)
    )

    self.fc1 = nn.Sequential(
        nn.Linear(1280, 250),
        nn.ReLU()
    )

    self.fc2 = nn.Sequential(
        nn.Linear(250, 25),
        nn.LogSoftmax(dim=1)
    )


  def forward(self,x):
    x = self.conv2(self.conv1(x))
    x = x.view(x.size(0), -1)
    x = self.fc2(self.fc1)

    return x
# define a video capture object
vid = cv2.VideoCapture(0)
gray=None
model = SignLangModel() 
torch.save(model.state_dict(), 'model_trained.pt')
model.load_state_dict(torch.load('model_trained.pt'))
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(gray.dtype)
    converter = T.ToTensor()
    gray = converter(gray)
    print(gray.dtype)
    gray = gray.unsqueeze(0)
    print(gray.dtype)
    out = model(gray)

    probs, label = torch.topk(out, 25)
    pred = out.max(1, keepdim=True)[1]
    print(chr(97+pred))
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


learning_rate = 1e-3
batch_size = 64
epochs = 5
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # Compute prediction and loss
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")

