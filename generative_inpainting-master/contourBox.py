import cv2
import numpy as np


def findContour(image):
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # eg = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    # cv2.imshow('im2',im2)
    # cv2.imshow('contours',contours)
    # print(contours)
    # cv2.imshow('eg',eg)
    # cv2.waitKey(0)
    return contours

def cropText(image):
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
    clone2 = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            image = clone2.copy()
        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break
        elif key == ord('p'):
            import sys
            sys.exit()
    print(refPt)
    textPart = image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.rectangle(clone2, refPt[0], refPt[1], (255,255,255,255), -1)
    return textPart,clone2

# def findNearestContour(image,refPt,contour):
#     #left border:
#     point = refPt[0]
#     x = refPt[0][0]
#     y = refPt[0][1]
#     maskList = []
#     stop = False
#     # while True:
#         #check all left part
#     for i in range(0,500):
#         xh = x-i
#         # y = y-i
#         # if image[xh,y].all() == 255:
#         # if [xh, y] in contours:
#         if [[xh,y]] in totalC:
#             maskList.append([xh,y])
#             maskList.append([xh-1,y])
#             stop = True
#         else:
#             maskList.append([xh,y])
#         #left down part
#         for j in range (0,500):
#             xv = xh
#             yv = y-j
#             # if image[xv,yv].all() == 255:
#             # if [xv, yv] in contours:
#             if [[xv,yv]] in totalC:
#                 maskList.append([xv, yv])
#                 maskList.append([xv, yv - 1])
#                 break
#             else:
#                 maskList.append([xv,yv])
#         #left up part
#         for k in range (0,500):
#             xv = xh
#             yv = y+k
#             # if image[xv,y].all() == 255:
#             # if [xv, yv] in contours:
#             if [[xv,yv]] in totalC:
#                 maskList.append([xh, yv])
#                 maskList.append([xv, yv + 1])
#                 break
#             else:
#                 maskList.append([xv, yv])
#         if stop == True:
#             break
#     for l in range(0,500):
#         xr = x+l
#         # if image[xr,y].all() == 255:
#         # if [xr, y] in contours:
#         if [[xr,y]] in totalC:
#             maskList.append([xr,y])
#             maskList.append([xr-1,y])
#             stop = True
#         else:
#             maskList.append([xr,y])
#         #left down part
#         for j in range (0,500):
#             xv = xr
#             yv = y-j
#             # if [xv,yv] in contours:
#             if [[xv,yv]] in totalC:
#                 maskList.append([xv, yv])
#                 maskList.append([xv, yv - 1])
#                 break
#         #left up part
#             else:
#                 maskList.append([xv, yv])
#         for k in range (0,500):
#             xv = xr
#             yv = y+k
#             # if image[xv,y].all() == 255:
#             # if [xv, yv] in contours:
#             # if detect(xv,yv,contours):
#             if [[xv,yv]] in totalC:
#                 maskList.append([xv, yv])
#                 maskList.append([xv, yv + 1])
#                 break
#             else:
#                 maskList.append([xv, yv])
#             if stop == True:
#                 break
#     return maskList

# def detect(x,y,contours):
#     return [[x,y]] in totalC

refPt = []
cropping = False
image = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\tempB.png")
# h,w = image.shape[0]
# image = image.astype('uint8')
clone = image.copy()
textPart, input = cropText(image)
# clone = image.copy()
contours = findContour(textPart)
h,w = image.shape[0:2]
# totalC = []
# for i in contours:
#     for j in i:
#         totalC.append(j.tolist())
# textPart, input = cropText(image)
# # cv2.imshow('textPart',textPart)
# # cv2.imshow('input',input)
# contour= findNearestContour(input,refPt,contours)
# # # creating mask.png
# # h,w= image.shape[0:2]
# # layer1 = np.zeros((h, w, 4))
# # output = image.copy()
# # for i,j in contour:
# #     output[i,j] = [255,255,255]
# # res = layer1[:]
# # cv2.imshow('output',output)
# # cv2.waitKey(0)
# # # cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\maskT4BOX.png", res)
#
layer1 = np.zeros((h, w, 4))
# output = image.copy()
res = layer1[:]
# cv2.imshow('output',output)

part = textPart.shape[0:2]
c = max(contours, key = cv2.contourArea)
# print(c)
# print(np.where(contours ==c))
cv2.drawContours(image,contours,2, 255, -1)
cv2.imshow('part',image)
cv2.waitKey(0)
# print(contours)

#
# mask = np.zeros_like(image) # Create mask where white is what we want, black otherwise
# cv2.drawContours(mask, contours, 2, 255, -1) # Draw filled contour in mask
# out = np.zeros_like(image) # Extract out the object and place into output image
# # out[mask == 255] = image[mask == 255]
#
# # Now crop
# ind = np.where(mask == 255)
# y = ind[1]
# x = ind[0]
# (topy, topx) = (np.min(ind[1]), np.min(ind[0]))
# (bottomy, bottomx) = (np.max(y), np.max(x))
# out = out[topy:bottomy+1, topx:bottomx+1]
#
# # Show the output image
# cv2.imshow('Output', out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
