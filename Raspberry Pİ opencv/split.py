import cv2
img=cv2.imread("/home/barbaros/Desktop/opencv/open1/opn.jpg")
b,g,r=cv2.split(img)

merge=cv2.merge((b,g,r))

cv2.imshow("merge",merge)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow("frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
