"""
Использовать существующую базу данных с продуктами и заказами.

    Создать новую базу данных руками
    Создать таблицу users с полями (id, name, email, age)
    Создать класс для работы с таблицей users
    Создать метод для селекта всех пользователей
    Создать метод для удаления пользователя по имейлу
    Создать метод для модификации пользователя по id
    Создать метод для добавления пользователя
Все методы должны быть реализованы через SqlAlchemy
"""
from sqlalchemy import text

from homework_23.config.session import session
from homework_23.models.users_model import Users


class UsersRepository:
    def __init__(self):
        self.__session = session

    def get_all(self):
        result = self.__session.execute(text("select * from users;"))
        for row in result:
            print(row)

    def delete_user_by_email(self, email: str):
        result = self.__session.query(Users).filter_by(email=email).first()
        self.__session.delete(result)
        self.__session.commit()

    def insert_user(self, user: Users):
        self.__session.add(user)
        self.__session.commit()

    def modification_user_by_id(self, id: int, new_name: str, new_email: str, new_age: int):
        result = self.__session.query(Users).get(id)
        result.name = new_name
        result.email = new_email
        result.age = new_age
        self.__session.commit()


if __name__ == '__main__':
    users_repository = UsersRepository()
    users_repository.get_all()
    users_repository.modification_user_by_id(1, "James", "james@gmail.com", 22)
    users_repository.insert_user(Users(id=2, name="Max", email="max@gmail.com", age=24))
    users_repository.delete_user_by_email("max@gmail.com")
