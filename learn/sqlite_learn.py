import sqlite3

conn = sqlite3.connect("book.db")
cur = conn.cursor()
def create_table():
  
  sql = """
  CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
  )
  """
  with conn:
    cur.execute(sql)

def add_book(title, author, year):
  sql = """
  INSERT INTO book(title, author, year) VALUES(?, ?, ?)
  """
  with conn:
    cur.execute(sql, (title, author, year))
  
def get_books():
  sql = """
  SELECT * FROM book
  """
  with conn:
    cur.execute(sql)
    res = cur.fetchall()
    list_res = []
    for row in res:
      id = row[0]
      title = row[1]
      author = row[2]
      year = row[3]
      list_res.append({"id": id, "title": title, "author": author, "year": year})
    return list_res


  
def get_book_from_id(id: int):
  sql = """
  SELECT * FROM book WHERE id = ?
  """
  with conn:
    cur.execute(sql, (id,))
    return cur.fetchone()

if __name__ == "__main__":
  # add_book("ICECREAM", "F. Scott Fitzgerald", 1925)
  print(get_books())
  conn.close()




