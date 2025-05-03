from flask import Flask
from controllers import contact_controller
from models.contact_model import init_db

app = Flask(__name__)
app.config['DATABASE'] = 'data/contacts.db'

with app.app_context():
    init_db()
    
# Routes
app.add_url_rule('/', 'home', contact_controller.list_contacts)
app.add_url_rule('/add', 'add_contact', contact_controller.add_contact, methods=['GET', 'POST'])
app.add_url_rule('/edit/<int:id>', 'edit_contact', contact_controller.edit_contact, methods=['GET', 'POST'])
app.add_url_rule('/delete/<int:id>', 'delete_contact', contact_controller.delete_contact)
app.add_url_rule('/search', 'search_contact', contact_controller.search_contact, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
