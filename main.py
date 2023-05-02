#Start of our programming project.
import tkinter
from tkinter import *

#Interface code should go here:
window = Tk()
window.title("NFL Match-up Tool Demo")
window.geometry("1920x1080+50+50")
#window.configure(bg="white")

windowWidth=1920
windowHeight=1080
screenWidth=window.winfo_screenwidth()
screenHeight=window.winfo_screenheight()
#Code here allows for the window to appear in the center of the screen.
centerX= int(screenWidth/2 - windowWidth /2)
centerY= int(screenHeight/2 - windowHeight/2)
window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

label=Label(window, text="NFL Match-up Tool", font=('Arial Black bold', 48))
label.place(x=20, y=20)

label1 = tkinter.Label(window, text='Enter the name of Team 1: ', font=('Arial Black',24))
label1.place(x=20, y=100)
label2 = tkinter.Label(window, text='Enter the name of Team 2: ', font=('Arial Black',24))
label2.place(x=20, y=200)

#Here is going to be the text boxes for the player, the user will be able to
#input the name of the player they want.
canvas1 = tkinter.Canvas(window, width=300, height=200)
canvas2 = tkinter.Canvas(window, width=300, height=200)
canvas1.place(x=20, y=150)
canvas2.place(x=20, y=250)
canvas1.pack()
canvas2.pack()

entry1 = tkinter.Entry(window)
entry2 = tkinter.Entry(window)
canvas1.create_window(200, 140, window=entry1)
canvas2.create_window(200, 140, window=entry2)

#Now is the finished design of the interface with added logos of each team 

#def getPlayer():

window.mainloop() 

