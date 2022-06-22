import sqlite3
from tkinter import *
connection = sqlite3.connect("BDD/base.db")
cursor = connection.cursor()

def traitement_formulaire():
    print("The information has been successfuly sent")
    print("The Korean word "+korean_word.get())
    print("The English word "+english_word.get())
    print("The French word "+french_word.get())
    if(korean_word.get()!="" and english_word.get()!="" and french_word!=""):
        new_word=(french_word.get(),korean_word.get(),english_word.get(),cursor.lastrowid)
        cursor.execute("INSERT INTO Translation VALUES(?,?,?,?)",new_word)
        connection.commit()
        print("The word has sucessfuly been send to the word bank.")
    else:
        print("You have to fill all the fields.")


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
frame = Frame(window,bg="white")
#champ de texte
label_french = Label(frame, bg="white",text="Enter french word",font=("Arial",10))
french_field = Entry(frame,bg="white",text="French",font=("Arial"),textvariable = french_word)
label_french.pack()
french_field.pack(expand=YES)

label_english = Label(frame, bg="white",text="Enter english word",font=("Arial",10))
english_field = Entry(frame,bg="white",text="English",font=("Arial"), textvariable = english_word)
label_english.pack()
english_field.pack(expand=YES)

label_korean = Label(frame, bg="white",text="Enter korean word",font=("Arial",10))
korean_field = Entry(frame,bg="white",text="Korean",font=("Arial"),textvariable=korean_word)
label_korean.pack()
korean_field.pack(expand=YES)
        
button_submit = Button(frame,bg="white",text="Submit",font=("Arial"),command=traitement_formulaire)
button_submit.pack(pady=25)

open_new_window = Button(frame,bg="white",text="Go to Translation",font=("Arial"),command=translation_window)
open_new_window.pack(pady=25)
frame.pack()

        
window.mainloop()
connection.close()

