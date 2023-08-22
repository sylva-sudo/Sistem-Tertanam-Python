import cv2

img=cv2.imread("foto1.jpg",1) #diisi dengan 0 atau 1
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()