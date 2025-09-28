from flask import Flask, jsonify, request
from .models import db, Task

def create_app(testing=False):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' if testing else 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.get_json()
        new_task = Task(
            title=data.get("title"),
            description=data.get("description"),
            priority=data.get("priority", 1)
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201

    @app.route("/tasks", methods=["GET"])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks]), 200

    @app.route("/tasks/<int:task_id>", methods=["PUT"])
    def update_task(task_id):
        task = db.session.get(Task, task_id)
        if not task:
            return jsonify({"error": "Task não encontrada"}), 404
        data = request.get_json()
        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.priority = data.get("priority", task.priority)
        task.done = data.get("done", task.done)
        db.session.commit()
        return jsonify(task.to_dict()), 200

    @app.route("/tasks/<int:task_id>", methods=["DELETE"])
    def delete_task(task_id):
        task = db.session.get(Task, task_id)
        if not task:
            return jsonify({"error": "Task não encontrada"}), 404
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deletada com sucesso"}), 200

    return app
