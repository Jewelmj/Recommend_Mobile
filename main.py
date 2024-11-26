import tkinter as tk
from tkinter import *
from predict import predict_1
from PIL import ImageTk, Image

root = Tk(className='Python Examples - Window Color')
root.title("Mobile Recommeding")
# image1 = Image.open("mobile.png")
root.iconbitmap("smartphone.png")
root.geometry("400x700")

input_from_user = {"Total_storage":0,
            "Back_Mpx":0,
            "Ram":0,
            "Total_storage_used":0,
            "image_storage_used":0,
            "Application_storage_used":0}
valid_dict_storage = {4:[32,64,128], 6:[64,128,256],8:[64,128,256,512],12:[128,256,512]}
valid_dict_MPX = {4:[12,32,48,64],6:[12,32,48,64,108],8:[12,32,48,64,108],12:[12,32,48,64,108]}
valid_dict_Application = {32:[" > 10 Gb","> 20 Gb"],64:[" > 20 Gb ","> 30 Gb","> 40 Gb"],128:["> 20 Gb","> 30 Gb"," > 40 Gb","> 50 Gb","> 60 Gb","> 70 Gb"],256:["> 40 Gb","> 50 Gb","> 60 Gb","> 70 Gb","> 80 Gb","> 90 Gb","> 100 Gb","> 120 Gb"],512:["> 50 Gb"," > 70 Gb"," > 80 Gb","> 100 Gb","> 120 Gb"," > 150 Gb"]}
def Ram_selected(event):
    # change the list
    Total_Storage = []
    tempof = 0
    initial = clicked.get()
    final = ""
    for letter in range(len(initial)):
        if initial[letter].isdigit():
            final = final + initial[letter]
    for i in valid_dict_storage.keys():
        if int(final) == i:
            temp = valid_dict_storage[i]
            for con in temp:
                Total_Storage.append(str(con)+" GB")
                
    global Total_Storage_clicked 
    Total_stroage_label = Label(root,text = "Total storage of mobile :",font = ("Times 20 italic bold", 10)).place(x = 70, y = 120) 
    Total_Storage_clicked = StringVar()
    Total_Storage_clicked.set(Total_Storage[0])
    drop = OptionMenu(root,Total_Storage_clicked,*Total_Storage,command=Total_storage_function).place(x = 250, y = 120) 

    input_from_user["Ram"]= int(final)
    
def Total_storage_function(event):
    # change the list
    Back_camera = []
    for i in valid_dict_MPX.keys():
        if input_from_user["Ram"] == i:
            temp = valid_dict_MPX[i]
            for con in temp:
                Back_camera.append(str(con)+" Mpx")
            
    global Back_camera_clicked
    Back_mpx_label = Label(root,text = "Back camera Mpx :",font = ("Times 20 italic bold", 10)).place(x = 70, y = 160) 
    Back_camera_clicked = StringVar()
    Back_camera_clicked.set(Back_camera[0])
    drop = OptionMenu(root,Back_camera_clicked,*Back_camera,command=Back_camera_function).place(x = 250, y = 160) 
    initial = Total_Storage_clicked.get()
    final = ""
    for letter in range(len(initial)):  
        if initial[letter].isdigit():
            final = final + initial[letter]
    input_from_user["Total_storage"] = int(final)
    # mylabel = Label(root, text=clicked.get()).pack()
def Back_camera_function(event):
    Total_storage_used = ['40%','50%','60%','70%','80%','90%','100%']
    global Total_storage_used_clicked 
    Total_storage_used_label = Label(root,text = "Total storage used :",font = ("Times 20 italic bold", 10)).place(x = 70, y = 200) 
    Total_storage_used_clicked = StringVar()
    Total_storage_used_clicked.set(Total_storage_used[0])
    drop = OptionMenu(root,Total_storage_used_clicked,*Total_storage_used,command=Total_storage_used_function).place(x = 250, y = 200) 
    initial = Back_camera_clicked.get()
    final = ""
    for letter in range(len(initial)):
        if initial[letter].isdigit():
            final = final + initial[letter]
    input_from_user["Back_Mpx"] = int(final)
def Total_storage_used_function(event):
    image_storge_used = ["< 2 GB","> 2 GB","> 3 GB","> 4 GB","> 5 GB","> 6 GB","> 7 GB"]
    global image_storge_used_clicked 
    image_storge_used_label = Label(root,text = " Total images storage :",font = ("Times 20 italic bold", 10)).place(x = 70, y = 240) 
    image_storge_used_clicked = StringVar()
    image_storge_used_clicked.set(image_storge_used[0])
    drop = OptionMenu(root,image_storge_used_clicked,*image_storge_used,command=image_storge_used_function).place(x = 250, y = 240) 
    initial = Total_storage_used_clicked.get()
    final = ""
    for letter in range(len(initial)):
        if initial[letter].isdigit():
            final = final + initial[letter]
    input_from_user["Total_storage_used"] = int(final)
def image_storge_used_function(event):
    Application_used = ["< 28 Gb"," > 28 Gb"," > 38 Gb","> 48 Gb"," > 58 GB"]
    for i in valid_dict_Application.keys():
        if input_from_user["Total_storage"] == i:
            Application_used = valid_dict_Application[i]
    global Application_used_clicked 
    Apllication_label = Label(root,text = "Total Applications storage:",font = ("Times 20 italic bold", 10)).place(x = 70, y = 280) 
    Application_used_clicked = StringVar()
    Application_used_clicked.set(Application_used[0])
    drop = OptionMenu(root,Application_used_clicked,*Application_used,command=Application_used_function).place(x = 250, y = 280) 
    initial = image_storge_used_clicked.get()
    final = ""
    for letter in range(len(initial)):
        if initial[letter].isdigit() or initial[letter] == ".":
            final = final + initial[letter]
    input_from_user["image_storage_used"] = float(final)/input_from_user["Total_storage"]*100
def Application_used_function(event):
    initial = Application_used_clicked.get()
    final = ""
    for letter in range(len(initial)):
        if initial[letter].isdigit():
            final = final + initial[letter]
    input_from_user["Application_storage_used"] = int(final)/input_from_user["Total_storage"]*100
    
    Submit_Button = Button(text="Recommend",command=main_function,width=20).place(x = 130, y = 350) 
    
def main_function():
    print(input_from_user)
    predict_1(input_from_user)

def start():
    # img = ImageTk.PhotoImage(Image.open("smartphone.png"))

    # # Create a Label Widget to display the text or Image
    # label = Label(root, image = img).place(x=10,y=50)
    # label.pack()
    photo = PhotoImage(file = "smartphone.png")
  
#    Resizing image to fit on button
    global photoimage 
    photoimage = photo.subsample(12, 12)
    label = Label(root, image = photoimage).place(x=20,y=10)
    title_label = Label(root,text="Mobile Recommendation",font = ("Times 20 italic bold", 20),bg="#898d8c").place(x=70,y= 10)
    Rame_label = Label(root,text = "Enter Ram :   ",font = ("Times 20 italic bold", 11)).place(x = 70, y = 80) 
    Ram = ["4 Gb","6 Gb","8 Gb","12 Gb",]
    global clicked 
    clicked = StringVar()
    clicked.set(Ram[0])
    drop = OptionMenu(root,clicked,*Ram,command=Ram_selected).place(x = 250, y = 80) 

start()
# 
# Mybutton = Button(root, text="set Ram",command=selected)
# Mybutton.pack()

root.mainloop() 