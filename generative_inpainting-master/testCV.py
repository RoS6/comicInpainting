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

# load the image, clone it, and setup the mouse callback function
image = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\003.png")
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

# cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpaint-master\\examples\\maskT2.png", res)
cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\maskT3.png", res)
# C:\Users\28340\Documents\UCL\internship\2ndYear\summerResearch\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\005.png
# cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\mask.png",mask)
# mask = cv2.imread("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\mask.png")
# cv2.rectangle(mask, refPt[0], refPt[1], (0,0,0), -1)
cv2.rectangle(input, refPt[0], refPt[1], (255,255,255), -1)
# cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpaint-master\\examples\\inputT2.png",input)
cv2.imwrite("C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\inputT3.png",input)

import os
os.system("python test.py --image examples\inputT2.png --mask examples\maskT2.png --output examples\outputT2.png --checkpoint logs/pretrain_model")


# import numpy as np
# import tensorflow as tf
# import neuralgym as ng
#
# from inpaint_model import InpaintCAModel
#
#
# parser = argparse.ArgumentParser()
# parser.add_argument('--image', default='', type=str,
#                     help='The filename of image to be completed.')
# parser.add_argument('--mask', default='', type=str,
#                     help='The filename of mask, value 255 indicates mask.')
# parser.add_argument('--output', default='output.png', type=str,
#                     help='Where to write output.')
# parser.add_argument('--checkpoint_dir', default='', type=str,
#                     help='The directory of tensorflow checkpoint.')
#
#
# if __name__ == "__main__":
#     FLAGS = ng.Config('inpaint.yml')
#     # ng.get_gpus(1)
#     args, unknown = parser.parse_known_args()
#
#     model = InpaintCAModel()
#     image = cv2.imread(args.image)
#     mask = cv2.imread(args.mask)
#     # mask = cv2.resize(mask, (0,0), fx=0.5, fy=0.5)
#
#     assert image.shape == mask.shape
#
#     h, w, _ = image.shape
#     grid = 8
#     image = image[:h//grid*grid, :w//grid*grid, :]
#     mask = mask[:h//grid*grid, :w//grid*grid, :]
#     print('Shape of image: {}'.format(image.shape))
#
#     image = np.expand_dims(image, 0)
#     mask = np.expand_dims(mask, 0)
#     input_image = np.concatenate([image, mask], axis=2)
#
#     sess_config = tf.ConfigProto()
#     sess_config.gpu_options.allow_growth = True
#     with tf.Session(config=sess_config) as sess:
#         input_image = tf.constant(input_image, dtype=tf.float32)
#         output = model.build_server_graph(FLAGS, input_image)
#         output = (output + 1.) * 127.5
#         output = tf.reverse(output, [-1])
#         output = tf.saturate_cast(output, tf.uint8)
#         # load pretrained model
#         vars_list = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)
#         assign_ops = []
#         for var in vars_list:
#             vname = var.name
#             from_name = vname
#             var_value = tf.contrib.framework.load_variable(args.checkpoint_dir, from_name)
#             assign_ops.append(tf.assign(var, var_value))
#         sess.run(assign_ops)
#         print('Model loaded.')
#         result = sess.run(output)
#         cv2.imwrite(args.output, result[0][:, :, ::-1])


# python test.py --image examples\inputT.png --mask examples\maskT.png --output examples\outputT.png --checkpoint logs/pretrain_model
