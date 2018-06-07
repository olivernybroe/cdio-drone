from pyzbar.pyzbar import decode
from pyzbar.wrapper import ZBarSymbol
from Recognition.Figure import Polygon, Point


class Qr:
    @staticmethod
    def recognize(image):
        return Qr.transform(decode(image, symbols=[ZBarSymbol.QRCODE]))

    @staticmethod
    def transform(qrs):
        result = []
        for qr in qrs:
            points = []
            for point in qr.polygon:
                points.append(Point(point.x, point.y))

            result.append({
                'data': str(qr.data)[2:6],
                'location': Polygon(*points)
            })
        return result
