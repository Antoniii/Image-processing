# conda activate value

"""
Python 3.6.5 [GCC 4.8.2 20140120 (Red Hat 4.8.2-15)]
cv2 3.4.1
numpy 1.14.4
matplotlib 2.2.2
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def nothing(*args, **kwargs):
	pass

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_aspect('equal')

#cap = cv2.VideoCapture(0) # arg = 0 or 1 for input camera, -1 for anyone free 
#cap = cv2.VideoCapture("video-test.mp4")
frame = cv2.imread('photo-test\photo-test-2.png') # for image

cv2.namedWindow( "settings" ) # create a settings window
# create 6 sliders to adjust the start and end color of the filter
cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
crange = [0,0,0, 0,0,0]

def animate(i):
    #_, frame = cap.read() # for video
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # read the values of the sliders
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')

    # form the initial and final color of the filter
    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    # impose a filter on the frame in the HSV model
    thresh = cv2.inRange(hsv, h_min, h_max)
    edges = cv2.Canny(thresh, 100, 200)

    cv2.imshow('frame', frame)
    cv2.imshow('edges', edges)

# create a window with animated construction of points to determine the distance between them
    
    x, y = np.meshgrid(np.arange(edges.shape[1]),
                       np.arange(edges.shape[0]))
    x = x[edges!=0]
    y = edges.shape[0] - 1 - y[edges!=0]
    ax1.clear()
    ax1.set_xlim([0, edges.shape[1]-1])
    ax1.set_ylim([0, edges.shape[0]-1])
    ax1.plot(x, y, 'k.', markersize=.5)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
