import cv2
import numpy as np

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    cropping = False
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

def processImage(image_path,imgdir):
    # refPt=[]
    # cropping = False
    global image
    image = cv2.imread(image_path)
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    h, w = image.shape[0:2]
    input = image.copy()
    mask = np.zeros((h, w, 4))
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            image = clone.copy()
        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            # cv2.destroyAllWindows()
            break
        # elif key == ord('p'):
        #     import sys
        #     sys.exit()

    layer1 = np.zeros((h, w, 4))
    print(refPt)
    cv2.rectangle(layer1, refPt[0], refPt[1], (255, 255, 255, 255), -1)

    res = layer1[:] #mask image

    tempImage = image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]] #cropped temp image

    # cv2.rectangle(input, refPt[0], refPt[1], (255, 255, 255), -1) #input become input image

    cv2.imwrite(imgdir+"temp.png", tempImage)
    cv2.imwrite(imgdir+"mask.png", res)
    cv2.rectangle(input, refPt[0], refPt[1], (255,255,255), -1)
    cv2.imwrite(imgdir+"input.png",input)

# def translate

def translate(model_path,imgdir):
    import os, io
    from google.cloud import vision
    from google.cloud.vision_v1 import types
    from PIL import Image, ImageDraw
    import cv2
    model_path = model_path+'\\'
    address = model_path+"cre_key.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = address
    client = vision.ImageAnnotatorClient()
    folder_path = imgdir
    with io.open((folder_path + 'temp.png'), 'rb') as image_files:
        content = image_files.read()

    def fillZero(list):
        for i in range(1, len(list)):
            if list[i - 1] == ',' and list[i] == ',':
                list.insert(i, '0')

    image = types.Image(content=content)

    response = client.text_detection(image=image, image_context={"language_hints": ["ja"]})
    texts = response.text_annotations

    def findVertex(bounding):
        # bounding = df.bounding
        xList = []
        yList = []
        xFlag = False
        yFlag = False
        writeFlag = False
        for i in bounding:
            for j in str(i):
                if j == 'x':
                    xFlag = True
                    writeFlag = False
                    yList.append(',')
                elif j == ':':
                    # writeFlag = True
                    continue
                elif j == 'y':
                    yFlag = True
                    writeFlag = False
                    xList.append(',')
                elif j == '\n':
                    writeFlag = False
                    xFlag = False
                    yFlag = False
                elif j == ' ':
                    writeFlag = True
                    continue
                if xFlag == True and writeFlag == True:
                    xList.append(int(j))
                if yFlag == True and writeFlag == True:
                    yList.append(int(j))
        return xList, yList
    import pandas as pd
    df = pd.DataFrame(columns=['locale', 'description', 'bounding', 'size'])
    for text in texts:
        xList, yList = findVertex(text.bounding_poly.vertices)
        df = df.append(dict(
            locale=text.locale,
            description=text.description,
            bounding=text.bounding_poly.vertices,
            size=[xList, yList]
        ),
            ignore_index=True
        )
    print(df.description)
    text = str(df.description.iloc[0]).replace("\n", '')
    print(text + "finished")

    return text

    # from this on is to write text on image
def writeText(model_path,imgdir,scanLan,tarLan,text,deltax,deltay,fs):

    target = ''
    print(tarLan.get())
    if tarLan.get() == "Chinese":
        target = 'zh-cn'
    elif tarLan.get() == "English":
        target = 'en'

    from googletrans import Translator

    translator = Translator()

    result = translator.translate(text,dest=target)
    print(type(result))
    print(result)
        # .text

    # return result
    position = ((refPt[0][0] - 10, refPt[0][1] + 20))
    import textwrap
    from PIL import Image, ImageDraw, ImageFont
    lines = textwrap.wrap(result.text, width=10)
    y_text = 0
    firstLine = max(lines, key=lambda line: len(line))
    W, H = (refPt[1][0] - refPt[0][0]), (refPt[1][1] - refPt[0][1])
    outputImage = Image.open(imgdir + 'output.png')
    draw = ImageDraw.Draw(outputImage)
    fontsize = int(fs)
    img_fraction = 0.50
    font = ImageFont.truetype("arial.ttf", fontsize)

    y = refPt[0][0]+int(deltay)
    x = refPt[0][1]+int(deltax)
    for i in lines:
        print(i)
        draw.text((y, x + y_text), i, fill="black", font=font, stroke_width=7,
                  stroke_fill=(255, 255, 255))
        outputImage.save(imgdir + "output2.png", "PNG")

        y_text += fontsize
    output2 = cv2.imread(imgdir+"output2.png")
    # cv2.imshow("press any key to close the window",output2)
    # cv2.waitKey(0)


