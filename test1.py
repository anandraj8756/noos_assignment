import numpy as np
import cv2


width, height = 250, 550
img = cv2.imread("warped_qrcode.png")

pts1 = np.float32([[1,75], [409,75], [3,425], [410,421]])

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width,height))

print(imgOutput)


for x in range(0, 4):
	cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0,0,255), cv2.FILLED)


cv2.imshow("Image", img)
cv2.imshow("WarpImage", imgOutput)
cv2.imwrite("save.png", imgOutput)			
cv2.waitKey(0)

