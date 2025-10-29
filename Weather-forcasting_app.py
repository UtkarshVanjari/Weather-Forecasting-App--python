from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b95ded9590ac8160beef0674938adea5").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text=data["main"]["pressure"])
    Humi_label1.config(text=data["main"]["humidity"])


win = Tk()
win.title("Zeus Weather")
win.config(bg = "skyblue")
win.geometry("900x900")

name_label = Label(win,text="Zeus Weather forecast",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=50,y=50,height=80,width=550)


city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Zeus Weather forecast",values=list_name,
                font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=50,y=150,height=80,width=550)


w_label = Label(win,text="Weather Climate",
                 font=("Time New Roman",15,"bold"))
w_label.place(x=50,y=320,height=80,width=230)
w_label1 = Label(win,text="",
                  font=("Time New Roman",15,"bold"))
w_label1.place(x=290,y=320,height=80,width=230)


wb_label = Label(win,text="Weather Description",
                  font=("Time New Roman",15,"bold"))
wb_label.place(x=50,y=420,height=80,width=230)
wb_label1 = Label(win,text="",
                   font=("Time New Roman",15,"bold"))
wb_label1.place(x=290,y=420,height=80,width=230)


temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",15,"bold"))
temp_label.place(x=50,y=520,height=80,width=230)
temp_label1 = Label(win,text="",
                   font=("Time New Roman",15,"bold"))
temp_label1.place(x=290,y=520,height=80,width=230)


pre_label = Label(win,text="Pressure",
                   font=("Time New Roman",15,"bold"))
pre_label.place(x=50,y=620,height=80,width=230)
pre_label1 = Label(win,text="",
                   font=("Time New Roman",15,"bold"))
pre_label1.place(x=290,y=620,height=80,width=230)


Humi_label = Label(win,text="Humidity",
                   font=("Time New Roman",15,"bold"))
Humi_label.place(x=50,y=720,height=80,width=230)
Humi_label1 = Label(win,text="",
                   font=("Time New Roman",15,"bold"))
Humi_label1.place(x=290,y=720,height=80,width=230)

done_button = Button(win, text="Search",
                         font=("Time New Roman", 20, "bold"),command=data_get)
done_button.place(y=250, height=50, width=100, x=270)
win.mainloop()
