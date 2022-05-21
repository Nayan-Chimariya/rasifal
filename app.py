import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from scraping import print_rasifal

def on_click(index):
  print_rasifal(index)

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

x=0 
y=0 
indx=0 

for i in range(0,4):
  for j in range(0,3):
    insertIamge("test.png",x,y,indx)
    x+= 167
    indx+= 1
  x=0
  y+= 165
   
root.mainloop()