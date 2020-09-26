import cv2
import converter

# Import picture & create HSI copy using algorithm
img = cv2.imread('ColorDetection_Plant.jpeg', 1)

hsi = cv2.resize(img, (400, 400))
hsi = converter.RGB_TO_HSI(hsi)

# Display HSV Image
cv2.imshow('HSI Image', hsi)

# The three value channels
cv2.imshow('H Channel', hsi[:, :, 0])
cv2.imshow('S Channel', hsi[:, :, 1])
cv2.imshow('I Channel', hsi[:, :, 2])

# Wait for a key press and then terminate the program
cv2.waitKey(0)
cv2.destroyAllWindows()