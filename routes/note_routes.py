from flask import Blueprint, request, jsonify
from models.note_model import insert_note_db, update_note_db, delete_note_db, get_all_notes_db

note_bp = Blueprint('notes', __name__)

@note_bp.route('/insert2', methods=['POST'])
def insert_note():
    userInputArray = request.json
    if 'note_name' not in userInputArray or 'note_description' not in userInputArray:
        return jsonify({'error': 'Missing required fields'}), 400

    name_input = userInputArray['note_name']
    description_input = userInputArray['note_description']
    note_id = insert_note_db(name_input, description_input)

    if note_id:
        return jsonify({'id': note_id}), 201
    return jsonify({'error': 'Failed to insert note'}), 500

@note_bp.route('/update2/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    userInputArray = request.json
    name_input = userInputArray.get('note_name')
    description_input = userInputArray.get('note_description')
    updated = update_note_db(note_id, name_input, description_input)

    if updated:
        return jsonify({'message': 'Note updated successfully'}), 200
    return jsonify({'message': 'ID not found'}), 404

@note_bp.route('/viewAll2/', methods=['GET'])
def viewall():
    all_notes = get_all_notes_db()
    if all_notes is not None:
        return jsonify(all_notes), 200
    return jsonify({'error': 'Failed to retrieve records'}), 500

@note_bp.route('/delete2/<int:note_id>', methods=['DELETE'])
def delete(note_id):
    deleted = delete_note_db(note_id)
    if deleted:
        return jsonify({'message': 'Deleted successfully'}), 200
    return jsonify({'message': 'ID not found'}), 404