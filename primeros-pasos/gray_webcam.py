import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capturar cuadro por cuadro
    ret, frame = cap.read()

    # si el cuadro se esta leyendo correctamente ret sera True
    if not ret:
        print("Can't reeceive frame (stream end?). Exiting...")

    # Nuestra operacion en el cuadro comienza aqui
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Mostrando el resultado en el cuadro
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break

# Cuando todo esta hecho, realizamos la captura
cap.release()
cv.destroyAllWindows()
