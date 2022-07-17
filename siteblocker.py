import datetime
from ipaddress import ip_address
import time
from tkinter import *
import validators



root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("_Website Blocker_")
root.configure(background = 'light blue')
Label(root, text =' WEBSITE BLOCKER ' , font ='arial 20 bold underline',bg="light blue",fg="brown").pack()



host_path="C:/Windows/System32/drivers/etc/hosts"
ip_address="127.0.0.1"
Label(root, text ='Enter Website :' , font ='arial 13 bold',bg = "light green",fg = "black").place(x=5 ,y=60)
Websites = Text(root,font = 'arial 10',height='4', width = '40', wrap = WORD, padx=8, pady=5)
Websites.place(x= 140,y = 60)

 
def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    v= validators.url(website_lists)
    if v== True:
        with open (host_path , 'r+') as host_file:
            file_content = host_file.read()
            for website in Website:
                if website in file_content:
                    Label(root, text = 'Already Blocked' , font = 'arial 12 bold' ,bg = "white").place(x=200,y=200)
                    pass
                else:
                    host_file.write(ip_address + " " + website + '\n')
                    Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)                   
  
block = Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command = Blocker ,width = 6,fg = "red", bg = 'white', activebackground = 'sky blue')
block.place(x = 230, y = 150)
root.mainloop()
         