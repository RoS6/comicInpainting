import cv2
import numpy as np
refPt = []
cropping = False
def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


image = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\003.png")
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
h,w= image.shape[0:2]
input = image.copy()
mask = np.zeros((h,w,4))
white_colour = (255,255,255,255)
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
    elif key == ord('p'):
        import sys
        sys.exit()

layer1 = np.zeros((h, w, 4))

# cv2.rectangle(layer1, refPt[0], refPt[1], (255,255,255,255), -1)

# res = layer1[:]
if len(refPt) == 2:
    tempImage = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.imshow("ROI", tempImage)
    cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\temp.png", tempImage)
# cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\maskT3.png", res)
# cv2.rectangle(input, refPt[0], refPt[1], (255,255,255), -1)
# cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\inputT3.png",input)

# Load image, grayscale, Gaussian blur, adaptive threshold
temp = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\temp.png")
# temp = temp.astype('uint8')
# gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (3,3), 0,)
# thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
#
# # Dilate to combine adjacent text contours
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
# dilate = cv2.dilate(thresh, kernel, iterations=4)
#
# # Find contours, highlight text areas, and extract ROIs
# cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#
# ROI_number = 0
# for c in cnts:
#     area = cv2.contourArea(c)
#     if area > 10000:
#         x,y,w,h = cv2.boundingRect(c)
#         cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 3)
#         # ROI = image[y:y+h, x:x+w]
#         # cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
#         # ROI_number += 1
#
# cv2.imshow('thresh', thresh)
# cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\thresh.png", thresh)
# thresh_to_mask = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\thresh.png")
# # to_mask = cv2.cvtColor(thresh_to_mask, cv2.COLOR_BGR2BGRA)
# # dst = cv2.warpPerspective(to_mask, lambda_val, (992,728), flags = cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue = [0, 0, 0, 0])
# print(thresh_to_mask)
# for i in range(len(thresh_to_mask)):
# 	for j in range(len(thresh_to_mask[0])):
# 		if image[i,j].all() == 255:
# 			cv2.circle(layer1,(refPt[0,0]+i, refPt[0,1]+j),0,(255,255,255,255),5)
# 			print(str((refPt[0,0]+i, refPt[0,1]+j)))
# res = layer1[:]
gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('thresh', thresh)

im2, ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)

    roi = temp[y:y + h, x:x + w]

    area = w*h

    if 250 < area < 900:
        rect = cv2.rectangle(temp, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('rect', rect)

cv2.waitKey(0)
# cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\maskT4.png", res)



# cv2.imshow('dilate', dilate)
# cv2.imshow('image', image)
# cv2.waitKey()