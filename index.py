import tkinter as tk
root = tk.Tk()
root.geometry("700x700")
root.configure(bg='#28282B')
root.title("Software Design")
frame1 = tk.Frame(root,bg="#50ad6f",width = 50)
title = tk.Label(frame1, text='Ecological Calculator',font=('Arial', 40,"bold"),fg = "white", bg="#50ad6f",width=50).pack(pady=20)
frame1.pack(pady=(70,0))
frame2 = tk.Frame(root,bg="#edede9",width=25)

frame21 = tk.Frame(frame2, width=50)
frame22 = tk.Frame(frame2, width=50)
motto = tk.Label(frame2,text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",font=('Arial',16),fg="black",width=125).pack(pady=10)
q1 = tk.Label(frame2,text="This will be determined later, so this is placeholder text in the place of Question 1",font=('Arial',16,"bold")).pack(pady=(10,10))
button1 = tk.Button(frame21, text="Option 1: Placeholder", font=('Arial',15,'bold'), fg = "#50ad6f").pack(ipady=50,ipadx=50,side="left")
button2 = tk.Button(frame21, text="Option 2: Placeholder", font=('Arial',15,'bold'), fg = "#50ad6f").pack(ipady=50,ipadx=50,side="left")
button3 = tk.Button(frame22, text="Option 3: Placeholder", font=('Arial',15,'bold'), fg = "#50ad6f").pack(ipady=50,ipadx=50,side="left")
button4 = tk.Button(frame22, text="Option 4: Placeholder", font=('Arial',15,'bold'), fg = "#50ad6f").pack(ipady=50,ipadx=50,side="left")
frame2.pack(ipady=10)
frame21.pack()

frame22.pack()
root.mainloop()
