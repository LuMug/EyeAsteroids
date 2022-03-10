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

def _insert_result(score, player):
  conn = sqlite3.connect('./space_asteroid/score.db')
  date = datetime.today().strftime('%Y-%m-%d')
  conn.execute(f"INSERT INTO Score (score, data, nome) VALUES ({score}, {date}, {player})")
  conn.commit()
  conn.close()

def _show_result():
  conn = sqlite3.connect('./space_asteroid/score.db')
  cor = cur.cursor()
  cur.execute("SELECT * FROM Score")
  rows = cur.fetchall()

  for row in rows:
      print(row)

  conn.commit()
  conn.close()


