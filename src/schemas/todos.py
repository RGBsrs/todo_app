from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.database.models import Todo


class TodoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        exclude = ['created_at', 'updated_at']
        load_instance = True