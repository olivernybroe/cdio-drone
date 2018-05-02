from Recognition.QR import Qr


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
        return {
            'qr': self._find_qr(),
            'rings': []
        }

    def _find_qr(self):
        return Qr.recognize(self.image)

