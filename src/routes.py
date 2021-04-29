from src import app
from src.resources.todos import TodoListApi
from src.resources.auth import LoginApi, RegisterApi


todo_list_api = TodoListApi.as_view('todos')
app.add_url_rule('/api/v1/todos', view_func=todo_list_api, strict_slashes = False)
app.add_url_rule('/api/v1/todos/<id>', view_func=todo_list_api, strict_slashes = False)


login_api = LoginApi.as_view('login')
app.add_url_rule('/api/v1/login', view_func=login_api, strict_slashes = False)


register_api = RegisterApi.as_view('register')
app.add_url_rule('/api/v1/register', view_func=register_api, strict_slashes = False)

