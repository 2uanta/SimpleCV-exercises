from SimpleCV import JpegStreamCamera, Display
import time
#initialize the IP camera
cam = JpegStreamCamera("http://142.157.159.116:8080/video.jpeg?sessionId=1378236515.816177")
display = Display()
img = cam.getImage()
img.save(display)
while not display.isDone():
  img = cam.getImage()
  img.drawText(time.ctime())
  img.save(display)
  # This might be a good spot to also save to disk
  # But watch out for filling up the hard drive
  time.sleep(1)