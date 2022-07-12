from tkinter import *
from PIL import Image,ImageTk
from pygame import mixer
import os
from tkinter.filedialog import askdirectory


def play_song():
        if play_btn["text"] == "Play":
        	play_btn["text"] = "Paused"
        	play_btn.config(image=play)
        	currentsong=lstbox.get(ACTIVE)
        	mixer.music.load(currentsong)
        	songstatus.set("Playing")
        	mixer.music.play()
        else:
        	play_btn["text"] = "Play"
        	play_btn.config(image=paused)
        	mixer.music.pause()
    

#previous song
songIndex=0
def previous_song():
    global songIndex
    songIndex = (songIndex - 1 + len(songs)) % len(songs)
    mixer.music.load(songs[songIndex])
    mixer.music.play()
 
    
#next song
def next_song():
    global songIndex
    songIndex = (songIndex+1) % len(songs)
    mixer.music.load(songs[songIndex])
    songstatus.set("Paused")
    mixer.music.play()
    
app=Tk()
mixer.init()
songstatus=StringVar()
songstatus.set("choosing")
app.configure(bg='#F2D7D5')

#title
app.title("Music Player")
app.geometry("600x300")


#logo image
log= (Image.open(r"logo.png"))

resized_image= log.resize((250,250), Image.ANTIALIAS)
logo= ImageTk.PhotoImage(resized_image)

#next button image
img= (Image.open(r"next_1.png"))

resized_image= img.resize((200,200), Image.ANTIALIAS)
next= ImageTk.PhotoImage(resized_image)


#previous button image 
img2= (Image.open(r"prev_1.png"))

resized_image2= img2.resize((200,200),Image.ANTIALIAS)

prev= ImageTk.PhotoImage(resized_image2)

#paus button

img3= (Image.open(r"paused.png"))

resized_image3= img3.resize((200,200),Image.ANTIALIAS)

paused= ImageTk.PhotoImage(resized_image3)

#play button

img4= (Image.open(r"play.png"))
resized_image4= img4.resize((200,200),Image.ANTIALIAS)

play= ImageTk.PhotoImage(resized_image4)

#playsong logo
playsong=PhotoImage(file="playsong.png")
lbl=Label(app,image=playsong,bg="#F2D7D5")
lbl.place(x=50,y=400)


# app logo 
label=Label(app,image=logo,bg="#F2D7D5")
label.place(x=100,y=50)



#Music

hed=Label(app,text="MUSIC",bg="#F2D7D5")
hed.config(font=('arial',25))
hed.place(x=400,y=100)

#songlist
lstbox=Listbox(app,width=21,height=12,font=('arial',15),bg="#D7BDE2",selectmode=SINGLE)


os.chdir(r'/storage/emulated/0/')
var = StringVar()
var.set("Select the song to play")
os.chdir(askdirectory())
songs= os.listdir()
for i in songs:
	lstbox.insert(END,i)


#resume button
nxt_btn=Button(app,image=prev,text="previous",bg="#F2D7D5",command=previous_song)
nxt_btn.place(x=100,y=1700)

#paused button
prev_btn=Button(app,image=next,text="next",bg="#F2D7D5",command=next_song)
prev_btn.place(x=800,y=1700)

#playbutton
play_btn=Button(app,image=paused,text="Play",bg="#F2D7D5",command=play_song)
play_btn.place(x=450,y=1700)



lstbox.select_set(0)
app.mainloop()
