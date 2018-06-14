from cv2 import cv2
from darkflow.net.build import TFNet

from Recognition.QR import Qr
from Recognition.CV2Finder import CV2Finder
import numpy as np


class Recognition:
    image = None

    def __init__(self, threshold=0.8):
        """
        Construct the recognition object.

        When using the recognition supply it a image and later call recognize
        and it will return with the results of where it has found QR codes and
        where it found rings.

        :param image:
        """
        options = {"pbLoad": "Yolo/tiny-yolo-voc-2c.pb",
                   "metaLoad": "Yolo/tiny-yolo-voc-2c.meta",
                   "threshold": threshold,
                   # "verbalise": False,
                   }

        self.tf_net = TFNet(options)

    def recognize(self, image):
        result = self.tf_net.return_predict(image)
        return result

        # cv2_result = self._find_with_cv2(image)

        # return {
        #     'qr': self._find_from_qr() + cv2_result['qr'],
        #     'rings': cv2_result['rings']
        # }

    @staticmethod
    def dd(image):
        Recognition.show(image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        exit(0)

    @staticmethod
    def show(image):
        result = Recognition().recognize(image)

        polygon = []
        for qr in result['qr']:
            pts = np.array(
                list(
                    map(lambda point: [point.x, point.y],
                        qr['location'].points)
                ),
                np.int32
            ).reshape((-1, 1, 2))
            polygon.append(pts)

        for ring in result['rings']:
            cv2.ellipse(
                img=image,
                center=(int(ring.center.x), int(ring.center.y)),
                axes=(int(ring.maxLength), int(ring.minLength)),
                angle=ring.angle,
                color=(0, 255, 255),
                startAngle=0,
                endAngle=360
            )

        cv2.polylines(image, polygon, True, (0, 255, 255))
        cv2.imshow('detected circles', image)
        cv2.moveWindow('detected circles', 20, 20)

    def _find_from_qr(self, image):
        return Qr.recognize(image)

    def _find_with_cv2(self, image):
        return CV2Finder(image).recognize()
