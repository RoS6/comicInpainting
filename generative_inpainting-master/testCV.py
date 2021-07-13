# import cv2
# import numpy as np
#
# image = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\005.png")
# h,w= image.shape[0:2]
# input = image.copy()
# mask = np.zeros((h,w,4))
# white_colour = (255,255,255,255)
# click_point = []
# mask_point = []
#
# def detectWord(x,y):
#     # assert image[x,y].any() != 0,"Click on the words only"
#     for i in range(x-10,x+10):
#         for j in range(y-10,y+10):
#             if image[i,j].all() <=100:
#                 mask_point.append([i,j])
#                 cv2.circle(input,(i,j),(255,255,255),-1)
#                 cv2.circle(mask, (i,j), 0, white_colour, -1)
#                 print(mask_point)
#                 detectWord(i,j)
#             elif image[i,j].all() >=100:
#                 for i,j in ([i,j],[i-1,j-1],[i-2,j-2],[i+1,j+1],[i+2,j+2]):
#                     mask_point.append([i,j])
#                     cv2.circle(input,(i,j),0,(255,255,255), -1)
#                     # cv2.circle(image, center_coordinates, radius, color, thickness)
#                     cv2.circle(mask, (i, j),0, white_colour, -1)
#                     print(mask_point)
#     print(mask_point)
# print(image)
# detectWord(456,271)
# import the necessary packages
import argparse
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
# construct the argument parser and parse the arguments
# def detectWord(x,y):
#     # assert image[x,y].any() != 0,"Click on the words only"
#     for i in range(x-10,x+10):
#         for j in range(y-10,y+10):
#             if image[i,j].all() <=100:
#                 mask_point.append([i,j])
#                 cv2.circle(input,(i,j),(255,255,255),-1)
#                 cv2.circle(mask, (i,j), 0, white_colour, -1)
#                 print(mask_point)
#                 detectWord(i,j)
#             elif image[i,j].all() >=100:
#                 for i,j in ([i,j],[i-1,j-1],[i-2,j-2],[i+1,j+1],[i+2,j+2]):
#                     mask_point.append([i,j])
#                     cv2.circle(input,(i,j),0,(255,255,255), -1)
#                     # cv2.circle(image, center_coordinates, radius, color, thickness)
#                     cv2.circle(mask, (i, j),0, white_colour, -1)
#                     print(mask_point)
#     print(mask_point)
# load the image, clone it, and setup the mouse callback function
image = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\005.png")
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
# image = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\005.png")
h,w= image.shape[0:2]
input = image.copy()
mask = np.zeros((h,w,4))
white_colour = (255,255,255,255)
# keep looping until the 'q' key is pressed
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

cv2.rectangle(layer1, refPt[0], refPt[1], (255,255,255,255), -1)

res = layer1[:]
# tempImage = image[refPt[0],refPt[1]]
tempImage = image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\tempB.png", tempImage)
cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\maskT4B.png", res)
cv2.rectangle(input, refPt[0], refPt[1], (255,255,255), -1)
cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\inputT4B.png",input)

import os
# os.system("python setting.py")
# os.system("python test.py --image examples\inputT4.png --mask examples\maskT4.png --output examples\outputT4.png --checkpoint logs/pretrain_model")

