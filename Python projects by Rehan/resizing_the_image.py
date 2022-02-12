from tkinter import Image
import matplotlib as plt
from PIL import Image
img = Image.open("qr.png")
newimg = img.resize((180,180))
print(newimg.size)
