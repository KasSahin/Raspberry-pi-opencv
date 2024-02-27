

import cv2
import pytesseract

img=cv2.imread("/home/barbaros/Desktop/ryo/yp/poe.png")
text=pytesseract.image_to_string(img,lang="eng")
print(text)


cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()