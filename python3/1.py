import cv2
webcam=cv2.VideoCapture(0)
while True:
    ret, frame = webcam.read()
    cv2.imshow("From webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()
