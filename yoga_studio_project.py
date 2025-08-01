import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from PIL import Image
import registration as reg

#setting up window, instance of Tk class
window=tk.Tk()
window.geometry("600x600")
window.title("Smiski Yoga Studio")


#welcome label and image
welcome=tk.Label(text="Welcome to the Smiski Yoga Studio!",font=("Arial",15,"bold"),foreground="black",background="light green",width=30,height=2)
welcome.pack()

pil=Image.open("yoga.png").resize((200,100))
tkimg=ImageTk.PhotoImage(pil)
imglabel=tk.Label(image=tkimg)
imglabel.pack()
    
#function to show info
def info(buttonpressed):
    if buttonpressed == 'instructors':
        pil=Image.open("emily.png").resize((150,150))
        image=ImageTk.PhotoImage(pil)
        imagebox.config(image=image)
        imagebox.image=image

        name1=tk.Label(window,text=""" Emily
        Experience: 5 yrs
        Specialty: Hatha Yoga
        Fun Fact: Loves rocks""",font=("Arial",8),width=25,height=8,bg="light green",fg="black")
        name1.pack(side=tk.LEFT)
        
        pil2=Image.open("reb.png").resize((150,150))
        image2=ImageTk.PhotoImage(pil2)
        imagebox2.config(image=image2)
        imagebox2.image=image2
        name2=tk.Label(window,text=""" Reb
        Experience: 22 yrs
        Specialty: Vinyasa Yoga
        Fun Fact: Allergic to fruit""",font=("Arial",8),width=25,height=8,bg="light green",fg="black")
        name2.pack(side=tk.RIGHT)
        
    elif buttonpressed == 'class':
        lbl=tk.Label(window,text="We offer Hatha and Vinyasa yoga classes.",font=("Arial",12),width=40,height=6,bg="light green",fg="black")
        lbl.pack(side=tk.TOP)

        text_display = tk.Text(window,width=79,height=10)  
        text_display.pack()
        def open_txt():
            f=open("yogastyle.txt").read()
            text_display.insert(0.0, f)
    
        open_button = tk.Button(window, text="Click here to learn more", command=open_txt)
        open_button.pack()        

    elif buttonpressed == 'register':
        db={1:('Monday','Beginner Hatha @7PM w/ Emily',25.99),2:('Monday','Vinyasa @10AM w/ Reb',25.99),
            3:('Wednesday','Hatha @5PM w/ Emily',25.99),4:('Wednesday','Vinyasa @12PM w/ Reb',25.99),
            5:('Friday','Advanced Vinyasa @8AM w/ Reb',25.99),6:('Friday','Hatha @8PM w/ Emily',25.99)}
        print('Thank you for registering for Smiski Yoga Studio Classes.\n\nHere is our class schedule:')

        for k, v in db.items():
            print('{}) {}: {} (${})'.format(k,v[0],v[1],v[2]))

        a=reg.Classes()
        a.register()
        a.printClass()
        a.price()
        
    
#instruction label
tk.Label(window, font=("Arial",12, "bold"), text="Click a button for information about us!",bg="light green").pack()

#frame for buttons
f1=tk.Frame(window)
f1.pack()

#button 1 + alignment
b1=tk.Button(f1,text="Meet Our Instructors",width=20,bg="white",fg="black",command=lambda: info('instructors'))
b1.grid(row=0,column=0)

#button 2 + alignment
b2=tk.Button(f1,text="Class Offerings",width=20,bg="white",fg="black",command=lambda: info('class'))
b2.grid(row=0,column=1)

#button 3 + alignment
b3=tk.Button(f1,text="Register Here",width=20,bg="white",fg="black",command=lambda: info('register'))
b3.grid(row=0,column=2)

#labels for instructor img
imagebox=tk.Label(window)
imagebox.pack(side=tk.LEFT)

imagebox2=tk.Label(window)
imagebox2.pack(side=tk.RIGHT)



window.mainloop()
