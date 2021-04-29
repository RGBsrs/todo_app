from datetime import timedelta, datetime
from functools import wraps
import jwt

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.security import check_password_hash
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from src import db, app
from src.schemas.users import UserSchema
from src.database.models import User
from src.services.user_service import UserService


class LoginApi(MethodView):
    user_sсhema = UserSchema()

    def post(self):
        auth = request.form

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
        print(auth.get('password',''))
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


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = UserService.fetch_user_by_id(db.session, data['id'])
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f( *args, **kwargs)

    return decorated