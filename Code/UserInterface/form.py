import sqlite3
from tkinter import *
connection = sqlite3.connect("./base.db")
cursor = connection.cursor()

def traitement_formulaire():
    for child in message_space.winfo_children():
        child.destroy()
    if(korean_word.get()!="" and english_word.get()!="" and french_word.get()!=""):
        new_word=(french_word.get(),korean_word.get(),english_word.get(),cursor.lastrowid)
        cursor.execute("INSERT INTO Translation VALUES(?,?,?,?)",new_word)
        connection.commit()
        Label(message_space,text="The word has been sent to the word bank successfully.",bg="white",font=("Arial")).pack()
    else:
        Label(message_space,text="You have to fill all the fields.",bg="white",font=("Arial")).pack()


window = Tk()
window=window
window.title("WordBank")
window.minsize(480,360)
window.config(background="white")
korean_word=StringVar()
french_word=StringVar()
english_word=StringVar()
#création d'un titre
label_title = Label(window, bg="white",text="Welcome to your own word bank",font=("Arial",25))
label_title.pack()
#création d'une boite
frame2 = Frame(window,bg="white")
#champ de texte
label_french = Label(frame2, bg="white",text="Enter French word",font=("Arial",10))
french_field = Entry(frame2,bg="white",text="French",font=("Arial"),textvariable = french_word)
label_french.pack()
french_field.pack(expand=YES)

label_english = Label(frame2, bg="white",text="Enter English word",font=("Arial",10))
english_field = Entry(frame2,bg="white",text="English",font=("Arial"), textvariable = english_word)
label_english.pack()
english_field.pack(expand=YES)

label_korean = Label(frame2, bg="white",text="Enter Korean word",font=("Arial",10))
korean_field = Entry(frame2,bg="white",text="Korean",font=("Arial"),textvariable=korean_word)
label_korean.pack()
korean_field.pack(expand=YES)
        
button_submit = Button(frame2,bg="white",text="Submit",font=("Arial"),command=traitement_formulaire)
button_submit.pack(pady=25)

frame2.pack()
message_space=Frame(window,bg="white")
message_space.pack()
Label(window,bg="white",text="Made by Morgan L2-Computer Science at the University of Montpellier,France.",font=("Arial",7)).pack()

        
window.mainloop()
connection.close()

