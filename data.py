import sqlite3
import csv 

conn= sqlite3.connect('iris.db')
cursor=conn.cursor()
iris_data= """CREATE TABLE IF NOT EXISTS iris_data (
  
)