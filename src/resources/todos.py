import datetime
from flask import jsonify, request
from flask.views import MethodView
from marshmallow import ValidationError

from src import db
from src.schemas.todos import TodoSchema
from src.services.todo_service import TodoService


class TodoListApi(MethodView):
    todo_shema = TodoSchema()
    def get(self):
        todos = TodoService.fetch_all_todos(db.session).all()
        if not todos:
            return '', 404
        return jsonify(self.todo_shema.dump(todos, many=True)), 200

    def post(self):
        try:
            todo = self.todo_shema.load(request.json, session = db.session)
        except ValidationError as e:
            return {'Message': f'error: {e}'}, 400
        db.session.add(todo)
        db.session.commit()
        return jsonify(self.todo_shema.dump(todo)), 201

    def patch(self, id = None):
        if not id:
            completed = request.json['completed']
            TodoService.bulk_check_todos(db.session, completed)
            return 'updated',200

        todo = TodoService.fetch_todo_by_id(db.session, id)
        if not todo:
            return '', 404
        try:
            todo = self.todo_shema.load(request.json, instance = todo, session = db.session,
                partial = True )
            todo.updated_at = datetime.datetime.now()
        except ValidationError as e:
            return {'Message': f'error: {e}'}, 400
        db.session.add(todo)
        db.session.commit()    
        return jsonify(self.todo_shema.dump(todo)), 200


    def delete(self, id = None):
        if not id:
            TodoService.delete_completed_todos(db.session)
            return '', 204
        todo = TodoService.fetch_todo_by_id(db.session, id)
        if not todo:
            return '', 404
        db.session.delete(todo)
        db.session.commit()
        return '', 204