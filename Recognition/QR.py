from pyzbar.pyzbar import decode
from pyzbar.wrapper import ZBarSymbol


class Qr:

    @staticmethod
    def regonise(image):
        return decode(image, symbols=[ZBarSymbol.QRCODE])
