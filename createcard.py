import cv2
img = cv2.imread("poster.jpg")
rocket = img[120:360, 400:500]
img[0:240, 500:600] = rocket

text2show = "Rocket go boom"
cv2.putText(img, text2show, (20,220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=1, color=(99,25,255))
cv2.imshow ("display", img)
cv2.waitKey(0)