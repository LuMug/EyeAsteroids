import sqlite3
con = sqlite3.connect('score.db')
cur = con.cursor()
cur.execute("DROP table IF EXISTS player;");
player ='''CREATE TABLE player(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   nome VARCHAR(25)
)'''
cur.execute(player)
cur.execute("DROP table IF EXISTS score;");
score ='''CREATE TABLE score(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    score int,
    data date,
    id_player int
)'''
cur.execute(score)
con.close()

