import sqlite3
from flask import g
import os

DATABASE = os.path.join('data', 'contacts.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    with sqlite3.connect(DATABASE) as db:
        with open('schema.sql', mode='r', encoding='utf-8') as f:
            db.executescript(f.read())

def get_contacts():
    db = get_db()
    return db.execute('SELECT * FROM contacts').fetchall()

def add_contact(nom, telephone, email):
    db = get_db()
    db.execute('INSERT INTO contacts (nom, telephone, email) VALUES (?, ?, ?)', (nom, telephone, email))
    db.commit()

def get_contact_by_id(contact_id):
    db = get_db()
    return db.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,)).fetchone()

def update_contact(contact_id, nom, telephone, email):
    db = get_db()
    db.execute('UPDATE contacts SET nom = ?, telephone = ?, email = ? WHERE id = ?', (nom, telephone, email, contact_id))
    db.commit()

def delete_contact(contact_id):
    db = get_db()
    db.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    db.commit()

def search_contacts(query):
    db = get_db()
    like_query = f"%{query}%"
    return db.execute('SELECT * FROM contacts WHERE nom LIKE ? OR email LIKE ?', (like_query, like_query)).fetchall()
