import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  

def on_click():
  print("image clicked")

def insertIamge(image_name,x_cord,y_cord):
  # Create a photoimage object of the image in the path
  image1 = Image.open(image_name)
  image1 = image1.resize((167, 220), Image.Resampling.LANCZOS)
  image = ImageTk.PhotoImage(image1)

  b = tk.Button(root, image=image, command=on_click)
  b.image = image

  # Position image
  b.place(x=x_cord, y=y_cord)

root = Tk()
root.title("Rasifal")
root.geometry('501x662')

insertIamge("test.png",0,0)
insertIamge("test.png",165,0)
insertIamge("test.png",330,0)

insertIamge("test.png",0,219)
insertIamge("test.png",165,219)
insertIamge("test.png",330,219)

insertIamge("test.png",0,438)
insertIamge("test.png",165,438)
insertIamge("test.png",330,438)

root.mainloop()