from SimpleCV import Camera
# First attached camera
cam0 = Camera(0)
# Second attached camera
cam1 = Camera(1)
# Show a picture from the first camera
img0 = cam0.getImage()
img0.drawText("I am Camera ID 0")
img0.show()
# Show a picture from the first camera
img1 = cam1.getImage()
img1.drawText("I am Camera ID 1")
img1.show()