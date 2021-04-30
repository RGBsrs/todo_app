from datetime import timedelta, datetime
import jwt

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.security import check_password_hash
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from src import db, app
from src.schemas.users import UserSchema
from src.services.user_service import UserService
from src.services.auth_service import token_required

class LoginApi(MethodView):
    
    def post(self):
        auth = request.json
        if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
            return ('Could not verify',
                    401,
                    {'WWW-Authenticate' : 'Basic realm ="Login required !!"'})

        user = UserService.fetch_user_by_email(db.session, auth.get('email'))
        if not user:
            # returns 401 if user does not exist
            return ('Could not verify',
                    401,
                    {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'})
        if check_password_hash(user.password, auth.get('password','')):
        # generates the JWT Token
            token = jwt.encode({
            'id': user.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
            }, app.config['SECRET_KEY'])

            return jsonify({'token' : token}), 201
        # returns 403 if password is wrong
        return ('Could not verify',
                403,
                {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'})


class LogoutApi(MethodView):
    
    @token_required
    def post(self):
        return {'message' : 'logged out'}, 200

class RegisterApi(MethodView):
    user_sсhema = UserSchema()

    def post(self):
        try:
            user = self.user_sсhema.load(request.json, session = db.session)
        except ValidationError as e:
            return {'Message' : f'Error : {e}'}
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            return {'Message' : 'Such user exists'}, 409
        return jsonify(self.user_sсhema.dump(user)), 201


