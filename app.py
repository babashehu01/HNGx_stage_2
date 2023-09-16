import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
data_file = os.path.join(os.path.dirname(__file__), 'data.json')

# Function to read data from the file
def read_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    else:
        return []

# Function to write data to the file
def write_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)

# Displays all people
@app.route('/api/all', methods=['GET'])
def get_persons():
    persons = read_data()
    return jsonify({'persons': persons})

# Display a person
@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    persons = read_data()
    for p in persons:
        if p['id'] == person_id:
            return jsonify({'person': p})
    return jsonify({'error': 'Person not found'})

# Create a person
@app.route('/api', methods=['POST'])
def create_person():
    data = read_data()
    new_person = {'id': len(data) + 1, 'name': request.json['name']}
    data.append(new_person)
    write_data(data)
    return jsonify(new_person)

# Update a person
@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = read_data()
    for p in data:
        if p['id'] == person_id:
            p['name'] = request.json['name']
            write_data(data)
            return jsonify(p)
    return jsonify({'error': 'Person not found'})
# Delete a person
@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    data = read_data()
    for p in data:
        if p['id'] == person_id:
            data.remove(p)
            write_data(data)
            return jsonify({'success': f'Person with ID {person_id} deleted successfully'})
    return jsonify({'error': 'Person not found'})

if __name__ == '__main__':
    app.run(debug=True)

