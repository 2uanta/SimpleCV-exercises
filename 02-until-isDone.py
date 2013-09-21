from SimpleCV import Display, Image
import time
display = Display()
Image("logo").save(display)
print "I launched a window"
# This while loop will keep looping until the window is closed
while not display.isDone():
  time.sleep(0.1)
print "You closed the window"