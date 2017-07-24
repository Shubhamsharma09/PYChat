import socket
import time
import tkinter
import threading
from tkinter import *

name='shubham'
host='127.0.0.1'
port=9998


cli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def rece():
  cl.config(state=NORMAL)
  cli.connect((host,port))
  print("connected")
  cl.insert(INSERT,"connected to admin\n")
  cl.config(state=DISABLED)
  while True:
   try:
      data=cli.recv(1024)
      cl.config(state=NORMAL)
      if not data:
          cl.insert(INSERT,"Admin has disconnected\n")
          break
      s=data.decode('utf-8')
      s = "Admin-->" + s + "\n"
      print(s)
      #cl.tag_add("start", "1.0", "1.8")
      #cl.tag_config("start", background="black", foreground="green")
      c=cl.index(INSERT)
      cl.insert(INSERT,s )
      c=float(c)
      cl.tag_add("start",c,c+0.8)
      cl.tag_config("start", background="black", foreground="green")

      cl.config(state=DISABLED)
   except:
       cl.config(state=NORMAL)
       cl.insert(INSERT, "Admin has been disconnected\n")
       cl.insert(INSERT, "Waiting for admin to restart server .......\n")
       cl.config(state=DISABLED)


  cli.close()

def send():
   s=EntryBox.get()
   a=s
   if(len(s)!=0):
       a="User-->"+a+"\n"
       cl.config(state=NORMAL)
       c = cl.index(INSERT)
       cl.insert(INSERT, a)
       c=float(c)
       cl.tag_add("st", c, c + 0.7)
       cl.tag_config("st", background="yellow", foreground="blue")
       cl.config(state=DISABLED)
       cli.sendall(s.encode('utf-8'))
       EntryBox.delete(0,END)




scr= Tk()
scr.title('User')
scr.geometry("400x500")
scr.resizable(width=FALSE, height=FALSE)


cl = Text(scr, bd=0, bg="white", height="8", width="50", font="Arial",)
cl.insert(END, "Connecting to your partner..\n")
cl.config(state=DISABLED)


scrollbar = Scrollbar(scr, command=cl.yview, cursor="heart")
cl['yscrollcommand'] = scrollbar.set

SendButton = Button(scr, font=30, text="Send", width="12", height=5,
                    bd=0, bg="orange", activebackground="red", command=send)


EntryBox = Entry(scr, bd=0, bg="white",width="29",  font="Arial")
#EntryBox.bind("<Return>", DisableEntry)
#EntryBox.bind("<KeyRelease-Return>", PressAction)

#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
cl.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
threading._start_new_thread(rece,())

scr.mainloop()