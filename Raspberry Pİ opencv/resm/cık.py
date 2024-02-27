import cv2
img=cv2.imread("/home/barbaros/Desktop/opencv/open1/resm/grey1.jpg")
img2=cv2.imread("/home/barbaros/Desktop/opencv/open1/resm/grey2.jpg")

result=cv2.subtract(img,img2)

cv2.imshow("add",result)
cv2.imshow("1",img)
cv2.imshow("2",img2)
cv2.waitKey()
cv2.destroyAllWindows()