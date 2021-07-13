import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import cv2
address ="C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\cre_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=address
client = vision.ImageAnnotatorClient()
folder_path = "C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\"
with io.open((folder_path + 'tempText.png'),'rb') as image_files:
    content = image_files.read()
refPt = [(508, 465), (578, 605)]
def fillZero(list):
    for i in range(1,len(list)):
        if list[i-1] == ',' and list[i] == ',':
            list.insert(i,'0')
# def calculateSize(bounding):
#
def findVertex(bounding):
    # bounding = df.bounding
    xList = []
    yList = []
    xFlag = False
    yFlag = False
    writeFlag = False
    for i in bounding:
        for j in str(i):

            # print(str(j))
            # print(type(j))
            # for j in str(i):
            # j = j.replace('\n','')
            if j == 'x':
                xFlag = True
                writeFlag = False
                yList.append(',')
            elif j==':':
                # writeFlag = True
                continue
            elif j == 'y':
                yFlag = True
                writeFlag = False
                xList.append(',')
            elif j =='\n':
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
            # if writeFlag ==False:

    # print(xList)
    # print(yList)
    # xList = fillZero(xList)
    # yList = fillZero(yList)
    return xList,yList

image = types.Image(content = content)
response = client.text_detection(image = image, image_context={"language_hints": ["ja"]})
texts = response.text_annotations
import pandas as pd
df = pd.DataFrame(columns = ['locale','description','bounding','size'])
for text in texts:
    # print(type(text))
    # print(type(text.bounding_poly.vertices))
    # print(text.bounding_poly.vertices)
    # print(text.bounding_poly.vertices[0])
    # print(type(text.bounding_poly.vertices[0]))
    # print(type(str(text.bounding_poly.vertices[0])))
    # print(str(text.bounding_poly.vertices[0])[0:4])
    xList,yList = findVertex(text.bounding_poly.vertices)
    df = df.append(dict(
        locale = text.locale,
        description = text.description,
        bounding = text.bounding_poly.vertices,
        size = [xList,yList]
    ),
        ignore_index = True
    )
    # calculateSize(text.bounding_poly.vertices)
    # print(text.bounding_poly.vertices)

# print(df)
# print(texts)

# print(df.description.iloc[0])
text =str(df.description.iloc[0]).replace("\n",'')
print(text+"finished")
# inputText = input("")
# calculateSize()
from googletrans import Translator

translator = Translator()
result = translator.translate(text,dest='zh-cn')
print('yes')
result2= translator.translate(text,dest='en')
print(texts)
print(text)
print(result.text)
print(result2.text)

#find font and size
# from PIL import ImageFont, ImageDraw, Image
#
# def find_font_size(text, font, image, target_width_ratio):
#     tested_font_size = 100
#     tested_font = ImageFont.truetype(font, tested_font_size)
#     observed_width, observed_height = get_text_size(text, image, tested_font)
#     estimated_font_size = tested_font_size / (observed_width / image.width) * target_width_ratio
#     return round(estimated_font_size)
#
# def get_text_size(text, image, font):
#     im = Image.new('RGB', (image.width, image.height))
#     draw = ImageDraw.Draw(im)
#     return draw.textsize(text, font)
#
# width_ratio = 0.5
# font_family = "heiti.ttf"
# # text = "Hello World"
#
# image = Image.open('pp.png')
# editable_image = ImageDraw.Draw(image)
# font_size = find_font_size(text, font_family, image, width_ratio)
# font = ImageFont.truetype(font_family, font_size)
#
# print(f"Font size found = {font_size} - Target ratio = {width_ratio} - Measured ratio = {get_text_size(text, image, font)[0] / image.width}")
position = ((refPt[0][0]-10,refPt[0][1]+20))
outputImage = cv2.imread(folder_path+'inputText.png')
while True:
    # fontsize = int(input("font size of text:"))
    cv2.putText(
         outputImage, #numpy array on which text is written
         result2.text, #text
         position, #position at which writing has to start
         cv2.FONT_HERSHEY_TRIPLEX, #font family
         0.7, #font size
         (0,0,0,255), #font color
         1) #font stroke
    # cv2.imwrite('outputText.png', outputImage)
    cv2.imshow('outputText',outputImage)
    cv2.waitKey(0)