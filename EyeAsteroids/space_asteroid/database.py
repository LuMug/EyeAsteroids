import sqlite3
from datetime import datetime


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

def insertResult(score, player):
   conn = sqlite3.connect('./space_asteroid/score.db')
   date = datetime.today().strftime('%Y-%m-%d')
   cur = conn.cursor()
   cur.execute(f"INSERT INTO score (score, data, nome) VALUES ({score}, '{date}', '{player}')")
   conn.commit()
   conn.close()

def showResult():
   conn = sqlite3.connect('./space_asteroid/score.db')
   cur = conn.cursor()
   cur.execute("SELECT nome, score, id FROM Score ORDER BY score DESC LIMIT 5")
   rows = cur.fetchall()

   #for row in rows:
   #   print(row)

   conn.commit()
   conn.close()
   return rows

