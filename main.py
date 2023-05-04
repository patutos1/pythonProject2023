import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

window = Tk()
window.title("NFL Matchup Tool Demo")
window.geometry("1920x1080+50+50")

windowWidth=1920
windowHeight=1080
screenWidth=window.winfo_screenwidth()
screenHeight=window.winfo_screenheight()
centerX= int(screenWidth/2 - windowWidth /2)
centerY= int(screenHeight/2 - windowHeight/2)
window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

a = ttk.Label(window, text="NFL Matchup Tool 2022", font=("Calibri", 60))
a.pack()

team1 = ttk.Label(window, text="Enter an NFL team:", font=("Calibri", 36))
team1.place(relx = 0.0, rely = 0.15, anchor ='sw')

team2 = ttk.Label(window, text="Enter another NFL team:", font=("Calibri", 36))
team2.place(relx = 0.467, rely = 0.15, anchor ='sw')

T1 = Text(window, height=3, width=42)
T1.place(relx=0.22, rely=0.15, anchor='sw')
T2 = Text(window, height=3, width=42)
T2.place(relx=0.749, rely=0.15, anchor='sw')

Enter1 = Button(window, text="Enter", height=3, width=8, command=check1())
Enter1.place(relx=0.423, rely=0.15, anchor='sw')
Enter2 = Button(window, text="Enter", height=3, width=8)
Enter2.place(relx=0.953, rely=0.15, anchor='sw')
Exit = Button(window, text="Exit Program", height=5, width=12, command=window.destroy)
Exit.place(relx=0.94, rely=0.995, anchor='sw')

window.mainloop()

def check1():
    
