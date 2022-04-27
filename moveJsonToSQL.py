import sqlite3
from sqlite3 import Error
import json
from pathlib import Path
import os
from classes import Word

allWords = []

def nextWord():
	dataDir = os.getcwd()
	abc = "abcdefghijklmnopqrstuzyx"
	
	for l in abc:
		filename = l
		filepath = os.path.join(dataDir,f"data/{filename}.json")
		
		with open(filepath) as json_file:
			data = json.load(json_file)
   
		for i in data:
			if ' ' not in i and '.' not in i and "'" not in i and len(i) == 5:
				wordAndDef = Word(i, data[i]["meanings"][0]["def"])
				allWords.append(wordAndDef)

	return allWords

mydictionary = nextWord()
dictLength = len(mydictionary)
print(dictLength)

def create_connection(db_file):
	""" create a database connection to the SQLite database
		specified by db_file
	:param db_file: database file
	:return: Connection object or None
	"""
	conn = None
	try:
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)

	return conn


def create_project(conn, project):
	"""
	Create a new word into the wordlist table
	:param conn:
	:param project:
	:return: word_id
	"""
	sql = ''' INSERT INTO wordlist(word,definition)
			  VALUES(?,?) '''
	cur = conn.cursor()
	cur.execute(sql, project)
	conn.commit()
	return cur.lastrowid

def main():
	database = r"./data/words.db"

	# create a database connection
	conn = create_connection(database)
	with conn:
		# Add all words
		for i in range (len(mydictionary)):
			project = (mydictionary[i].word, mydictionary[i].definition);
			project_id = create_project(conn, project)

if __name__ == '__main__':
	main()
