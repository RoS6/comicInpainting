import cv2
import numpy as np
click_point = []
mask_point = []
refPt = []
# def mouseCallBack(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         click_point = [x,y]
#         print(click_point)
#         detectWord(click_point[0],click_point[1])
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

# def detectWord(x,y):
#     # assert image[x,y].any() != 0,"Click on the words only"
#     for i in range(x-2,x+3):
#         for j in range(y-2,y+3):
#             if image[i,j].all() >=250:
#                 mask_point.append([i,j])
#                 cv2.circle(input,(i,j),(254,254,254),-1)
#                 cv2.circle(mask, (i,j), 0, white_colour, -1)
#                 print(mask_point)
#                 detectWord(i,j)
#             elif image[i,j].all() == 0:
#                 for i,j in ([i,j],[i-1,j-1],[i-2,j-2],[i+1,j+1],[i+2,j+2]):
#                     mask_point.append([i,j])
#                     cv2.circle(input,(i,j),0,(255,255,255), -1)
#                     # cv2.circle(image, center_coordinates, radius, color, thickness)
#                     cv2.circle(mask, (i, j),0, white_colour, -1)
#                     print(mask_point)
#     print(mask_point)
# def createMask():
#     empty_mask = np.zeros((h,w,4))
#     white_colour = (255,255,255,255)
#     for i,j in

# import the necessary packages
# def detectWord(x,y):
#     # assert image[x,y].any() != 0,"Click on the words only"
#     for i in range(x-10,x+10):
#         for j in range(y-10,y+10):
#             if image[i,j].all() >=200:
#                 mask_point.append([i,j])
#                 cv2.circle(input,(i,j),(255,255,255),-1)
#                 cv2.circle(mask, (i,j), 0, white_colour, -1)
#                 print(mask_point)
#                 detectWord(i,j)
#             elif image[i,j].all() ==0:
#                 for i,j in ([i,j],[i-1,j-1],[i-2,j-2],[i+1,j+1],[i+2,j+2]):
#                     mask_point.append([i,j])
#                     cv2.circle(input,(i,j),0,(255,255,255), -1)
#                     # cv2.circle(image, center_coordinates, radius, color, thickness)
#                     cv2.circle(mask, (i, j),0, white_colour, -1)
#                     print(mask_point)

image = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\005.png")
h,w= image.shape[0:2]
input = image.copy()
mask = np.zeros((h,w,4))
white_colour = (255,255,255,255)
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_point)
while True:
    cv2.imshow("image",image)
    key = cv2.waitKey(1)
    if key == ord("c"):
        break

cv2.rectangle(mask, refPt[0], refPt[1], (255,255,255), 0)
cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\input.png",input)
cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\mask.png",mask)



