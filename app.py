from flask import Flask, jsonify, request
from flask_cors import CORS
from config.config import Config
from routes.todo_routes import todo_bluprint
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(todo_bluprint)
    
    @app.route('/health')
    def health_check():
        return jsonify({
            'status': 'OK',
            "message": "Server is up and running"
            }), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
