import sqlite3
from tkinter import *

connection = sqlite3.connect("base.db")
cursor = connection.cursor()
word = ""
def addWord(cursor,connection,reponse):
    print("Enter the English word first.")
    english_word=input()
    print("Then enter the French word.")
    french_word=input()
    print("And then the Korean word.")
    korean_word=input()
    new_word=(french_word,korean_word,english_word,cursor.lastrowid)
    cursor.execute("INSERT INTO Translation VALUES(?,?,?,?)",new_word)
    connection.commit()
    print("The word has sucessfuly been send to the word bank.")
    
            
def getTranslation(cursor,language):
    stop = False
    if(language == "English"):
        while(not(stop)):
            print("\nEnter a word you want to translate or enter '?!' to choose another language.")
            string=input()
            if(string=="?!"):
                stop=True
            else:
                word = (string,)
                cursor.execute("SELECT  Korean FROM Translation WHERE English = ?",word)
                print("The translation is "+cursor.fetchone()[0]+" in Korean.")
                cursor.execute("SELECT  French FROM Translation WHERE English = ?",word)
                print("The translation is "+cursor.fetchone()[0]+" in French.")
    elif(language=="French"):
        while(not(stop)):
            print("\nChoisissez le mot que vous voulez traduire ou entrer '?!' pour choisir une autre langue.")
            string=input()
            if(string=="?!"):
                stop=True
            else:
                word = (string,)
                cursor.execute("SELECT  Korean FROM Translation WHERE French = ?",word)
                print("Le mot se traduit par "+cursor.fetchone()[0]+" en Coréen.")
                cursor.execute("SELECT  English FROM Translation WHERE French = ?",word)
                print("Le mot se traduit par "+cursor.fetchone()[0]+" en Anglais.")
    elif(language=="Korean"):
        while(not(stop)):
            print("\n언어를 선택하세요 다른 언어를 선택할 경우에는 ?!를 누르세요.")
            string=input()
            if(string=="?!"):
                stop=True
            else :
                word = (string,)
                cursor.execute("SELECT  French FROM Translation WHERE Korean = ?",word)
                print("이 말이 프랑스로 "+cursor.fetchone()[0]+" 이라고 예요.")
                cursor.execute("SELECT  English FROM Translation WHERE Korean = ?",word)
                print("이 말이 영어로 "+cursor.fetchone()[0]+" 이라고 예요.")
    else:
        exit()
    stop=False
    
print("Enter 'Yes' or 'No' to enter a new word to the word bank.")
response=input()
while(response=="Yes" or response=="No"):
    if(response=="Yes"):
        while(response=="Yes"):
            addWord(cursor, connection,response)
            print("Enter 'Yes' or 'No' if you want to enter a new word to the word bank.")
            response=input()  
    if(response=="No"):
        while(True):
            print("You have to choose between French/English/Korean or enter anything else to exit.")
            language = input()
            getTranslation(cursor, language)
    elif(response!="Yes" and response!="No"):
        while(response!="Yes" and response!="No"):
            print("You have to enter 'Yes' or 'No', Please try again...")
            response=input()
connection.close()