from SimpleCV import Camera, Display
import time
#initialize the IP cameras
cam1 = Camera(0)
cam2 = Camera(1)
cam3 = Camera(0)
cam4 = Camera(0)
display = Display((640,480))
while not display.isDone():
	img1 = cam1.getImage().resize(320, 240)
	img2 = cam2.getImage().resize(320, 240)
	img3 = cam3.getImage().resize(320, 240)
	img4 = cam4.getImage().resize(320, 240)
	top = img1.sideBySide(img2)
	bottom = img3.sideBySide(img4)
	combined = top.sideBySide(bottom, side="bottom")
	combined.save(display)
	time.sleep(5)