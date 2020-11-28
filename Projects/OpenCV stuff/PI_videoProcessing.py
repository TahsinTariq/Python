import cv2
import datetime
import keyboard
import numpy as np
from PIL import Image, ImageFilter

def remap(value, source_s, source_e, start, end):
    return start + ((value - source_s) / (source_e-source_s)) * (end-start)

def change_brightness(img: Image, level: float) -> Image:
    def brightness(c: int) -> float:
        return 128 + level + (c - 128)
    if not -255.0 <= level <= 255.0:
        raise ValueError("level must be between -255.0 (black) and 255.0 (white)")
    return img.point(brightness)

def brighten(img, val):
    return cv2.convertScaleAbs(img, alpha=val[0], beta=val[1])

def brighten2(img, val2):
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    brightened_pil = change_brightness(pil_img, val2[0])
    brightened_cv = cv2.cvtColor(np.array(brightened_pil), cv2.COLOR_RGB2BGR)
    return brightened_cv

def sharpen(img, val):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    kernel = np.array([[-1, -1, -1],
                       [-1, val[0], -1],
                       [-1, -1, -1]
                       ])
    return cv2.filter2D(img, -1, kernel)

def UnsharpMask(img):
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    pil = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
    return cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)

def medianBlur(img):
    return cv2.medianBlur(img, 5)

class capture_mouse:

    def __init__(self, window_name : str, x : list, y: list = None):
        self.window = window_name
        self.val = [0,0]
        self.x = x
        self.y = y

    def mouse(self):
        self.do_the_thing()
        return self.val

    def do_the_thing(self):
        cv2.setMouseCallback(self.window, self.mouse_event)

    def mouse_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            self.val[0] = remap(x, 0, 640, *self.x)
            if not self.y==None:
                self.val[1] = remap(y, 0, 480, *self.y)
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print("Clicked")
            cv2.imwrite(f"photos/{str(datetime.datetime.now().strftime('%H_%M_%S'))}.png", processed3)
            # print(f"brightness : {self.val}")

    def show(self, img):
        cv2.imshow(self.window, img)


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    window1 = capture_mouse("process1", [0,10])
    window2 = capture_mouse("process2", [5, 15])
    window3 = capture_mouse("process3", [5, 15], [5, 15])

    while True:
        ret, img = cap.read()

        # processed1 = brighten(img, window1.mouse())
        # processed2 = brighten2(img, window2.mouse())
        # processed1 = medianBlur(sharpen(UnsharpMask(img), window1.mouse()))
        processed1 = sharpen(medianBlur(img), window1.mouse())
        # processed2 = medianBlur(sharpen(img, window2.mouse()))
        # processed3 = sharpen(processed2 ,window3.mouse())
        processed3 = sharpen(processed1 ,window3.mouse())

        window1.show(processed1)
        # window2.show(processed2)
        window3.show(processed3)

        cv2.waitKey(1)
        # if keyboard.is_pressed('s'):
        #     name  = str(datetime.datetime.now().strftime('%H_%M_%S'))
        #     print(type(name))
        #     cv2.imwrite(f"photos/{name}.png", img)
        if keyboard.is_pressed('q'):
            break
    cap.release()
    cv2.destroyAllWindows()