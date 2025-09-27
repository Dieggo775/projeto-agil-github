from flask import Flask, request, jsonify
from src.models import db, Task

def create_app(database_uri="sqlite:///tasks.db"):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.before_first_request
    def init_db():
        db.create_all()

    @app.route("/tasks", methods=["GET"])
    def list_tasks():
        tasks = Task.query.all()
        return jsonify([t.to_dict() for t in tasks])

    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.get_json() or {}
        title = data.get("title")
        if not title:
            return jsonify({"error": "title é obrigatório"}), 400
        t = Task(title=title, description=data.get("description",""), status=data.get("status","todo"), priority=data.get("priority","medium"))
        db.session.add(t)
        db.session.commit()
        return jsonify(t.to_dict()), 201

    @app.route("/tasks/<int:tid>", methods=["GET","PUT","DELETE"])
    def task_ops(tid):
        t = Task.query.get_or_404(tid)
        if request.method == "GET":
            return jsonify(t.to_dict())
        if request.method == "PUT":
            data = request.get_json() or {}
            t.title = data.get("title", t.title)
            t.description = data.get("description", t.description)
            t.status = data.get("status", t.status)
            t.priority = data.get("priority", t.priority)
            db.session.commit()
            return jsonify(t.to_dict())
        if request.method == "DELETE":
            db.session.delete(t)
            db.session.commit()
            return jsonify({"result":"deleted"})

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
