import cv2

import unittest
import zbarlight
import zxing

from Recognition.Recognition import Recognition


class TestQrRecognition(unittest.TestCase):

    def test_can_find_qrs_on_qr_image(self):
        img = cv2.imread('../examples/qr.jpg')
        recognition = Recognition(img)

        result = recognition.recognize()

        self.assertEqual(10, len(result['qr']))

    def test_find_qr_on_image_7(self):
        img = cv2.imread('../examples/7.jpg')
        recognition = Recognition(img)

        result = recognition.recognize()

        self.assertEqual(1, len(result['qr']))

    def test_find_qr_on_image_8(self):
        img = cv2.imread('../examples/8.jpg')

        reader = zxing.BarCodeReader()
        barcode = reader.decode("../examples/8.jpg")
        print(barcode)

        recognition = Recognition(img)

        recognition.dd(img)
        result = recognition.recognize()
        print(result)

        self.assertEqual(1, len(result['qr']))

    def test_find_qr_on_image_9(self):
        img = cv2.imread('../examples/9.jpg')
        recognition = Recognition(img)

        recognition.dd(img)
        result = recognition.recognize()
        print(result)

        self.assertEqual(1, len(result['qr']))

    def test_find_qr_on_image_10(self):
        img = cv2.imread('../examples/10.jpg')
        recognition = Recognition(img)

        result = recognition.recognize()

        self.assertEqual(1, len(result['qr']))

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
