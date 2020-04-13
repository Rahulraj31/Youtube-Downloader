from tkinter import *
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *

from functools import partial

root = Tk()
root.geometry('950x370')
root.title("RRP Downloader")
root.configure(bg='white')


def downloadytv():
    url = linkEnter.get()
    destination = askdirectory()

    ob = YouTube(url)
    strm = ob.streams.first()
    strm.download(destination)
    showinfo("Downloading Finished","Downloaded Sucessfully")


#setting up heading icon
file=PhotoImage(file="images.png")
icon=Label(root,image=file,justify=CENTER)
icon.pack(side=TOP,pady=10)



Label(root, text="===========SASTA YOUTUBE DOWNLOADER========", font=('georgia',20),bg='white').pack(padx=10)




#Setting up the icon
photo = PhotoImage(file = "download.png")
root.iconphoto(FALSE, photo)




Label(root, text="Enter Link Here", font=75, bg='white').pack(pady=5)

link = StringVar()

linkEnter = Entry(root,textvariable=link, font=("verdana",15),justify=CENTER,width=300 ,bg='white')
linkEnter.pack(fill=X,padx=30)

bt = Button(root, text="Download", font=('comic sans mc',15),relief=RAISED,command=downloadytv).pack(fill=X,padx=400,pady=8)  # relief property of button

Label(root, text="Made by RRP", font=("georgia",13,) , bg='white').pack(pady=8)

root.mainloop()
