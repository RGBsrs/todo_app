from copy import Error
import datetime
from flask import jsonify, request
from flask.views import MethodView
from marshmallow import ValidationError

from src import db
from src.database.models import Todo
from src.schemas.users import UserSchema
from src.schemas.todos import TodoSchema
from src.services.user_service import UserService
from src.services.todo_service import TodoService
from src.services.auth_service import token_required


class UserTodoListApi(MethodView):
    user_sсhema = UserSchema()
    todo_schema = TodoSchema()

    @token_required
    def get(self, user_id):
        user = UserService.fetch_user_by_id(db.session, user_id)
        todos = user.todos
        if not todos:
            return '', 404
        return jsonify(self.todo_schema.dump(todos, many= True)), 200

    @token_required
    def post(self, user_id):
        user = UserService.fetch_user_by_id(db.session, user_id)
        try:
            todo = Todo(title = request.json['title'])
            user.todos.append(todo)
        except Error as e:
            return {'Message': f'error: {e}'}, 400
        db.session.add(user)
        db.session.commit()
        return jsonify(self.todo_schema.dump(todo)), 201

    @token_required
    def patch(self, user_id, id = None):
        if not id:
            completed = request.json['completed']
            TodoService.bulk_check_todos(db.session,user_id, completed)
            return 'updated',200

        todo = TodoService.fetch_todo_by_id(db.session, user_id, id)
        if not todo:
            return '', 404
        try:
            todo = self.todo_schema.load(request.json, instance = todo, session = db.session,
                partial = True )
            todo.updated_at = datetime.datetime.now()
        except ValidationError as e:
            return {'Message': f'error: {e}'}, 400
        db.session.add(todo)
        db.session.commit()    
        return jsonify(self.todo_schema.dump(todo)), 200

    @token_required
    def delete(self, user_id, id = None):
        if not id:
            TodoService.delete_completed_todos(db.session, user_id)
            return '', 204
        todo = TodoService.fetch_todo_by_id(db.session,user_id, id)
        if not todo:
            return '', 404
        db.session.delete(todo)
        db.session.commit()
        return '', 204