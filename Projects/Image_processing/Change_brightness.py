import numpy
from PIL import Image
import cv2 as cv

def change_brightness(img: Image, level: float) -> Image:
    """
    Change the brightness of a PIL Image to a given level.
    """

    def brightness(c: int) -> float:
        """
        Fundamental Transformation/Operation that'll be performed on
        every bit.
        """
        return 128 + level + (c - 128)

    if not -255.0 <= level <= 255.0:
        raise ValueError("level must be between -255.0 (black) and 255.0 (white)")
    return img.point(brightness)


if __name__ == "__main__":
    # Load image
    with Image.open("shaan.jpg") as img:
        # Change brightness to 100
        bright_img = change_brightness(img, 100)
        a = cv.cvtColor(numpy.array(bright_img), cv.COLOR_RGB2BGR)

    while True:
        cv.imshow("b", a)
        cv.waitKey(30)
