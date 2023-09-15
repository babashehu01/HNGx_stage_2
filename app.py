from flask import Flask, request

app = Flask(__name__)

# Dummy data
persons = [
    {'id': 1, 'name': 'Bashehu'},
    {'id': 2, 'name': 'Shettima'},
    {'id': 3, 'name': 'Musti'}
        ]

# Displays  all people
@app.route('/api/all', methods=['GET'])
def get_persons():
    return persons

# Display a person
@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    for p in persons:
        if p['id'] == person_id:
            return p
    return {'error': 'Person not found'}

# Create a person
@app.route('/api', methods=['GET', 'POST'])
def create_person():
    new_person = {'id': len(persons)+1, 'name': request.json['name']}
    persons.append(new_person)
    return new_person

# Update a person
@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    for p in persons:
        if p['id'] == person_id:
            p['name'] = request.json['name']
            return p
    return {'error': 'Person not found'}

# Delete a person
@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    for p in persons:
        if p['id'] == person_id:
            persons.remove(p)
            return {'Success': f'{p} is deleted successfully'}
    return {'error': 'Person not found'}

if __name__ == '__main__':
    app.run(debug=True)
