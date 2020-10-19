import cv2
import numpy as np
import keyboard

# face = cv2.CascadeClassifier('hogcascade_pedestrians.xml')
# face = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# face = cv2.CascadeClassifier('haarcascade_eye.xml')
# face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
# for external USB cameras
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
img_translation =0
while True:
    hat = cv2.imread("hat.png")
    num_rows, num_cols = hat.shape[:2]
    ret, img = cap.read()
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(width, height)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        translation_matrix = np.float32([[1, 0, 70], [0, 1, 110]])
        img_translation = cv2.warpAffine(hat, translation_matrix, (num_cols, num_rows))
    img = cv2.addWeighted(img, 0.4, img_translation, 0.1, 0)
    cv2.imshow('img', img)
    # cv2.imshow('img', img_translation)
    cv2.waitKey(30)
    if keyboard.is_pressed('q'):
        break
cap.release()
cv2.destroyAllWindows()




# import cv2
# from math import sin, cos, radians
#
# camera =  cv2.VideoCapture(0)
# face = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
# profile = cv2.CascadeClassifier("haarcascade_profileface.xml")
#
# settings = {
#     'scaleFactor': 1.3,
#     'minNeighbors': 3,
#     'minSize': (50, 50),
#     # 'flags': cv2.cv.CV_HAAR_FIND_BIGGEST_OBJECT|cv2.cv.CV_HAAR_DO_ROUGH_SEARCH
# }
#
# def rotate_image(image, angle):
#     if angle == 0: return image
#     height, width = image.shape[:2]
#     rot_mat = cv2.getRotationMatrix2D((width/2, height/2), angle, 0.9)
#     result = cv2.warpAffine(image, rot_mat, (width, height), flags=cv2.INTER_LINEAR)
#     return result
#
# def rotate_point(pos, img, angle):
#     if angle == 0: return pos
#     x = pos[0] - img.shape[1]*0.4
#     y = pos[1] - img.shape[0]*0.4
#     newx = x*cos(radians(angle)) + y*sin(radians(angle)) + img.shape[1]*0.4
#     newy = -x*sin(radians(angle)) + y*cos(radians(angle)) + img.shape[0]*0.4
#     return int(newx), int(newy), pos[2], pos[3]
#
# while True:
#     ret, img = camera.read()
#
#     for angle in [0, -25, 25]:
#         rimg = rotate_image(img, angle)
#         detected = face.detectMultiScale(rimg, **settings)
#         detectedP = face.detectMultiScale(rimg, **settings)
#         if len(detected):
#             detected = [rotate_point(detected[-1], img, -angle)]
#             break
#         if len(detectedP):
#             detectedP = [rotate_point(detectedP[-1], img, -angle)]
#             break
#
#     # Make a copy as we don't want to draw on the original image:
#     for x, y, w, h in detected[-1:]:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
#     for x, y, w, h in detectedP[-1:]:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
#
#     cv2.imshow('facedetect', img)
#
#     if cv2.waitKey(5) != -1:
#         break
#
# cv2.destroyWindow("facedetect")