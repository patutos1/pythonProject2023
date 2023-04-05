#Start of our programming project.
#Interface code should go here:
from tkinter import *

window = Tk()
window.title("NFL Matchup Tool")
window.configure(width=800, height=500)
window.configure(bg='white')

winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

welcome = Label(window, text="NFL Matchup Tool", background="white", foreground="white")
welcome.grid(row=0, column=winWidth/2, columnspan=10)

window.mainloop()
