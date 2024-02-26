# import pytesseract as ocr
# from PIL import Image
# import PIL

# ocr.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# print(ocr.image_to_string(Image.open('teste.png')))


from os import listdir
from PIL import Image
import pytesseract



pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


list =  listdir('./autoavaliacao')
text = ""
for arquivo in list:
    f = open('convert.txt', 'a', encoding='utf8' )
    f.write(pytesseract.image_to_string(Image.open(f'./autoavaliacao/{arquivo}')))

print('processo finalizado')