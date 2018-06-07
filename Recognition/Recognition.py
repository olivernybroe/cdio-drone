from cv2 import cv2

from Recognition.QR import Qr
from Recognition.CV2Finder import CV2Finder


class Recognition:

    image = None

    def __init__(self, image):
        """
        Construct the recognition object.

        When using the recognition supply it a image and later call recognize
        and it will return with the results of where it has found QR codes and
        where it found rings.

        :param image:
        """
        self.image = image

    def recognize(self):
        cv2_result = self._find_with_cv2()

        return {
            'qr': self._find_from_qr() + cv2_result['qr'],
            'rings': cv2_result['rings']
        }

    def _find_from_qr(self):
        return Qr.recognize(self.image)

    def _find_with_cv2(self):
        return CV2Finder(self.image).recognize()

