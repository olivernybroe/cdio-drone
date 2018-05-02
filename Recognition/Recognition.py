from Recognition.QR import Qr


class Recognition:

    image = None

    def __init__(self, image):
        self.image = image

    def recognize(self):
        return self._find_qr()

    def _find_qr(self):
        return Qr.recognize(self.image)

