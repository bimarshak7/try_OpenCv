import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

colors = [[110,28,125,130,229,255],
            [73,44,0,98,255,255],
            [2,100,0,155,146,255],
            [57,76,0,100,255,255]
            ]
mycolor=[[255,0,255]
		,[0,255,0]
		,[51,153,255]
		,[255, 128, 0]
		]
points=[]#[x,y,colorindex]
def findcolor(img,colors,mycolor):
	HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	count=0
	newpoints=[]
	for color in colors:
		low=np.array(color[0:3])
		up=np.array(color[3:6])
		mask=cv2.inRange(HSV,low,up)
		x,y=contours(mask)
		cv2.circle(imgres,(x,y),10,mycolor[count],cv2.FILLED)
		if x!=0 and y!=0:newpoints.append([x,y,count])
		count+=1
	return newpoints

def contours(img):
	x,y,w,h=0,0,0,0
	contour,hierarchay=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contour:
		area=cv2.contourArea(cnt)
		if area>700:
			#cv2.drawContours(imgres,cnt,-1,(255,0,0),1)
			per=cv2.arcLength(cnt,True)
			approx=cv2.approxPolyDP(cnt,0.05*per,True)
			x,y,w,h=cv2.boundingRect(approx)
	return x+w//2,y

def draw(points,mycolor):
	for point in points:
		cv2.circle(imgres,(point[0],point[1]),10,mycolor[point[2]],cv2.FILLED)

while True:
	sucess,img=cap.read()
	imgres=img.copy()
	newpoints=findcolor(img,colors,mycolor)
	if len(newpoints)!=0:
		for newpoint in newpoints:
			points.append(newpoint)
	if len(points)!=0:
		draw(points,mycolor)
	cv2.imshow("COLOR",imgres)
	if(cv2.waitKey(1)==27):
		break