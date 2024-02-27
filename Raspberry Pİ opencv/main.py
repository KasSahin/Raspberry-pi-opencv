import cv2

image=cv2.imread("22.jpg",0)

print(image[1500,1400])
roi =image[0:1500,0:1400] 
cv2.imshow("roi",roi)

cv2.imshow("frame",image)
cv2.waitKey(0)
cv2.destroyAllWindows()