from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.database.models import Todo


class TodoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        exclude = ['id']
        load_instance = True