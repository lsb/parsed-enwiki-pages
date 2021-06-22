import json
import sys
import sqlite3

con = sqlite3.connect("parsedpages.db")
con.execute("create table pages (id integer primary key, title text, body text, entropy integer)")

for line in sys.stdin:
  [id, title, parsedtext, entropy] = json.loads(line)
  con.execute("insert into pages (id, title, body, entropy) values (?,?,?,?)", (id, title, parsedtext, entropy))

con.execute("commit")
