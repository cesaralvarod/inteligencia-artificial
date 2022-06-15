import cv2

cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('AIOTPERU', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('a'):  # no entiendo esta linea
        cv2.imwrite("test.jpg", frame)
    if key & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
