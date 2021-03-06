import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from scraping import print_rasifal

def hide_frames():
  frame.pack_forget()

def frames(index,image_name):
  frame.pack(fill="both", expand=1)
  insertIamge(image_name,300,0,0)
  rasifal_display_box = Listbox(frame,height =13, width= 76,)
  rasifal_display_box.place(x=10, y=173)
  rasifal = print_rasifal(index)
  rasifal_as_list = list(rasifal)
  rasifal_name = rasifal.split(' ').pop(0)
  rasifal_initials = rasifal.split(') ').pop(0)
  splitted_character_index = len(rasifal_initials)

  rasifal_name_lable = Label(frame, text =" " + rasifal_name,
   font= ("Arial",30)).place(x=10,y=30)
  rasifal_name_lable = Label(frame, text =" " + rasifal_initials + 
    rasifal_as_list[splitted_character_index],
    font= ("Arial",11)).place(x=10,y=90)


  rasifal_list=rasifal.split("।")

  entire_sentence = rasifal.split(') ').pop(1)
  first_sentence = entire_sentence.split('।').pop(0)
  rasifal_lable = Label(rasifal_display_box, text = first_sentence +"।" ,font= ("Arial",13))
  rasifal_lable.place(x=10, y=10)
  x=10
  y=40

  for i in range (len(rasifal_list)-2):
    if i == len(rasifal_list)-2:
      rasifal_lable = Label(rasifal_display_box, text = rasifal_list[i+1] +"।" ,
        font= ("Arial",13))
    else:
      rasifal_lable = Label(rasifal_display_box, text = rasifal_list[i+1], 
        font= ("Arial",13))
    
    rasifal_lable.place(x=x, y=y)
    y+= 30
    
def on_click(index,image_name):
  frames(index,image_name)

def insertIamge(image_name,x_cord,y_cord,index):
  # Create a photoimage object of the image in the path
  image1 = Image.open(image_name)
  image1 = image1.resize((167, 165), Image.Resampling.LANCZOS)
  image = ImageTk.PhotoImage(image1)

  b = tk.Button(root, image=image, command=lambda: on_click(index,image_name))
  b.image = image

  # Position image
  b.place(x=x_cord, y=y_cord)

root = Tk()
root.title("Rasifal")
root.geometry('660x501')
root.resizable(width=0, height=0)
text = tk.Text(root, height=10)
text.configure(font=(20))

x=0 
y=0 
indx=0 
image_label = 0
images_dict={
  "0" : "mesh.png",
  "1" : "brish.png",
  "2" : "mithun.png",
  "3" : "karkat.png",
  "4" : "singha.png",
  "5" : "kanya.png",
  "6" : "tula.png",
  "7" : "brishchik.png",
  "8" : "dhanu.png",
  "9" : "makar.png",
  "10" : "khumba.png",
  "11" : "meen.png",
}

for i in range(0,3):
  for j in range(0,4):
    insertIamge(images_dict[str(image_label)],x,y,indx)
    x+= 167
    indx+= 1
    image_label+=1
  x=0
  y+= 165

frame = Frame(root, width = 501, height = 660) 
root.mainloop()