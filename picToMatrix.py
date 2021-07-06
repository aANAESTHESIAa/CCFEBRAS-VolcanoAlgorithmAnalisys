#  Copyright (c) 2021. Anastasia Dutchina.
#  All rights reserved.

from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import easygui


input_file_png = easygui.fileopenbox(msg="Выберите исследуемое избражение с разметкой алгоритма", filetypes=["*.png"])
input_file_jpg = input_file_png.rpartition('.')[0]+".jpg"


def get_mouse_posn(event):
    global topy, topx
    topx, topy = event.x, event.y


def update_sel_rect(event):
    global rect_id
    global topy, topx, botx, boty
    global selectedtopx, selectedtopy, selectedbotx, selectedboty
    botx, boty = event.x, event.y
    canvas.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.
    selectedtopx, selectedtopy, selectedbotx, selectedboty = topx, topy, botx, boty
    print(selectedtopx, selectedtopy, selectedbotx, selectedboty)


selectedtopx, selectedtopy, selectedbotx, selectedboty = 0, 0, 0, 0
topx, topy, botx, boty = 0, 0, 0, 0
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
canvas.img = img  # Keep reference in case this code is put into a function.
canvas.create_image(0, 0, image=img, anchor=tk.NW)
rect_id = canvas.create_rectangle(topx, topy, topx, topy,
                                  dash=(2, 2), fill='', outline='white')

canvas.bind('<Button-1>', get_mouse_posn)
canvas.bind('<B1-Motion>', update_sel_rect)
window.mainloop()


def autocut(inputJpg, inputPng):   #обрезка изображений
    jpg = Image.open(inputJpg)
    png = Image.open(inputPng)
    png.crop((selectedtopx, selectedtopy, selectedbotx, selectedboty)).save('png_crop.png', "PNG")
    jpg.crop((selectedtopx, selectedtopy, selectedbotx, selectedboty)).save('jpg_crop.jpg', "JPEG")


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



