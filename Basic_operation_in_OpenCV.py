import cv2 as cv

img = cv.imread("abert.jpg", 1)

cv.imshow("Image", img)
e = cv.waitKey()
e
if e == 27:
    cv.destroyAllWindows()
elif e == ord("s"):
    cv.imwrite("The-New_Albert.jpg", img)
    cv.destroyAllWindows()
