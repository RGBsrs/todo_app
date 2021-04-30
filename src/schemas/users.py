from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from src.database.models import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('remember_token', 'created_at')
        load_instance = True
        #include_fk = True
        todos = Nested('TodoSchema', many = True, exclude = ('updated_at','created_at',))