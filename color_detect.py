import numpy as np
import cv2
#path for image
path="opencv/samples/data/WindowsLogo.jpg"
def empty(x):
	pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("HUE min","TrackBars",85,179,empty)
cv2.createTrackbar("HUE Max","TrackBars",118,179,empty)
cv2.createTrackbar("Satur min","TrackBars",128,255,empty)
cv2.createTrackbar("Satur max","TrackBars",255,255,empty)
cv2.createTrackbar("Val min","TrackBars",0,255,empty)
cv2.createTrackbar("Val max","TrackBars",255,255,empty)
while True:
	img=cv2.imread(path)
	HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	hmin=cv2.getTrackbarPos("HUE min","TrackBars")
	hmax=cv2.getTrackbarPos("HUE Max","TrackBars")
	smin=cv2.getTrackbarPos("Satur min","TrackBars")
	smax=cv2.getTrackbarPos("Satur max","TrackBars")
	vmin=cv2.getTrackbarPos("Val min","TrackBars")
	vmax=cv2.getTrackbarPos("Val max","TrackBars")	
	print(hmin,hmax,smin,smax,vmin,vmax)
	low=np.array([hmin,smin,vmin])
	up=np.array([hmax,smax,vmax])
	mask=cv2.inRange(HSV,low,up)
	imgres=cv2.bitwise_and(img,img,mask=mask)
	cv2.imshow("OUTPUT",imgres)
	print(hmin)
	if(cv2.waitKey(1)==ord('q')):
		break
cv2.destroyAllWindows()
