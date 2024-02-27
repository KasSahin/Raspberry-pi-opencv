import cv2
img=cv2.imread("/home/barbaros/Desktop/opencv/open1/resm/2.jpg")
img2=cv2.imread("/home/barbaros/Desktop/opencv/open1/resm/1.jpg")

cv2.imshow("1",img)
cv2.imshow("2",img2)


result=cv2.addWeighted(img,0.3,img2,0.7,0)
cv2.imshow("add",result)
cv2.waitKey(0)
cv2.destroyAllWindows()