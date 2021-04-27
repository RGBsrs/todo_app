from src.database.models import Todo


class TodoService:
    @staticmethod
    def fetch_all_todos(session):
        return session.query(Todo)

    @classmethod
    def fetch_todo_by_uuid(cls, session, uuid):
        return cls.fetch_all_todos(session).filter_by(uuid = uuid).first()