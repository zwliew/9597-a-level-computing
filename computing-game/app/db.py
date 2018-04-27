import sqlite3
import os

DB_PATH = 'game.sqlite3'

def connect():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create():
    if os.path.isfile(DB_PATH):
        print('The database already exists; skipping database creation.')
        return
    conn = connect()
    conn.execute('CREATE TABLE question(text TEXT, answer INTEGER)')
    conn.execute('CREATE TABLE attempt(question_id INTEGER, guess INTEGER)')
    conn.close()

def get_questions():
    conn = connect()
    questions = conn.execute('SELECT * FROM question').fetchall()
    conn.close()
    return questions

def add_question(text, answer):
    conn = connect()
    cur = conn.execute(
        'INSERT INTO question VALUES (?, ?)', (text, answer)
    )
    rowid = cur.lastrowid
    conn.close()
    return rowid

def get_question(rowid):
    conn = connect()
    question = conn.execute(
        'SELECT * FROM question WHERE rowid=?', (rowid,)
    ).fetchone()
    conn.close()
    return question

def delete_question(id):
    pass
