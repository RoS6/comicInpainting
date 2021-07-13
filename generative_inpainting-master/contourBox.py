import cv2

def findContour(image):
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    eg = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    cv2.imshow('im2',im2)
    # cv2.imshow('contours',contours)
    print(contours)
    cv2.imshow('eg',eg)

    cv2.waitKey(0)

image = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\tempB.png")
image = image.astype('uint8')
findContour(image)