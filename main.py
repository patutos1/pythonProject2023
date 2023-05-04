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

player_dict={
    "Giants":{"Wins":9,"Losses":7,"Ties":1,"Points Scored Total":365,"Points Allowed":371},
    "Buccaneers":{"Wins":8,"Losses":9,"Ties":0,"Points Scored Total":313,"Points Allowed":358},
    "49ers":{"Wins":13,"Losses":4,"Ties":0,"Points Scored Total":450,"Points Allowed":277},
    "Panthers":{"Wins":7,"Losses":10,"Ties":0,"Points Scored Total":347,"Points Allowed":374},
    "Packers":{"Wins":8,"Losses":9,"Ties":0,"Points Scored Total":370,"Points Allowed":371},
    "Rams":{"Wins":5,"Losses":12,"Ties":0,"Points Scored Total":307,"Points Allowed":384},
    "Vikings":{"Wins":13,"Losses":4,"Ties":0,"Points Scored Total":424,"Points Allowed":427},
    "Cowboys":{"Wins":12,"Losses":5,"Ties":0,"Points Scored Total":467,"Points Allowed":342},
    "Saints":{"Wins":7,"Losses":10,"Ties":0,"Points Scored Total":330,"Points Allowed":345},
    "Seahawks":{"Wins":9,"Losses":8,"Ties":0,"Points Scored Total":407,"Points Allowed":401},
    "Eagles":{"Wins":14,"Losses":3,"Ties":0,"Points Scored Total":477,"Points Allowed":344},
    "Commanders":{"Wins":8,"Losses":8,"Ties":1,"Points Scored Total":321,"Points Allowed":343},
    "Bears":{"Wins":3,"Losses":14,"Ties":0,"Points Scored Total":326,"Points Allowed":463},
    "Lions":{"Wins":9,"Losses":8,"Ties":0,"Points Scored Total":453,"Points Allowed":427},
    "Falcons":{"Wins":7,"Losses":10,"Ties":0,"Points Scored Total":365,"Points Allowed":386},
    "Cardinals":{"Wins":4,"Losses":13,"Ties":0,"Points Scored Total":340,"Points Allowed":449},
    "Steelers":{"Wins":9,"Losses":8,"Ties":0,"Points Scored Total":308,"Points Allowed":346},
    "Patriots":{"Wins":8,"Losses":9,"Ties":0,"Points Scored Total":364,"Points Allowed":347},
    "Dolphins":{"Wins":9,"Losses":8,"Ties":0,"Points Scored Total":397,"Points Allowed":399},
    "Jets":{"Wins":7,"Losses":10,"Ties":0,"Points Scored Total":296,"Points Allowed":316},
    "Colts":{"Wins":4,"Losses":12,"Ties":1,"Points Scored Total":289,"Points Allowed":427},
    "Broncos":{"Wins":5,"Losses":12,"Ties":0,"Points Scored Total":287,"Points Allowed":359},
    "Ravens":{"Wins":10,"Losses":7,"Ties":0,"Points Scored Total":350,"Points Allowed":315},
    "Raiders":{"Wins":6,"Losses":11,"Ties":0,"Points Scored Total":395,"Points Allowed":418},
    "Jaguars":{"Wins":9,"Losses":8,"Ties":0,"Points Scored Total":404,"Points Allowed":350},
    "Chargers":{"Wins":10,"Losses":7,"Ties":0,"Points Scored Total":391,"Points Allowed":384},
    "Browns":{"Wins":7,"Losses":10,"Ties":0,"Points Scored Total":361,"Points Allowed":381},
    "Chiefs":{"Wins":14,"Losses":3,"Ties":0,"Points Scored Total":496,"Points Allowed":369},
    "Bills":{"Wins":13,"Losses":3,"Ties":0,"Points Scored Total":455,"Points Allowed":286},
    "Bengals":{"Wins":12,"Losses":4,"Ties":0,"Points Scored Total":418,"Points Allowed":322},
    "Texans":{"Wins":3,"Losses":13,"Ties":1,"Points Scored Total":289,"Points Allowed":420},
    "Titans":{"Wins":7,"Losses":10,"Ties":0,"Points Scored Total":298,"Points Allowed":459},
}
print("NFL Stat Tracker\n")
print("ALL TEAMS:")
for dict in sorted(player_dict.keys()):
    print(dict)

while(1):
    flag=1
    print("\nEnter a team : ",end='')
    name=input()
    for dict in player_dict.keys():
        if(name.lower()==dict.lower()):
            print("Wins: ",end='')
            print(player_dict[dict]["Wins"])
            print("Losses: ",end='')
            print(player_dict[dict]["Losses"])
            print("Ties: ",end='')
            print(player_dict[dict]["Ties"])
            print("Points Scored Total: ",end='')
            print(player_dict[dict]["Points Scored Total"])
            print("Points Allowed: ",end='')
            print(player_dict[dict]["Points Allowed"])
            flag=0
    if flag:
        print("There is no team named ",end='')
        print(name)
        
    print("\Continue? (y) : ",end='')
    choice=input()
    if(choice=='y'):
        print("Next")
        break

while(2):
    flag=2
    print("\nEnter another team : ",end='')
    name=input()
    for dict in player_dict.keys():
        if(name.lower()==dict.lower()):
            print("Wins: ",end='')
            print(player_dict[dict]["Wins"])
            print("Losses: ",end='')
            print(player_dict[dict]["Losses"])
            print("Ties: ",end='')
            print(player_dict[dict]["Ties"])
            print("Points Scored Total: ",end='')
            print(player_dict[dict]["Points Scored Total"])
            print("Points Allowed: ",end='')
            print(player_dict[dict]["Points Allowed"])
            flag=0             
    if flag:
        print("There is no team named ",end='')
        print(name)

    print("\nContinue? (y/n) : ",end='')
    choice=input()
    if(choice=='n'):
        print("Thanks for using the NFL Team Stat Tracker!")
        break
