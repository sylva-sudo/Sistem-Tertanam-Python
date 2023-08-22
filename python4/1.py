import cv2
webcam=cv2.VideoCapture(0)

ret, image=webcam.read()
if ret:
    cv2.imshow("capture01", image)
    cv2.imwrite("capture01.png", image)
    cv2.waitKey(0)
    cv2.destroyWindow("capture01")
else:
 print("gambar tidak terdeteksi, silakan dicoba lagi")
