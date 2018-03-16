
import movement
import camera
import os

import h5py
import numpy as np
from keras.models import load_model
from keras.models import Model
from PIL import Image

import sys
sys.path.append('/home/pi/Documents/Self-driving-car')
sys.path.append()
sys.path.append()
sys.path.append()

print("Wait please")
p = 3
tf = 1
camera.init()
movement.init()
model = load_model('my_model.h5')
print("Camera initialized, go ahead!")
correct = 'w'
while correct != 'q':
    imageName = camera.take_picture_return()
    image = Image.open(imageName)
    image = np.array(image)
    p = model.predict(np.expand_dims(image, axis=0))
    print(p)
    p = np.argmax(p, axis = 1)
    p=p[0]
    print(p)

    correct = input('Enter correct prediction')  # previously raw_input()

    if correct == 'w':
        camera.take_picture()
        os.rename("/home/pi/Documents/Self-driving-car/"+imageName, "home/pi/Documents/Self-driving-car/images/w/"+imageName)
        movement.forward(tf)

    elif correct == 'd':
        camera.take_picture()
        os.rename("/home/pi/Documents/Self-driving-car/"+imageName, "home/pi/Documents/Self-driving-car/images/d/"+imageName)
        movement.right(tf)

    elif correct == 'a':
        camera.take_picture()
        os.rename("/home/pi/Documents/Self-driving-car/"+imageName, "home/pi/Documents/Self-driving-car/images/a/"+imageName)
        movement.left(tf)

    elif correct == 'q':
        camera.end()
    

