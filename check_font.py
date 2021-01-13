from fontTools.ttLib import TTFont
import os
chars_list = []
with open('hanzi.txt', 'r') as f:
    for ch in f.readlines():
        chars_list.append(ch[:-1])
#print(len(chars_list))
font_list = os.listdir('font')
for font_name in font_list:
    ttf = TTFont('font/'+font_name)
    chars_int = set()
    for table in ttf['cmap'].tables:
        for k,v in table.cmap.items():
            chars_int.add(chr(k))
    for ch in chars_list:
        if ch not in chars_int:
            print(font_name+' have not char '+ch)

