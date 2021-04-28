from src.database.models import Todo


class TodoService:
    @staticmethod
    def fetch_all_todos(session):
        return session.query(Todo)

    @classmethod
    def fetch_todo_by_id(cls, session, id):
        return cls.fetch_all_todos(session).filter_by(id = id).first()

    @staticmethod
    def bulk_complete_todos(cls,session):
        todos_to_update = cls.fetch_all_todos(session).filter_by(completed = False).all()
        for todo in todos_to_update:
            todo.completed = True

        session.bulk_update_mappings(todos_to_update)
        session.commit()