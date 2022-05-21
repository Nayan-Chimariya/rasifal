import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from scraping import print_rasifal

def on_click(index):
  print_rasifal(index)
  print("image clicled")

def insertIamge(image_name,x_cord,y_cord,index):
  # Create a photoimage object of the image in the path
  image1 = Image.open(image_name)
  image1 = image1.resize((167, 165), Image.Resampling.LANCZOS)
  image = ImageTk.PhotoImage(image1)

  b = tk.Button(root, image=image, command=lambda: on_click(index))
  b.image = image

  # Position image
  b.place(x=x_cord, y=y_cord)

root = Tk()
root.title("Rasifal")
root.geometry('501x660')

insertIamge("test.png",0,0,0)
insertIamge("test.png",167,0,1)
insertIamge("test.png",334,0,2)

insertIamge("test.png",0,165,3)
insertIamge("test.png",167,165,4)
insertIamge("test.png",334,165,5)

insertIamge("test.png",0,330,6)
insertIamge("test.png",167,330,7)
insertIamge("test.png",334,330,8)

insertIamge("test.png",0,495,9)
insertIamge("test.png",167,495,10)
insertIamge("test.png",334,495,11)

root.mainloop()