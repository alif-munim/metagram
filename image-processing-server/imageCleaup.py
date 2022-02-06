import cv2
import numpy as np


class ImageProcessing:

    def __init__(self, img_path):
        self.img = cv2.imread(img_path)

    def sharpen(self, img):
        sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen = cv2.filter2D(img, -1, sharpen_kernel)
        sharpen = cv2.GaussianBlur(sharpen, (5, 5), 0)
        sharpen = cv2.addWeighted(img, 1.5, sharpen, -0.5, 0)
        sharpen = cv2.bilateralFilter(sharpen, 9, 80, 80)
        return sharpen

    def resize(self):
        h, w = self.img.shape[0],  self.img.shape[1]
        new_img = self.img
        if h > 1000 or w > 1700:
            new_img = cv2.resize(self.img, (int(w*0.6), int(h*0.6)))
        return new_img

    def process_all(self, export=False, outputName=None):
        img = self.resize()
        # img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10,
        #                                              7, 21)
        # img = self.sharpen(img)

        # blur
        blur = cv2.GaussianBlur(img, (5, 5), 0)

        # convert to hsv and get saturation channel
        sat = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)[:, :, 1]

        # threshold saturation channel
        thresh = cv2.threshold(sat, 50, 255, cv2.THRESH_BINARY)[1]

        # apply morphology close and open to make mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
        mask = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel, iterations=1)

        # do OTSU threshold to get circuit image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[
            1]

        # write black to otsu image where mask is black
        otsu_result = otsu.copy()
        otsu_result[mask == 0] = 0

        # write black to input image where mask is black
        img_result = img.copy()
        img_result = cv2.fastNlMeansDenoisingColored(img_result, None, 10, 10, 7, 21)
        img_result = self.sharpen(img_result)
        if export:
            self.export_img(img_result, outputName)
        return img_result

    def export_img(self, img, name):
        cv2.imwrite(name + '.png', img)


if __name__ == "__main__":
    pic = ImageProcessing('img1.jpg')
    print(pic.img.shape)
    processed = pic.process_all(export=True, outputName='output')

    cv2.imshow('sample', processed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
