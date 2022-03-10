import sqlite3


def createDatabase():
   con = sqlite3.connect('./space_asteroid/score.db')
   cur = con.cursor()
   player ='''CREATE TABLE IF NOT EXISTS player(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome VARCHAR(25)
   )'''
   cur.execute(player)
   score ='''CREATE TABLE IF NOT EXISTS score(
       id INTEGER PRIMARY KEY AUTOINCREMENT, 
       score int,
       data date,
       id_player int
   )'''
   cur.execute(score)
   con.close()

