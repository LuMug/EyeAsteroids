import sqlite3


def createDatabase():
   con = sqlite3.connect('./space_asteroid/score.db')
   cur = con.cursor()
   score ='''CREATE TABLE IF NOT EXISTS score(
       id INTEGER PRIMARY KEY AUTOINCREMENT, 
       score int,
       data date,
       nome varchar(25)
   )'''
   cur.execute(score)
   con.close()

