import cv2
import numpy as np

from Recognition.Figure import Polygon, Point, Ellipse


class CV2Finder:

    def __init__(self, image):
        self.image = image
        self.rings = []
        self.qrs = []

    def recognize(self):
        gray = self.image.copy()
        gray = cv2.bilateralFilter(gray, 5, 17, 17)
        edged = cv2.Canny(gray, 200, 200)

        # find contours in the edged image, keep only the largest
        # ones, and initialize our screen contour
        _, contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                                          cv2.CHAIN_APPROX_SIMPLE)

        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        #cv2.drawContours(self.image, contours, -1, (0, 255, 0), 1)

        possible_rings = []
        possible_qrs = []
        for contour in contours:
            # approximate the contour
            peri = cv2.arcLength(contour, False)
            approx = cv2.approxPolyDP(contour, 0.03 * peri, True)
            # rings.append(approx)

            # Find all possible squares
            if len(approx) == 4:
                possible_qrs.append(approx)

            # Find all possible rings.
            if len(approx) > 8:
                ellipse = cv2.fitEllipse(approx)
                possible_rings.append(ellipse)

        # Find all qr codes
        #cv2.drawContours(self.image, possible_qrs, -1, (0, 255, 0), 1)
        for possible_qr in possible_qrs:
            contains = CV2Finder.contains(possible_qr, possible_qrs)
            #print(contains)
            # TODO: limit to not add qrs which is inside already added qrs.
            if (len(contains) >= 2 and
                    not any(
                        bool(CV2Finder.contains(qr, [possible_qr]))
                        for qr in self.qrs)):
                self.qrs.append(possible_qr)

        # Find all rings.
        for possible_ring in possible_rings:
            if CV2Finder.size(possible_ring) >= 100000:
                self.rings.append(possible_ring)

        return {
            'qr': CV2Finder.transform_qrs(self.qrs),
            'rings': CV2Finder.transform_rings(self.rings)
        }

    @staticmethod
    def contains(matchingContour, contours):
        (rt, lt, lb, rb) = matchingContour

        matches = []
        for contour in contours:
            (child_rt, child_lt, child_lb, child_rb) = contour

            # check if right top x is biggest and y is smallest
            if (rt[0][0] > child_rt[0][0] and rt[0][1] < child_rt[0][1] and
                    lt[0][0] < child_lt[0][0] and lt[0][1] < child_lt[0][1] and
                    lb[0][0] < child_lb[0][0] and lb[0][1] > child_lb[0][1] and
                    rb[0][0] > child_rb[0][0] and rb[0][1] > child_rb[0][1] and
                    CV2Finder.size(matchingContour) > CV2Finder.size(
                        contour) + 00):
                matches.append(contour)

        return matches

    @staticmethod
    def size(contour):
        try:
            return cv2.contourArea(contour)
        except TypeError:
            axes = contour[1]
            return np.pi * axes[0] * axes[1]

    @staticmethod
    def show(image):
        cv2.imshow('detected circles', image)
        cv2.moveWindow('detected circles', 20, 20)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def dd(self):
        cv2.drawContours(self.image, self.qrs, -1, (0, 255, 0), 3)
        [cv2.ellipse(self.image, ring, (0, 255, 0), 2) for ring in self.rings]
        CV2Finder.show(self.image)
        exit(0)

    @classmethod
    def transform_qrs(cls, qrs):
        result = []
        for qr in qrs:
            points = []
            for point in qr:
                points.append(Point(point[0][0], point[0][1]))

            result.append({
                'data': None,
                'location': Polygon(*points)
            })

        return result

    @classmethod
    def transform_rings(cls, rings):
        result = []
        for ring in rings:
            result.append(Ellipse(
                Point(ring[0][0], ring[0][1]),
                ring[1][0],
                ring[1][1],
                ring[2]
            ))

        return result
