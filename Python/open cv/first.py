import cv2 as cv


image = cv.imread("Ishtar.jpg")

rez = cv.resize(image,(320,80))

crop = image[100:400,200:700]


cv.imshow("Ishtar.jpg",image)
cv.imshow("rez",rez)
cv.imshow("crop",crop)



cv.waitKey(0)


cv.destroyAllWindows()
