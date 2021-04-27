from src import app
from src.resources.smoke import Smoke
from src.resources.todo import TodoListApi


smoke_api = Smoke.as_view('smoke')
app.add_url_rule('/smoke', view_func=smoke_api, strict_slashes = False)

todo_list_api = TodoListApi.as_view('todo')
app.add_url_rule('/', view_func=todo_list_api, strict_slashes = False)

