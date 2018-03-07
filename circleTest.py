import cv2
import numpy as np
import json
from pyzbar.pyzbar import decode

img = cv2.imread('examples/4.jpg', 0)
#img = cv2.medianBlur(img, 3)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(
    image=img,
    method=cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=100,
    param1=300
)

circles = np.uint16(np.around(circles))

jsonCircles = []
for i in circles[0, :]:
    jsonCircles.append({
        'center': {
            'x': int(i[0]),
            'y': int(i[1])
        },
        'radius': int(i[2])
    })


qrs = decode(img)

print(qrs)

    
print(json.dumps(jsonCircles))

for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
