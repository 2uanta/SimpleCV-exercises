from SimpleCV import JpegStreamCamera
# Initialize the webcam by providing URL to the camera
cam = JpegStreamCamera("http://142.157.159.116:8080/video.jpeg?sessionId=1378236515.816177")
cam.getImage().show()