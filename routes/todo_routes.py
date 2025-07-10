from flask import Blueprint

from controllers import todo_controller

todo_bluprint = Blueprint('todo', __name__)

todo_bluprint.route('/todos', methods=['GET'])(todo_controller.get_todos)
todo_bluprint.route('/todos/<int:todo_id>', methods=['GET'])(todo_controller.get_todo)
todo_bluprint.route('/todos', methods=['POST'])(todo_controller.create_todo)
todo_bluprint.route('/todos/<int:todo_id>', methods=['PUT'])(todo_controller.update_todo)
todo_bluprint.route('/todos/<int:todo_id>', methods=['DELETE'])(todo_controller.delete_todo)
