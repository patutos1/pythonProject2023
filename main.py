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

label=Label(window, text="NFL Match-up Tool", font=('Helvetica bold', 48))
label.place(x=20, y=20)

#Here is going to be the text boxes for the player, the user will be able to
#input the name of the player they want.
canvas1 = tkinter.Canvas(window, width=400, height=300)
canvas2 = tkinter.Canvas(window, width=400, height=300)
canvas1.pack()
canvas2.pack()

label1 = tkinter.Label(window, text='Enter the name of a Wide Receiver: ', font=('Helevetica',24))
label1.place(x=20, y=100)

entry1 = tkinter.Entry(window)
entry2 = tkinter.Entry(window)
canvas1.create_window(200, 140, window=entry1)
canvas2.create_window(200, 140, window=entry2)

#def getPlayer():


window.mainloop()
