import cv2 as cv


image = cv.imread("Ishtar.jpg")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)
cv.imshow("Ishtar.jpg",image)


cv.waitKey(0)


cv.destroyAllWindows()
