'''
TO DOS: 
MAKE THE ANSWER SUBMIT FOR FINAL QUESTION
DELETE QUESTION AFTER SUBMISSION
MAKE SUGGESTIONS PERSONAL
'''

#Imports
import tkinter as tk
from tkinter import ttk

#set up tkinter window as root
root = tk.Tk()
root.geometry("700x700")
root.configure(bg='#28282B')
scrollbar = tk.Scrollbar(root)
root.title("Software Design")

#setting up frame
frame1 = tk.Frame(root,bg="#50ad6f",width = 50)
title = tk.Label(frame1, text='Ecological Calculator',font=('Arial', 40,"bold"),fg = "white", bg="#50ad6f",width=50).pack(pady=20)
frame1.pack(pady=(40,0))
frame2 = tk.Frame(root,bg="#edede9",width=25)
frame2.pack(ipady=15)

#setting up question and labels
qList = ["How many days a week do you spend at least 30 min in vehicle with heavy carbon emissions.", "How many days a week do you eat processed and packaged foods", "How often do you throw out food waste.", "How many days a week do you use more than 90 gallons of water", "How many days a week do you fill up your trash can (approx 13 gallon)", "How many days a week do you wear clothes made by unsustainable brands"]
motto = tk.Label(frame2,
text="Answer each of the following questions with a response from 0-7, 0 being no days of the week and 7 being all days of the week",
font=('Arial',16),fg="black",width=125
).pack(pady=10)
question = ttk.Label(frame1, text = qList.pop(0))
question.pack(pady = 5, padx = 5)
scaleInt = tk.IntVar(value = 0)
slider = tk.Scale(
frame2,
variable = scaleInt,
orient= 'horizontal',
from_=0,
to=5
)
slider.pack(pady=5,padx=5)
answers = []

#function to change question after submit button pressed
def changeQ():
    question.config(text = qList.pop(0))
    if len(qList) <= 0:
        submit.pack_forget()
        finSubmit.pack(pady=5)
    answers.append(scaleInt.get())
    print(answers)

  
#set up final submit button to get total score
def finSubmit():
    total = int()
    for x in answers:
        total += x
    answer = "You're EcoScore is " + str(total)
    frame2.pack_forget()
    frame3 = tk.Frame(root,bg="#edede9")
    frame3.pack(ipady=30)
    text1 = tk.Label(frame3,text=answer,font =("Arial",30,"bold"),width=65)
    text1.pack(pady=20)
    
    # tells you what to improve based on score
    if total <= 10:
        info = tk.Label(frame3,text="0-7: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Arial",16,"italic"))
        improve1 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
        improve2 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    elif total <= 20:
        info = tk.Label(frame3,text="8-14: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Arial",16,"italic"))
        improve1 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
        improve2 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    elif total <= 30:
        info = tk.Label(frame3,text="14-21: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Arial",16,"italic"))
        improve1 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
        improve2 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    elif total <= 40:
        info = tk.Label(frame3,text="22-28: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Arial",16,"italic"))
        improve1 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
        improve2 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    elif total <= 50:
        info = tk.Label(frame3,text="29-35: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Arial",16,"italic"))
        improve1 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
        improve2 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    elif total <= 60:
        info = tk.Label(frame3,text="36-42: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Arial",16,"italic"))
        improve1 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
        improve2 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    elif total <= 70:
        info = tk.Label(frame3,text="43-49: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Arial",16,"italic"))
        improve1 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
        improve2 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    info.pack(pady=5)
    improve1.pack(pady=5)
    improve2.pack(pady=5)

#create final and regular submit buttons
finSubmit = tk.Button(frame2, text="FINISH",font=('Arial',14,"bold"),bg="#00FF00",command=finSubmit)
submit = tk.Button(frame2, text="SUBMIT",font=('Arial',14,"bold"),bg="#00FF00",command=changeQ)
submit.pack(pady = 5)

#creates loop to keep window open
root.mainloop()
