from models.todo import Todo
from flask import jsonify, request
from extensions import db

def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        return jsonify(todo.to_dict())
    else:
        return jsonify({'error': 'Todo not found'}), 404

def create_todo():
    data = request.get_json()
    todo = Todo(title=data['title'], description=data['description'])
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201

def update_todo(todo_id):
    data = request.get_json()
    todo = Todo.query.get(todo_id)
    if todo:
        todo.title = data['title']
        todo.description = data['description']
        db.session.commit()
        return jsonify(todo.to_dict())
    else:
        return jsonify({'error': 'Todo not found'}), 404

def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({'message': 'Todo deleted successfully'})
    else:
        return jsonify({'error': 'Todo not found'}), 404