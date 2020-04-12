import cv2
import numpy as np
img=cv2.imread("ronaldo.jpeg")
facecas=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
	sucess,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	face=facecas.detectMultiScale(img,1.1,4)
	for (x,y,w,h) in face:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,103,140),7)
	cv2.imshow("FACE",img)
	if(cv2.waitKey(1)==27):
		break