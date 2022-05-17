from lib2to3.pgen2.token import TILDE
from os import curdir
import sqlite3

class Database:

    

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, number INTEGER)")
        
        
    
    def insert(self, name, number):
        
        self.cur.execute("INSERT INTO contacts VALUES (NULL, ?, ?)", (name, number))
        self.conn.commit()
        
    
    def  view(self):
        self.cur.execute("SELECT * FROM contacts")
        rows = self.cur.fetchall()
        
        return rows


    def search(self, name="", number=""):
        
        self.cur.execute("SELECT * FROM contacts WHERE name = ? OR number = ?", (name, number))
        rows = self.cur.fetchall()
        
        return rows


    def delete(self, id):
        
        self.cur.execute("DELETE FROM contacts WHERE id=?",(id,))
        self.conn.commit()
        


    def update(self, id, name, number):
       
        self.cur.execute("UPDATE contacts SET name = ?, number = ? WHERE id = ?", (name, number, id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
    
   

    




#print(search(author = "jacob jackson"))