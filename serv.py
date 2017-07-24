import tkinter as tk
import socket
import threading
from tkinter import *

from PIL import Image,ImageTk
import time

host = '127.0.0.1'
port = 9998



sr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sr.bind((host, port))
    print("binded")
    sr.listen(1)
except socket.error as e:
    print(str(e))


def client():
    #conn.send(str.encode("welcome,type your info....."))
    a.config(state=NORMAL)
    global conn
    conn, addr = sr.accept()
    print("connected")
    #a.insert(INSERT,"connected\n")
    a.insert('1.0', "connected to: {0} , {1} \n".format(addr[0],addr[1]))
    a.config(state=DISABLED)
    while True:
     try:
        data = conn.recv(1024)
        a.config(state=NORMAL)
        # reply="server output:" + data.decode('utf-8')
        if not data:
            a.insert(INSERT,"user has left...\n")
            break

        s= data.decode('utf-8')
        s="User-->"+s+"\n"
        print(s+"\n")
        #a.tag_add("here", "1.0", "1.7")
        #a.tag_config("here", background="yellow", foreground="blue")
        #a.delete(1.0, END)
        #a.index('1.0')
        c=a.index(INSERT)
        a.insert(INSERT,s)
        c=float(c)
        a.tag_add("here",c , c+0.7 )
        a.tag_config("here", background="yellow", foreground="blue")
        a.config(state=DISABLED)

     except:
        a.config(state=NORMAL)
        a.insert(INSERT , "User has been disconnected\n")
        a.insert(INSERT, "Waiting for user to join in .......\n")
        a.config(state=DISABLED)
    conn.close()

def send():
   global conn
   s=EntryBox.get()
   a1=s
   if(len(s)!=0):
       a1="Admin-->"+a1+"\n"
       a.config(state=NORMAL)
       c = a.index(INSERT)
       a.insert(INSERT, a1)
       c=float(c)
       a.tag_add("he", c, c + 0.8)
       a.tag_config("he", background="black", foreground="green")
       a.config(state=DISABLED)
       conn.sendall(s.encode('utf-8'))
       EntryBox.delete(0,END)








scr=Tk()
img = Image.open("/home/shubhi/Downloads/chatbg.jpg")
photoImg = ImageTk.PhotoImage(img)
scr.wm_title("Admin")
scr.geometry("400x500")
#scr.wm_maxsize(width=300 ,height=300)
#scr.wm_minsize(width=250 , height=250)
a=tk.Text(scr,fg='green')
a.insert(INSERT , "waiting for a connection........\n")
a.config(state=DISABLED)
scr.resizable(width=False, height=False)


scrollbar = Scrollbar(scr, command=a.yview, cursor="heart")
a['yscrollcommand'] = scrollbar.set

#Create the Button to send message
SendButton = Button(scr, font=30, text="Send", width="12", height=5,
                    bd=0, bg="blue", activebackground="lightblue",command=send
                    )

#Create the box to enter message
EntryBox = Entry(scr, bd=0, bg="white",width="29", font="Arial")
scrollbar.place(x=376,y=6, height=386)
a.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
a.image_create(INSERT,image=photoImg)


threading._start_new_thread(client,())










scr.mainloop()





