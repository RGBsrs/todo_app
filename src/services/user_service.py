from src.database.models import User


class UserService():
    @staticmethod
    def fetch_all_users(session):
        return session.query(User)

    @classmethod
    def fetch_user_by_id(cls, session, id):
        return cls.fetch_all_users(session).filter_by(id = id).first()

    @classmethod
    def fetch_user_by_email(cls, session, email):
        return cls.fetch_all_users(session).filter_by(email = email).first()

