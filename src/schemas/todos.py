from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from src.database.models import Todo


class TodoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        exclude = ['id']