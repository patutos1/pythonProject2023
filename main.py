#Start of our programming project.
from tkinter import *

#Interface code should go here:
window = Tk()
window.title("NFL Match-up Tool Demo")
window.geometry("800x500+50+50")
window.configure(bg="white")

windowWidth=800
windowHeight=500
screenWidth=window.winfo_screenwidth()
screenHeight=window.winfo_screenheight()
#Code here allows for the window to appear in the center of the screen.
centerX= int(screenWidth/2 - windowWidth /2)
centerY= int(screenHeight/2 - windowHeight/2)
window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

label=Label(window, text="NFL Match-up Tool", bg='white', font=('Helvetica bold', 48))
label.place(x=20, y=20)

window.mainloop()
