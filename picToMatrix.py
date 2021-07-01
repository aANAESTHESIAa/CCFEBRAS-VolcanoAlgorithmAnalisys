from PIL import Image, ImageDraw, ImageFont

import easygui
import subprocess

input_file_jpg = easygui.fileopenbox(msg="Выберите исходное изображение", filetypes=["*.jpg"])
input_file_png = easygui.fileopenbox(msg="Выберите изображение с разметкой алгоритма", filetypes=["*.png"])
print(input_file_jpg)


cmd = "C:/Windows/System32/mspaint.exe "+str(input_file_png)
print("cmd")
print(cmd)
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)
process.wait()
#запуск paint для определения пользователем начальной координаты рамки обрезания файла
def autocut(inputJpg, inputPng):   #обрезка изображений
    jpg = Image.open(inputJpg)
    png = Image.open(inputPng)
    answer = 0
    startCutX = 0
    startCutY = 0
    endCutX = 0
    endCutY = 0
    startCutX = int(input("Введите значение координаты Х верхнего левого пикселя для рамки обрезания изображения"))
    startCutY = int(input("Введите значение координаты Y верхнего левого пикселя для рамки обрезания изображения"))
    print("Каков наклон выделения аномалии? ")
    print("1 - Эллипс наклонен горизонтально -")
    print("2 - Эллипс наклонен вертикально | ")
    print("3 - Эллипс наклонен диагонально (квадратная область выделения)")
    print("4 - Задать правый нижний пиксель рамки обрезки вручную ")
    answer = str(input())
    if answer == "1":
        endCutX = startCutX + 50
        endCutY = startCutY + 30
    elif answer == "2":
        endCutX = startCutX + 30
        endCutY = startCutY + 50
    elif answer == "3":
        endCutX = startCutX + 50
        endCutY = startCutY + 50
    elif answer == "4":
        endCutX = input("Введите значение координаты Х нижнего правого пикселя для рамки обрезания изображения")
        endCutY = input("Введите значение координаты Y нижнего правого пикселя для рамки обрезания изображения")
    else:
        print("Вы ввели некорректное значение")
        exit(-1)
    png.crop((startCutX, startCutY, endCutX, endCutY)).save('png_crop.png', "PNG")
    jpg.crop((startCutX, startCutY, endCutX, endCutY)).save('jpg_crop.jpg', "JPEG")


autocut(input_file_jpg, input_file_png)

preAlgImage = Image.open('jpg_crop.jpg')  # Открываем изображение без выделения алгоритмом
draw = ImageDraw.Draw(preAlgImage)  # Создаем инструмент для рисования
width = preAlgImage.size[0]  # Определяем ширину
height = preAlgImage.size[1]  # Определяем высоту
pix = preAlgImage.load()  # Выгружаем значения пикселей

postAlgImage = Image.open('png_crop.png')  # Открываем изображение, обработанное алгоритмом
postAlgPixVals = list(postAlgImage.getdata())

newWidth = width * 20
newHeight = height * 20
im = Image.new('RGB', (newWidth, newHeight), 'white')
data = list(preAlgImage.getdata())
dx = 0
dy = 0
counter = 0
for y in range(height):
    for x in range(width):
        draw.rectangle((dx, dy, dx + 20, dy + 20), fill=data[counter])
        font = ImageFont.truetype("arial.ttf", 10)
        fillage = str(data[counter])
        if postAlgPixVals[counter][0] - postAlgPixVals[counter][1] > 10:
            draw.text((dx + 1, dy + 5), fillage[1:4], 'green', font=font)
        else:
            draw.text((dx + 1, dy + 5), fillage[1:4], 'red', font=font)
        draw = ImageDraw.Draw(im)
        dx = dx + 20
        counter = counter + 1
    dy = dy + 20
    dx = 0
draw.rectangle((0, 0, 19, 19), fill=data[0])
draw.text((1, 5), str(data[0])[1:4], 'red', font=font)
draw = ImageDraw.Draw(im)

im.save("result.png", "PNG")
im.show()



