#Team 21732
#Imports
import tkinter as tk
from tkinter import ttk

#set up tkinter window as root
root = tk.Tk()
root.geometry("700x700")
root.configure(bg='#91c7a3')
scrollbar = tk.Scrollbar(root)
root.title("Software Design: Team #21732")

#setting up frame
frame1 = tk.Frame(root,bg="#50ad6f",width = 50)
title = tk.Label(frame1, text='Ecological Calculator',font=('Arial', 40,"bold"),fg = "white", bg="#50ad6f",width=50).pack(pady=20)
frame1.pack(pady=(40,0))
frame2 = tk.Frame(root,bg="#edede9",width=25)
frame2.pack(ipady=15)

#setting up question and labels
qList = ["How many days a week do you spend at least 30 min in vehicle with heavy carbon emissions.", "How many days a week do you eat processed and packaged foods", "How many days a week do you throw out food waste.", "How many days a week do you use more than 90 gallons of water", "How many days a week do you fill up your trash can (approx 13 gallon)", "How many days a week do you wear clothes made by unsustainable brands"]
motto = tk.Label(frame2,
text="Answer each of the following questions with a response from 0-7, 0 being no days of the week and 7 being all days of the week",
font=('Arial',16),fg="black",width=125
).pack(pady=10)
question = ttk.Label(frame2, text = qList.pop(0), font=("Arial",20))
question.pack(pady = 5, padx = 5)
scaleInt = tk.IntVar(value = 0)
slider = tk.Scale(
frame2,
variable = scaleInt,
orient= 'horizontal',
from_=0,
to=7
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
    answers.append(scaleInt.get())
    total = int()
    for x in answers:
        total += x
    answer = "You're EcoScore is..." + str(round((42-total)*(100/42)))
    frame2.pack_forget()
    frame3 = tk.Frame(root,bg="#edede9")
    frame3.pack(ipady=30)
    text1 = tk.Label(frame3,text=answer,font =("Arial",30,"bold"),width=65)
    text1.pack(pady=20)
    if total <= 14:
        line = tk.Label(frame3,text="-----------------------------------------------------------------------------------------------------------",bg="#edede9").pack()
        improve1 = tk.Label(frame3,text="LEGENDARY! You're successfully doing your job and limiting your \nlifestyle's impact on the environment through a \nvariety of practices whether that be by limiting travel \nin vehicels with heavy carbon emissions, buying\n clothes from sustainable brands, and/or limiting water use.", font=("Arial",18,"italic"),bg="#edede9").pack()
        improve2 = tk.Label(frame3,text="As you have performed well on your own, it is now your\n job to serve as a leader for others. Encourage \nthem to continue or start implementing sustainable \npractices in their day to day lives. If they don't know \nwhere to start show them your own approaches. When\n we work together the better we'll be able to maintain our planet.", font=("Arial",18,"italic"),bg="#edede9").pack()
    elif total <= 28:
        improve1 = tk.Label(frame3,text="GREAT. You're on the right track to limiting your lifestyles \nimpact on the environment. While for most/all of \nthe tested behaviors, you spend most of the week practicing \nsustainable methods, there are still a few days to which\nyou should plan on working towards maintaining \nthe sustainable lifestyle.", font=("Arial",18,"italic"),bg="#edede9").pack()
        improve2 = tk.Label(frame3,text="You can look into many different areas for improvement \nsuch as limiting your time/usage of vehicles with \nheavy carbon emissions, limiting water use, and \nlimiting waste thrown away. As you are an upcoming \nleader in your community, it is important that you invite \nyour family and friends to start practicing sustainable \nmethods too.", font=("Arial",18,"italic"),bg="#edede9").pack()
    elif total <= 42:
        improve1 = tk.Label(frame3,text="POOR. You have much work to do to minimize your \nlifestyles impact on the enviornment. For most/all of the tested\n behaviors, you spend most of the week practicing unsustainable \nmethods. You have a lot to learn and must actively start making \na plan to reduce your impact on the enviornment.", font=("Arial",18,"italic"),bg="#edede9").pack()
        improve2 = tk.Label(frame3,text="There are many ways you can look to improve your score,\nbut make sure not to overwhelm yourself with tasks. \nFocus on one of these six sides, and stick to it \nuntil it becomes a habit. Then while maintaining that, \nhabit look to improve in another way. Eventually you'll\n be scoring as a well as a Legendary!",font=("Arial",18,"italic"),bg="#edede9").pack()
    setImprove()

    
    # tells you what to improve based on score
def findWorst():
    y = answers[0]
    for x in answers:
        if x < y:
            y = x
    return y

def findQImprove(qIndex):
    if qIndex == 0:
        q = 'this is for q1'
    elif qIndex == 1:
        q = 'q2'
    elif qIndex == 2:
        q = 'q3'
    elif qIndex == 3:
        q = 'q4'
    elif qIndex == 4:
        q = 'q5'
    else:
        q = 'q6'

def setImprove():
    OGAns = findWorst()
    worstQ1 = answers.index(OGAns)
    answers[worstQ1] = 6
    worstQ2 = answers.index(findWorst())
    answers.pop(worstQ1)
    answers.insert(worstQ1, OGAns)
    info = tk.Label(frame1,text="43-49: Lorem ipsum dolor sit amet", font=("Arial",16,"italic"))
    improve1 = tk.Label(frame1,text=findQImprove(worstQ1), font=("Arial",16,"italic"))
    improve2 = tk.Label(frame1,text=findQImprove(worstQ2), font=("Arial",16,"italic"))
    

        
    #info = tk.Label(frame3,text="43-49: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Arial",16,"italic"))
    #improve1 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    #improve2 = tk.Label(frame3,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut \nenim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial",16,"italic"))
    #info.pack(pady=5)
    #improve1.pack(pady=5)
    #improve2.pack(pady=5)

#create final and regular submit buttons
finSubmit = tk.Button(frame2, text="FINISH",font=('Arial',14,"bold"),bg="#00FF00",command=finSubmit)
submit = tk.Button(frame2, text="NEXT",font=('Arial',14,"bold"),bg="#00FF00",command=changeQ)
submit.pack(pady = 5)

#creates loop to keep window open
root.mainloop()
