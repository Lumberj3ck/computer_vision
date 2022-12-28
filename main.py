import cv2


img = cv2.imread('cover.jpg')

while True:
    cv2.imshow('Application', img)
    key = cv2.waitKey(1)
    cv2.rectangle(img, (50, 50), (900, 900), (0, 220, 220), 2)
    cv2.imwrite('output.jpg', img)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
