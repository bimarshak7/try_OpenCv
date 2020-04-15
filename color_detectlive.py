import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver




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
	sucess,img=cap.read()
	imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	hmin=cv2.getTrackbarPos("HUE min","TrackBars")
	hmax=cv2.getTrackbarPos("HUE Max","TrackBars")
	smin=cv2.getTrackbarPos("Satur min","TrackBars")
	smax=cv2.getTrackbarPos("Satur max","TrackBars")
	vmin=cv2.getTrackbarPos("Val min","TrackBars")
	vmax=cv2.getTrackbarPos("Val max","TrackBars")	
	print(hmin,hmax,smin,smax,vmin,vmax)
	low=np.array([hmin,smin,vmin])
	up=np.array([hmax,smax,vmax])
	mask=cv2.inRange(imghsv,low,up)
	res=cv2.bitwise_and(img,img,mask=mask)
	mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
	hstack=np.hstack([img,mask,res])
	cv2.imshow("FACE",hstack)
	if(cv2.waitKey(1)==27):
		break
cv2.destroyAllWindows()