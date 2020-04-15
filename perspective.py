import numpy as np
import cv2
#img=np.zeros((512,512,3),np.uint8)
#img=cv2.imread("res.jpg")
width,height=250,350
#res=cv2.resize(img,(512,512))
pt1=np.float32([[200,115],[367,89],[276,448],[470,386]])
pt2=np.float32([[0,0],[width,0],[0,height],[width,height]])
cap=cv2.VideoCapture(0)
cap.set(4,512)
while True:
	sucess,img=cap.read()
	matrix=cv2.getPerspectiveTransform(pt1,pt2)
	out=cv2.warpPerspective(img,matrix,(width,height))
	cv2.imshow("OUTPUT",out)
	if(cv2.waitKey(1)==ord('q')):
		break
