from tkinter import *
import time
import threading
import tkinter.font as font
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("System_ip", Port_no))
root = Tk()
root.title("VS Chat")
root.geometry("400x700")
root['background']='#e6ffe6'
T = Text(root,bg='#d9d9d9',bd=3,font=4)
l = Label(root, text = "VS Chating App",bg='#e6ffe6')
myFont2 = font.Font(size=15,weight='bold')
l['font'] = myFont2
l.pack()
T.pack()
s1=Entry(root,width = 42)
s1['font'] = myFont2
s1.pack()
def sws(event):
    mychat=s1.get()
    T.insert(END, "\n you-->"+mychat)
    s1.delete(-1,'end')
    s2=bytes(mychat, 'utf-8')
    s.send(s2)
def sws1():
    mychat=s1.get()
    T.insert(END, "\n you-->"+mychat)
    s1.delete(-1,'end')
    s2=bytes(mychat, 'utf-8')
    s.send(s2)
b1 = Button(root, text = "Chating",command=sws1,width=15)
b2 = Button(root, text = "Exit",command = root.destroy,width=15)
b1['font'] = myFont2
b2['font'] = myFont2
b1.pack()
b2.pack()
root.bind('<Return>', sws)
other="VS CHATING"

def rec():
    while True:
        other=s.recv(1024)
        T.insert(END, "\n client-->"+str(other.decode()))
    #         ms=s.recv(1024)
    #         Fact = "sagar -->"+str(ms.decode())
    #         T.insert(tk.END, Fact)
threading.Thread(target=rec).start()
mainloop()
