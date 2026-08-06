import os
import sqlite3
import hashlib
import pickle

PASSWORD = "admin123"

username = input("Username: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username='" + username + "'"
cursor.execute(query)

command = input("Command: ")
os.system(command)

data = pickle.loads(open("data.pkl", "rb").read())

print(hashlib.md5(b"hello").hexdigest())
