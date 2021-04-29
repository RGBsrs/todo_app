from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.database.models import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('remember_token', 'created_at')
        load_instance = True
        load_only = ('password',)