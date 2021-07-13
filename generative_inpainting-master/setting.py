import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
address ="C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\cre_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=address
client = vision.ImageAnnotatorClient()
folder_path = "C:\\Users\\28340\\Documents\\UCL\\internship\\2ndYear\\summerResearch\\generative_inpainting-master (1)\\generative_inpainting-master\\examples\\"
with io.open((folder_path + 'temp.png'),'rb') as image_files:
    content = image_files.read()
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
print(text)
inputText = input("")
# calculateSize()
from googletrans import Translator

translator = Translator()
result = translator.translate(text,dest='zh-cn')
result2= translator.translate(text,dest='en')
print(texts)
print(text)
print(result.text)
print(result2.text)


