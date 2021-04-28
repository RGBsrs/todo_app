from src import app
from src.resources.todos import TodoListApi


todo_list_api = TodoListApi.as_view('todos')
app.add_url_rule('/api/v1/todos', view_func=todo_list_api, strict_slashes = False)
app.add_url_rule('/api/v1/todos/<id>', view_func=todo_list_api, strict_slashes = False)

