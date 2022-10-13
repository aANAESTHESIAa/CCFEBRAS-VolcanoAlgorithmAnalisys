#  Copyright (c) 2021. Anastasia Dutchina.
#  All rights reserved.

from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import easygui

input_file_png = easygui.fileopenbox(msg="Выберите исследуемое избражение с разметкой алгоритма",
                                     filetypes=["*.png"])
input_file_jpg = input_file_png.rpartition('.')[0] + ".jpg"
print(input_file_jpg)


def get_mouse_position(event):
    global firstPointY, firstPointX
    firstPointX, firstPointY = event.x, event.y


def update_sel_rect(event):
    global rect_id
    global firstPointY, firstPointX, secondPointX, secondPointY
    global cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower
    secondPointX, secondPointY = event.x, event.y
    canvas.coords(rect_id, firstPointX, firstPointY, secondPointX, secondPointY)  # Update selection rect.
    if firstPointX < secondPointX:  # selection direction check
        if firstPointY < secondPointY:
            cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = firstPointX, firstPointY, secondPointX, secondPointY
        else:
            cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = firstPointX, secondPointY, secondPointX, firstPointY
    elif firstPointX > secondPointX:
        if firstPointY < secondPointY:
            cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = secondPointX, firstPointY, firstPointX, secondPointY
        else:
            cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = secondPointX, secondPointY, firstPointX, firstPointY


cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = 0, 0, 0, 0
firstPointX, firstPointY, secondPointX, secondPointY = 0, 0, 0, 0
rect_id = None
WINDOWWIDTH, WINDOWHEIGHT = 900, 900
window = tk.Tk()
window.title("Select Area")
window.geometry('%sx%s' % (WINDOWWIDTH, WINDOWHEIGHT))
window.configure(background='grey')
img = ImageTk.PhotoImage(Image.open(input_file_png))
canvas = tk.Canvas(window, width=img.width(), height=img.height(),
                   borderwidth=0, highlightthickness=0)
canvas.pack(expand=True)
canvas.img = img
canvas.create_image(0, 0, image=img, anchor=tk.NW)
rect_id = canvas.create_rectangle(firstPointX, firstPointY, firstPointX, firstPointY,
                                  dash=(2, 2), fill='', outline='white')

canvas.bind('<Button-1>', get_mouse_position)
canvas.bind('<B1-Motion>', update_sel_rect)
window.mainloop()


def cut_image(inputJpg, inputPng):
    jpg = Image.open(inputJpg)
    png = Image.open(inputPng)
    png.crop((cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower)).save('png_crop.png', "PNG")
    jpg.crop((cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower)).save('jpg_crop.jpg', "JPEG")


cut_image(input_file_jpg, input_file_png)

preAlgImage = Image.open('jpg_crop.jpg')  # Открываем изображение без выделения алгоритмом
draw = ImageDraw.Draw(preAlgImage)  # Создаем инструмент для рисования
width = preAlgImage.size[0]  # Определяем ширину
height = preAlgImage.size[1]  # Определяем высоту
pix = preAlgImage.load()  # Выгружаем значения пикселей

postAlgImage = Image.open('png_crop.png')  # Открываем изображение, обработанное алгоритмом
postAlgPixVals = list(postAlgImage.getdata())

canvasWidth = width * 20
canvasHeight = height * 20
im = Image.new('RGB', (canvasWidth, canvasHeight), 'white')
data = list(preAlgImage.getdata())
dx = 0
dy = 0
counter = 0
for y in range(height):  # перебор пикселей
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
im.save((input_file_png.rpartition('.')[0]).rpartition('\\')[0] + '\\results\\' +
        (input_file_png.rpartition('.')[0]).rpartition('\\')[2] + "_result.png", "PNG")
im.show()

