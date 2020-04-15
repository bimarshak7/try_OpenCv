import cv2
import numpy as np
def contours(img):
	contour,hierarchay=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contour:
		area=cv2.contourArea(cnt)
		if area>400:
			cv2.drawContours(imgc,cnt,-1,(255,0,0),3)
			per=cv2.arcLength(cnt,True)
			approx=cv2.approxPolyDP(cnt,0.05*per,True)
			objcor=len(approx)
			x,y,w,h=cv2.boundingRect(approx)
			if objcor==3: objtype="Triangle"
			elif objcor==4:
				aspectratio=w/float(h)
				if aspectratio>0.95 and aspectratio<1.05: objtype="square"
				else: objtype="rectangle"
			elif objcor==5:objtype="Pentagon"
			else: objtype="Circle"
			cv2.rectangle(imgc,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(imgc,objtype,(x+(w//2)-40,y+(h//2)+40),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),1)
cap=cv2.VideoCapture(0)
while True:
	sucess,img=cap.read()
	#img=cv2.imread("shapes.png")
	imgc=img.copy()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur=cv2.GaussianBlur(gray,(7,7),1)
	canny=cv2.Canny(blur,40,20)
	contours(canny)
	cv2.imshow("Shape Detect",imgc)
	if(cv2.waitKey(1)==27):
		break