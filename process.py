import sqlite3
import csv 


con = sqlite3.connect('D:/VSC/bot_project/db/dictionary_db.sqlite') 

cur = con.cursor()

def add_word(en_word, ru_word):
    cur.execute("""INSERT INTO test (en_word, ru_word) VALUES (?, ?)""", (en_word, ru_word))

    con.commit()
