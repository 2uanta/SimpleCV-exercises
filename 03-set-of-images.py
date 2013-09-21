from SimpleCV import Camera, ImageSet
import time
cam = Camera()
camImages = ImageSet()
# Set to a maximum of 10 images saved
# Feel free to increase, but beware of running out of space
maxImages = 5
for counter in range(maxImages):
  # Capture a new image and add to set
  img = cam.getImage()
  camImages.append(img)
  # Show the image and wait before capturing another
  img.show()
  time.sleep(2)
camImages.save(destination='imageset1', verbose=True)
