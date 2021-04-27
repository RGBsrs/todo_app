from flask.views import MethodView


class TodoListApi(MethodView):
    def get(self):
        return {'todo': 'OK'}