from src.database.models import Todo


class TodoService:
    @staticmethod
    def fetch_all_todos(session):
        return session.query(Todo)

    @classmethod
    def fetch_todo_by_id(cls, session, id):
        return cls.fetch_all_todos(session).filter_by(id = id).first()
    
    @classmethod
    def delete_completed_todos(cls, session):
        cls.fetch_all_todos(session).filter_by(completed = True).delete()
        session.commit()

    @classmethod
    def bulk_check_todos(cls, session, completed):
        todos = cls.fetch_all_todos(session).filter(completed != completed).all()
        mapper = []
        for todo in todos:
            mapper.append(dict(id =todo.id, title=todo.title, completed = completed))

        session.bulk_update_mappings(Todo, mapper)
        session.commit()