import pandas as pd
import tkinter as tk
from tkinter import *


    #reading the data
def filter_1(result_sep):
    df = pd.read_csv('main1.csv')
    #inititalising remporary variables for filtering.
    name_dict = {"Total_storage":'Internal storage (GB)',"Back_Mpx":'Rear camera',"Ram":'RAM (MB)'}
    user_input = result_sep
    filter_df = df          #output in this df.
    temp_df = df
    temp_range = []
    global scar
    scar = []
    i = 0
    #filtering the df
    while len(filter_df)>=2 and i <3:
        temp_range = filter_df[name_dict[list(user_input.keys())[i]]].unique()
        if list(user_input.values())[i] > max(temp_range):
            temp_df = filter_df[filter_df[name_dict[list(user_input.keys())[i]]]== max(temp_range)]
        elif list(user_input.values())[i] < min(temp_range):
            temp_df = filter_df[filter_df[name_dict[list(user_input.keys())[i]]]== min(temp_range)]
        else:
            temp_df = filter_df[filter_df[name_dict[list(user_input.keys())[i]]] == user_input[list(user_input.keys())[i]]]
        if len(temp_df) >=2:
            filter_df = temp_df
            i += 1
        else: 
            # scar.append(list(name_dict.values())[i])         #stores the sacrifices.
            # print(f'not enougth {list(name_dict.values())[i]}') 
            i+=1
        filter_df = filter_df.sort_values('Price')
        global output_1,output_2
        output_1,output_2  = filter_df.iloc[0],filter_df.iloc[-1]
        print(output_1)
        print(output_2)
        
    if len(output_1) == 0 and len(output_2) == 0 :
        out_gui(False)
    else:
        out_gui()
    #output

def out_gui(find=True):
    root = tk.Tk(className='Python Examples - Window Color')
    root.title("Mobile Recommeding")
    root.iconbitmap("mobile.png")
    root.geometry("400x700")
    root['bg'] = "#898d8c"
    if len(scar) > 0:
          sacrifice_label = Label(root,text="You have to Sacrifice "+scar+" for this mobiles",font = ("Times 20 italic bold", 15),bg="#898d8c")
          sacrifice_label.pack()
    if find:
        for items in range(1,len(output_1)):
            list_of_items = output_1.keys()
            output_1_mobile = list_of_items[items] + " : " + str(output_1[items])
            output_1_label = tk.Label(root, text = output_1_mobile,font = ("Times 20 italic bold", 15),bg="#898d8c")
            output_1_label.pack()
        line = tk.Label(root,text="_______________________________________________",font = ("Times 20 italic bold", 15),bg="#898d8c")
        line.pack()
        for items in range(1,len(output_2)):
            list_of_items = output_2.keys()
            output_2_mobile = list_of_items[items]+ " : " + str(output_2[items])
            output_2_label = tk.Label(root, text =output_2_mobile,font = ("Times 20 italic bold", 15),bg="#898d8c")
            output_2_label.pack()
    else:
        Not_found = tk.Label(root,text="Not founded in List with this specifications",font = ("Times 20 italic bold", 15),bg="#898d8c")
        Not_found.pack()
    root.mainloop()