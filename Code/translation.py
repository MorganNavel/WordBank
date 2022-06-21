import sqlite3
from tkinter import *

connection = sqlite3.connect("BDD/base.db")
cursor = connection.cursor()

def traitement_formulaire():
    print("The information has been successfuly sent.")
    print(language.get())
    if(language.get()=="French"):
        if(french_word.get()!=""):
            print(french_word.get())
            word=(french_word.get())
            cursor.execute("SELECT  Korean FROM Translation WHERE French = ?",word)
            print(cursor.fetchone()[0])
            Label(frame2,text="Coréen: "+cursor.fetchone()[0]+"").pack()
            cursor.execute("SELECT  English FROM Translation WHERE French = ?",word)
            Label(frame2,text="Anglais: "+cursor.fetch()[0]+".").pack()
        else:
            print("You have to fill the French field")
    elif(language.get()=="English"):
        if(english_word.get()!=""):
            word=(english_word.get())
            cursor.execute("SELECT  Korean FROM Translation WHERE English = ?",word)
            Label(frame2,text="Korean: "+cursor.fetchone()[0]+"").pack()
            cursor.execute("SELECT  French FROM Translation WHERE English = ?",word)
            Label(frame2,text="French: "+cursor.fetchone()[0]+"").pack()
        else:
            print("You have to fill the English field")
    elif(language.get()=="Korean"):
        if(english_word.get()!=""):
            word=(korean_word.get())
            cursor.execute("SELECT  English FROM Translation WHERE Korean = ?",word)
            Label(frame2,text="영국어: "+cursor.fetchone()[0]+"").pack()
            cursor.execute("SELECT  French FROM Translation WHERE Korean = ?",word)
            Label(frame2,text="프랑스어: "+cursor.fetchone()[0]+"").pack()
        else:
            print("You have to fill the Korean field")  

        

window = Tk()
window=window
window.title("WordBank")
window.minsize(480,360)
window.config(background="white")

korean_word=StringVar()
french_word=StringVar()
english_word=StringVar()

language=StringVar()


#création d'un titre
label_title = Label(window, bg="white",text="Translation App",font=("Arial",25))
label_title.pack()

#création d'une boite
frame = Frame(window,bg="white")

#champ de texte
Radiobutton(frame, bg="white",variable=language,value="French").pack()
label_french = Label(frame, bg="white",text="Enter french word",font=("Arial",10))
french_field = Entry(frame,bg="white",text="French",font=("Arial"),textvariable = french_word)
label_french.pack()
french_field.pack(expand=YES)


Radiobutton(frame, bg="white",variable=language,value="English").pack()
label_english = Label(frame, bg="white",text="Enter english word",font=("Arial",10))
english_field = Entry(frame,bg="white",text="English",font=("Arial"), textvariable = english_word)
label_english.pack()
english_field.pack(expand=YES)

Radiobutton(frame, bg="white",variable=language,value="Korean").pack()
label_korean = Label(frame, bg="white",text="Enter korean word",font=("Arial",10))
korean_field = Entry(frame,bg="white",text="Korean",font=("Arial"),textvariable=korean_word)
label_korean.pack()
korean_field.pack(expand=YES)
        
button_submit = Button(frame,bg="white",text="Submit",font=("Arial"),command=traitement_formulaire)
button_submit.pack(pady=25)

frame.pack()

frame2 = Frame(window,bg="white")

        
window.mainloop()
connection.close()

