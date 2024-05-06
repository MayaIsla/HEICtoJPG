#pip install wand

from wand.image import Image
import os

SourceFolder = "D:/Downloads/Pics/More final pics"
TargetFolder = "D:/Downloads/test2"


for file in os.listdir(SourceFolder):
    SourceFile = SourceFolder + "/" + file
    TargetFile = TargetFolder + "/" + file.replace(".HEIC", ".jpg")

    img = Image(filename=SourceFile)
    img.format = 'HEIC'
    img.save(filename=TargetFile)
    img.close()