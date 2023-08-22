import cv2

img=cv2.imread("foto1.jpg",0) 
#isi dengan 0 atau 1 / cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCAHNGED
img2=cv2.imread("foto2.jpg",cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.imshow("image2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()