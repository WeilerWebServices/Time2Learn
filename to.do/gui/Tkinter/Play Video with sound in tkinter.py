#!python3

# Play Video with sound in tkinter

import os

from tkinter import *

app = TK()
app.title('Video Player')

Fcanvas = bg="black, height = 600, width = 600"


def snd1():
    os.system("D:\github\wws\Time-To-Learn\Pic-Video-Audio\abc\ABC-Phonics-Song-with-Sounds.mp4")

def snd2():
    os.system("D:\github\wws\Time-To-Learn\Pic-Video-Audio\abc\Phonics-Song.mp4")

#def snd3():
#    os.system("D:\github\wws\Time-To-Learn\Pic-Video-Audio\abc\ABC-Phonics-Song-with-Sounds.mp4")

var = IntVar()

rb1 =Radiobutton(app, text= "Play Video One", variable =var, value=1,command=snd1)
rb1.pack(anchor =W)

rb2 =Radiobutton(app, text= "Play Video Two", variable =var, value=2,command=snd1)
rb2.pack(anchor =W)

rb3 =Radiobutton(app, text= "Play Video Three", variable =var, value=3,command=snd1)
rb3.pack(anchor =W)

Fcanvas.pack()

app.mainloop()
