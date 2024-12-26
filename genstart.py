from PIL import Image, ImageDraw, ImageFont, ImageTk
import random
import os
from tkinter import Tk, Label
bg = "backgrounds"
mem = "memes"
mem_txt = [
        "Я плохая — ты хороший",
        "В 20:31 прибыл Годжо Сатору",
        "Оплата у психолога не прошла",
        "Мистер Фреш",
        "Стоять, ковбой",
        "Педро-Педро-Педро",
        "Чиназес, сюда",
        "Nike Pro, ПИКМИ",
        "Бу! Испугался? Не бойся! Я друг",
        "Вы когда-нибудь мечтали стать лучшей версией себя?" 
    ]

def create_mem(bg, mem, mem_txt):
    bg_image = Image.open(os.path.join(bg,random.choice(os.listdir(bg))))
    mem_image = Image.open(os.path.join(mem,random.choice(os.listdir(mem))))

    meme_width = int(bg_image.width * 1/4)
    meme_height = int(bg_image.width * 1/4)
    mem_image = mem_image.resize((meme_width,meme_height), Image.Resampling.LANCZOS)


    x = (bg_image.width - meme_width)//2
    y = (bg_image.height - meme_height)//2

    bg_image.paste(mem_image, (x,y), mask=mem_image.convert("RGBA"))

    draw = ImageDraw.Draw(bg_image)
    font_shrift = "arial.ttf"
    font = ImageFont.truetype(font_shrift, 40)
    mem_txt = random.choice(mem_txt)
    text_bbox = draw.textbbox((0, 0), mem_txt, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    tx = (bg_image.width - text_width) // 2
    ty = bg_image.height - text_height - 20
    draw.text((tx,ty), mem_txt, font=font, fill="white")
    
    shadow_color = "black"
    text_color = "white"
    draw.text((tx + 2, ty + 2), mem_txt, font=font, fill=shadow_color)
    draw.text((tx, ty), mem_txt, font=font, fill=text_color)
    return bg_image
# ткинтер вывод
def show_mem():
    window = Tk()
    window.title("Генератор мемов")
    window.geometry("1000x1000")
    img = create_mem(bg,mem,mem_txt)
    tk_image = ImageTk.PhotoImage(img)
    label = Label(window, image = tk_image)
    label.pack()
    window.mainloop()
show_mem()