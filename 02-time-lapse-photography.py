from SimpleCV import Camera, Image
import time

cam = Camera()

# Set the number of frames to capture
numFrames = 10

# Loop until we reach the limit set in numFrames
for x in range(0, numFrames):
  img = cam.getImage()
  
  filepath = "image-" + str(x) + ".jpg"
  img.save(filepath)
  print "Saved image to: " + filepath
  
  time.sleep(5)