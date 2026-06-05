from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(load_contacts())

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data.get('name', '').strip()
    phone = data.get('phone', '').strip()
    email = data.get('email', '').strip()
    address = data.get('address', '').strip()

    if not name or not phone:
        return jsonify({'error': 'Name and phone are required'}), 400

    contacts = load_contacts()


    if any(c['phone'] == phone for c in contacts):
        return jsonify({'error': 'A contact with this phone number already exists'}), 400

    new_contact = {
        'id': max([c['id'] for c in contacts], default=0) + 1,
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    return jsonify(new_contact), 201

@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.get_json()
    contacts = load_contacts()
    contact = next((c for c in contacts if c['id'] == contact_id), None)

    if not contact:
        return jsonify({'error': 'Contact not found'}), 404

    name = data.get('name', '').strip()
    phone = data.get('phone', '').strip()

    if not name or not phone:
        return jsonify({'error': 'Name and phone are required'}), 400

   
    if any(c['phone'] == phone and c['id'] != contact_id for c in contacts):
        return jsonify({'error': 'Another contact with this phone already exists'}), 400

    contact['name']    = name
    contact['phone']   = phone
    contact['email']   = data.get('email', '').strip()
    contact['address'] = data.get('address', '').strip()
    save_contacts(contacts)
    return jsonify(contact)

@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contacts = load_contacts()
    updated = [c for c in contacts if c['id'] != contact_id]
    if len(updated) == len(contacts):
        return jsonify({'error': 'Contact not found'}), 404
    save_contacts(updated)
    return jsonify({'message': 'Deleted'})

@app.route('/search', methods=['GET'])
def search_contacts():
    query = request.args.get('q', '').lower().strip()
    if not query:
        return jsonify([])
    contacts = load_contacts()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
