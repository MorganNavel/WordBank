import sqlite3
from tkinter import *
class Formulaire:
    def __init__(self,window):
        self.window=window
        self.window.title("WordBank")
        self.window.minsize(480,360)
        self.window.config(background="white")
        #création d'un titre
        label_title = Label(window, bg="white",text="Welcome to your own word bank",font=("Arial",25))
        label_title.pack()
        #création d'une boite
        frame = Frame(window,bg="white")
        #champ de texte
        label_french = Label(frame, bg="white",text="Enter french word",font=("Arial",10))
        french_word = Entry(frame,bg="white",text="French",font=("Arial"))
        label_french.pack()
        french_word.pack(expand=YES)

        label_english = Label(frame, bg="white",text="Enter english word",font=("Arial",10))
        english_word = Entry(frame,bg="white",text="English",font=("Arial"))
        label_english.pack()
        english_word.pack(expand=YES)

        label_korean = Label(frame, bg="white",text="Enter korean word",font=("Arial",10))
        korean_word = Entry(frame,bg="white",text="Korean",font=("Arial"))
        label_korean.pack()
        korean_word.pack(expand=YES)
        
        button_submit = Button(frame,bg="white",text="Submit",font=("Arial"))
        button_submit.pack(pady=25)
        frame.pack()
window = Tk()
obj=Formulaire(window)
window.mainloop()

#def traitement_formulaire():
#    try:
        
#    except Exception as es:
#        messagebox.error
#button


