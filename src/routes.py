from src import app
from src.resources.smoke import Smoke


smoke_api = Smoke.as_view('smoke')
app.add_url_rule('/smoke', view_func=smoke_api, strict_slashes = False)

# film_list_api = FilmListApi.as_view('films')
# app.add_url_rule('/films', view_func=film_list_api, strict_slashes = False)
# app.add_url_rule('/films/<uuid>', view_func=film_list_api, strict_slashes = False)
