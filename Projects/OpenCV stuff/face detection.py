import cv2
import keyboard

# face = cv2.CascadeClassifier('hogcascade_pedestrians.xml')
# face = cv2.CascadeClassifier('haarcascade_fullbody.xml')
face = cv2.CascadeClassifier('haarcascade_eye.xml')
# face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(30)
    if keyboard.is_pressed('q'):
        break
cap.release()
cv2.destroyAllWindows()