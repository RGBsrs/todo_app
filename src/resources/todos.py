from flask import jsonify
from flask.views import MethodView

from src import db
from src.database.models import Todo
from src.schemas.todos import TodoSchema
from src.services.todo_service import TodoService


class TodoListApi(MethodView):
    todo_shema = TodoSchema()
    def get(self):
        todos = TodoService.fetch_all_todos(db.session).all()
        return jsonify(self.todo_shema.dump(todos, many=True)),200