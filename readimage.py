import cv2
img = cv2.imread("butterfly.jpg")
cv2.imshow("displayimage", img)
#print(img)
greyimage = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale", greyimage)
print(greyimage)
cv2.waitKey(0)