import sqlite3
from tkinter import *
window = Tk()
def show_frame(frame,frame2,label):
    frame2.pack_forget()
    label.pack_forget()
    frame.pack()
    label.pack()
    


def translate_word():
    for child in frameTranslation.winfo_children():
        child.destroy()
    connection = sqlite3.connect("base.db")
    with connection:
        cursor = connection.cursor()
    if(language.get()=="French"):
        if(french_word.get()!=""):
            word=(french_word.get(),)
            cursor.execute("SELECT  English FROM Translation WHERE French = ?",word)
            Label(frameTranslation,bg="white",text="English: "+cursor.fetchone()[0],font=("Arial")).pack()
            cursor.execute("SELECT  Korean FROM Translation WHERE French = ?",word)
            Label(frameTranslation,bg="white",text="Korean: "+cursor.fetchone()[0],font=("Arial")).pack()
        else:
            Label(frameTranslation,bg="white",text="You have to fill the French field",font=("Arial")).pack()
    elif(language.get()=="English"):
        if(english_word.get()!=""):
            word=(english_word.get(),)
            cursor.execute("SELECT  French FROM Translation WHERE English = ?",word)
            Label(frameTranslation,bg="white",text="French: "+cursor.fetchone()[0],font=("Arial")).pack()
            cursor.execute("SELECT  Korean FROM Translation WHERE English = ?",word)
            Label(frameTranslation,bg="white",text="Korean: "+cursor.fetchone()[0],font=("Arial")).pack()
        else:
            Label(frameTranslation,bg="white",text="You have to fill the English field",font=("Arial")).pack()
    elif(language.get()=="Korean"):
        if(korean_word.get()!=""):
            word=(korean_word.get(),)
            cursor.execute("SELECT  English FROM Translation WHERE Korean = ?",word)
            Label(frameTranslation,bg="white",text="English: "+cursor.fetchone()[0],font=("Arial")).pack()
            cursor.execute("SELECT  French FROM Translation WHERE Korean = ?",word)
            Label(frameTranslation,bg="white",text="French: "+cursor.fetchone()[0],font=("Arial")).pack()
        else:
            Label(frameTranslation,bg="white",text="You have to fill the Korean field",font=("Arial")).pack()
    connection.close()
    
def register_word():
    for child in message_space.winfo_children():
        child.destroy()
    connection = sqlite3.connect("base.db")
    with connection:
        cursor = connection.cursor()
    if(korean_word.get()!="" and english_word.get()!="" and french_word.get()!=""):
        new_word=(french_word.get(),korean_word.get(),english_word.get(),cursor.lastrowid)
        cursor.execute("INSERT INTO Translation VALUES(?,?,?,?)",new_word)
        connection.commit()
        Label(message_space,text="The word has been sent to the word bank successfully.",bg="white",font=("Arial")).pack()
    else:
        Label(message_space,text="You have to fill all the fields.",bg="white",font=("Arial")).pack()
    connection.close()

    

        


window.title("WordBank")
window.minsize(480,360)
window.config(background="white")
#frame1
korean_word=StringVar()
french_word=StringVar()
english_word=StringVar()

language=StringVar()


#title creation
label_title = Label(window, bg="white",text="Translation App",font=("Arial",25))
label_title.pack()

#frame creation
frame = Frame(window,bg="white")

#fields

Radiobutton(frame, bg="white",variable=language,value="English").pack()
label_english = Label(frame, bg="white",text="Enter English word",font=("Arial",10))
english_field = Entry(frame,bg="white",text="English",font=("Arial"), textvariable = english_word)
label_english.pack()
english_field.pack(expand=YES)

Radiobutton(frame, bg="white",variable=language,value="French").pack()
label_french = Label(frame, bg="white",text="Enter French word",font=("Arial",10))
french_field = Entry(frame,bg="white",text="French",font=("Arial"),textvariable = french_word)
label_french.pack()
french_field.pack(expand=YES)

Radiobutton(frame, bg="white",variable=language,value="Korean").pack()
label_korean = Label(frame, bg="white",text="Enter Korean word",font=("Arial",10))
korean_field = Entry(frame,bg="white",text="Korean",font=("Arial"),textvariable=korean_word)
label_korean.pack()
korean_field.pack(expand=YES)
        
button_submit = Button(frame,bg="white",text="Submit",font=("Arial"),command=translate_word)
button_submit.pack(pady=25)

button_change=Button(frame,bg="white",text="A new word ?",font=("Arial"),command=lambda:show_frame(frame2,frame,labelInfo))
button_change.pack()
frameTranslation=Frame(frame, bg="white")
frameTranslation.pack()
frame.pack()
labelInfo=Label(window,text="Made by Morgan L2-Computer Science at the University of Montpellier,France.",font=("Arial",7),bg="white")
labelInfo.pack()

#frame2
frame2 = Frame(window,bg="white")
#fields
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
        
button_submit = Button(frame2,bg="white",text="Submit",font=("Arial"),command=register_word)
button_submit.pack(pady=25)
button_change2=Button(frame2,bg="white",text="Want to know a word ?",font=("Arial"),command=lambda:show_frame(frame,frame2,labelInfo))
button_change2.pack()
message_space=Frame(frame2,bg="white")
message_space.pack()






        
window.mainloop()

