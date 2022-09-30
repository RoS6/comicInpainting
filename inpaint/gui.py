import cv2
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import os
from inpainting import click_and_crop, processImage,translate,writeText

model_path = os.getcwd()
imgdir = model_path + "/tempFolderforimageInpainting/"
# dir_path = os.path.dirname(path)
if not os.path.exists(imgdir):
    os.makedirs(imgdir)

def select_image():
    # global panelA
    path = filedialog.askopenfilename()
    print(path)
    # model_path = os.getcwd()
    # imgdir = model_path+"/tempFolderforimageInpainting/"
    # if not os.path.exists(imgdir):
    #     os.makedirs(imgdir)
    # print(imgdir)
    processImage(path,imgdir)
    # os.system("python test.py --image "+"tempFolderforimageInpainting/input.png" +" --mask "+"tempFolderforimageInpainting/mask.png" +" --output "+"tempFolderforimageInpainting/output.png" +" --checkpoint logs/pretrain_model")

    text=translate(model_path,imgdir)

    contentVar.set(text)

    # contentVar = tkinter.StringVar(root, '')

    #translate

# def selectScanLan():
#     print("Selected Option :{}".format(scanlang.get()))
#     return None
#
# def selectTarLan():
#     print("SelectedOption :{}" .format(targetlang.get()))
#     return None
#


# def translate(scanLan,tarLan):
#     import os, io
#     from google.cloud import vision
#     from google.cloud.vision_v1 import types
#     from PIL import Image, ImageDraw
#     import cv2
#     address = model_path+"cre_key.json"
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = address
#     client = vision.ImageAnnotatorClient()
#     folder_path = imgdir
#     with io.open((folder_path + 'output.png'), 'rb') as image_files:
#         content = image_files.read()
#     # refPt = [(66, 323), (236, 625)]
#
#     def fillZero(list):
#         for i in range(1, len(list)):
#             if list[i - 1] == ',' and list[i] == ',':
#                 list.insert(i, '0')
#
#
#     image = types.Image(content=content)
#     response = client.text_detection(image=image, image_context={"language_hints": ["ja"]})
#     texts = response.text_annotations
#     import pandas as pd
#     df = pd.DataFrame(columns=['locale', 'description', 'bounding', 'size'])
#     text = str(df.description.iloc[0]).replace("\n", '')
#     print(text + "finished")
#     from googletrans import Translator
#
#     translator = Translator()
#     result = translator.translate(text, dest='zh-cn')
#     print('yes')
#     result2 = translator.translate(text, dest='en')
#     print(texts)
#     print(text)
#     print(result.text)
#     print(result2.text)
#     position = ((refPt[0][0] - 10, refPt[0][1] + 20))
#
#     def changeLine(text, refpt):
#         pass
#
#     import textwrap
#     from PIL import Image, ImageDraw, ImageFont
#     lines = textwrap.wrap(result.text, width=10)
#     y_text = 0
#     firstLine = max(lines, key=lambda line: len(line))
#     W, H = (refPt[1][0] - refPt[0][0]), (refPt[1][1] - refPt[0][1])
#     outputImage = Image.open(folder_path + 'inputText3.png')
#     draw = ImageDraw.Draw(outputImage)
#     fontsize = 45
#     img_fraction = 0.50
#     font = ImageFont.truetype("arial.ttf", fontsize)
#
#     for i in lines:
#         print(i)
#         draw.text((refPt[0][0], refPt[0][1] + y_text), i, fill="black", font=font, stroke_width=7,
#                   stroke_fill=(255, 255, 255))
#         outputImage.save(folder_path + "outputwithText3.png", "PNG")
#         y_text += fontsize

def uploadText():
    cv2.destroyAllWindows()
    text = contentVar.get()
    # print(text)
    deltax = x.get()
    deltay = y.get()
    fs = fontsize.get()
    print(deltax,deltay)
    # cv2.destroyAllWindows()
    writeText(model_path, imgdir, scanlang, targetlang, text,deltax,deltay,fs)
    image = cv2.imread(imgdir + "output2.png")
    cv2.imshow('Output image',image)
    cv2.waitKey(10)


# def saveImage():
#     selection = filedialog.askdirectory()
#     path = selection +"/output.png"
def save(path):
    image = cv2.imread(imgdir+"output2.png")
    cv2.imwrite(savePath,image)
def create():
    global savePath
    # v1 = StringVar()
    # e1 = Entry(top,textvariable=v1,width=10)
    # e1.grid(row=1,column=0,padx=1,pady=1)
    savePath = StringVar(root,'0')
    sp = Entry(root,textvariable = savePath)
    selection = filedialog.askdirectory()
    print(selection)
    savePath.set(selection)
    image = cv2.imread(imgdir+"output2.png")
    print(selection + "/output.png")
    cv2.imwrite(selection+ "/output.png",image)
    cv2.destroyAllWindows()


root = Tk()
# panelA = None
# panelB = None
options_list1 = ["Chinese","English"]
options_list2 = ["Japanese"]
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
scanlang = StringVar(root)
scanlang.set("select language in the manga")

targetlang = StringVar(root)
targetlang.set("select target language of translation")

menuScan = OptionMenu(root,scanlang,*options_list2)
menuScan.pack()
menuTarg = OptionMenu(root,targetlang,*options_list1)
menuTarg.pack()

btn = Button(root, text="Select an image", command=select_image)
btn.pack()
translabel = Label(root,text = "recognised word:")
translabel.pack()
contentVar = StringVar(root,'')
contentEntry = Entry(root,textvariable= contentVar)
contentEntry.pack()
contentEntry.focus_set()

btn2 = Button(root,text="upload for translation",command=uploadText)
# kick off the GUI
btn2.pack()
xLabel = Label(root,text = "change the vertical direction of translated word:")
xLabel.pack()
x = StringVar(root,'0')
xEntry = Entry(root,textvariable= x)
xEntry.pack()
xEntry.focus_set()
# deltax = x.get()
yLabel = Label(root,text = "change the horizontal direction of translated word:")
yLabel.pack()
y = StringVar(root,'0')
yEntry = Entry(root,textvariable= y)
yEntry.pack()
yEntry.focus_set()
# deltay = y.get()
fontLabel = Label(root,text = "fontsize of text")
fontLabel.pack()
fontsize= StringVar(root,'20')
fEntry = Entry(root,textvariable= fontsize)
fEntry.pack()
fEntry.focus_set()

Button(root, text='save the image', command=create).pack()



root.mainloop()