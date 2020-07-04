import cv2
import keyboard
for i in range(1):
    try:
        if i < 10:
            img = cv2.imread('E:/Assignment/For Maliha apu/dataset-master/dataset-master/JPEGImages/BloodImage_0000' + str(1) +'.jpg')
        #   # if i < 10:
        #     img = cv2.imread('E:/Assignment/For Maliha apu/dataset-master/dataset-master/JPEGImages/BloodImage_0000' + str(i) +'.jpg')

        # if 9 < i < 100:
        #     img = cv2.imread('E:/Assignment/For Maliha apu/dataset-master/dataset-master/JPEGImages/BloodImage_000' + str(i) +'.jpg')
        # if 99 < i < 1000:
        #     img = cv2.imread('E:/Assignment/For Maliha apu/dataset-master/dataset-master/JPEGImages/BloodImage_00' + str(i) +'.jpg')
        # cv2.imshow('image', img)
        # flags, hcursor, (x, y) = win32gui.GetCursorInfo()
        ret, thresh = cv2.threshold(img, 115, 117, cv2.THRESH_BINARY)
        gray = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray",gray)
        edged = cv2.Canny(gray, 30, 200)
        contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # cv2.imshow('Canny Edges After Contouring', edged)
        print("1")
        cv2.imshow('Contours',hierarchy)
        print("2")
        cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
        cv2.imshow('Contours', img)
        print("3")
    except Exception as e:
        print(e)
        print("4")
    finally:
        if keyboard.is_pressed("q"):
            break
        cv2.waitKey(30)
