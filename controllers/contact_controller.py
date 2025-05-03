from flask import render_template, request, redirect, url_for
from models import contact_model

def list_contacts():
    contacts = contact_model.get_contacts()
    return render_template('list_contacts.html', contacts=contacts)

def add_contact():
    if request.method == 'POST':
        nom = request.form['nom']
        telephone = request.form['telephone']
        email = request.form['email']
        contact_model.add_contact(nom, telephone, email)
        return redirect(url_for('home'))
    return render_template('add_contact.html')

def edit_contact(id):
    contact = contact_model.get_contact_by_id(id)
    if request.method == 'POST':
        nom = request.form['nom']
        telephone = request.form['telephone']
        email = request.form['email']
        contact_model.update_contact(id, nom, telephone, email)
        return redirect(url_for('home'))
    return render_template('edit_contact.html', contact=contact)

def delete_contact(id):
    contact_model.delete_contact(id)
    return redirect(url_for('home'))

def search_contact():
    query = request.args.get('q', '')
    contacts = contact_model.search_contacts(query)
    return render_template('list_contacts.html', contacts=contacts)
