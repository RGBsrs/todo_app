from src.database.models import Todo


class TodoService():
    @staticmethod
    def fetch_all_todos(session):
        return session.query(Todo)

    @classmethod
    def fetch_user_todos(cls, session, user_id):
        return cls.fetch_all_todos(session).filter_by(user_id = user_id).all()

    @classmethod
    def fetch_todo_by_id(cls, session, user_id, id):
        return cls.fetch_all_todos(session).filter_by(user_id = user_id, id = id).first()
    
    @classmethod
    def delete_completed_todos(cls, session, user_id):
        cls.fetch_all_todos(session).filter_by(user_id = user_id, completed = True).delete()
        session.commit()

    @classmethod
    def bulk_check_todos(cls, session, user_id, completed):
        todos = cls.fetch_all_todos(session).filter_by(user_id = user_id).all()
        mapper = []
        for todo in todos:
            mapper.append(dict(id = todo.id, title=todo.title, completed = completed))
        session.bulk_update_mappings(Todo, mapper)
        session.commit()