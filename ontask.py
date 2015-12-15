#!/usr/bin/python3

import sqlite3
import time
import datetime
import os

screen=[
"Welcome to OnTask! Type 'help' for commands"
]

class DatabaseManager(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.row_factory = sqlite3.Row
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def dict_query(self, arg):
        
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur.fetchall()    

    def __del__(self):
        self.conn.close()




def refresh():
	os.system('cls' if os.name == 'nt' else 'clear')
	for lines in screen:
		print(lines)

def returnDateString():
	date=datetime.datetime.now()
	return date.strftime("%A the %d, %B %Y")

def returnTimeString():
	date=datetime.datetime.now()
	return date.strftime("%I:%M %p")	

def showTime():
	print("It is "+returnTimeString() +" on "+returnDateString())

db_location="test.db"
global dbmgr
dbmgr = DatabaseManager(db_location)

dbmgr.query("create table if not exists task_log(id INT, 'in_out' TEXT, task_name TEXT)")
dbmgr.query("create table if not exists task_goals(task_name TEXT, deadline timestamp)") #make sure deadline is inputted as a date only, no time




class taskManager():
    def __init__(self):
    	global dbmgr
        

    def showTasks(self):
    	global dbmgr

    	query = dbmgr.dict_query("SELECT * FROM task_log;")

    	rows = query
    	for row in rows:
        	print(row["task_name"], "clocked", row["in_out"],"at", "10:00PM")


#for row in dbmgr.query("SELECT name FROM sqlite_master WHERE type='table'"):
#	print(row[0])
global tasks
tasks=taskManager()

def takeCmd():
	while True:
	
		user_input=input("Enter command $: ")

		if user_input == "show task":
			tasks.showTasks()
		elif user_input == "end task":
			user.add_nonessential()	
		elif user_input == "exit":
			global dbmgr
			del dbmgr
			exit()		
		else:
			print('Invalid command ¯\_(ツ)_/¯ \nType "help" for well.. help')




while True:
	refresh()
	showTime()
	print("")
	takeCmd()
















