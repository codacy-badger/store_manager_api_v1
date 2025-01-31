from flasky.database.postgres import db


class UserController:

    # Controller class for handling and storing user data
    @classmethod
    def create_user(cls, user):
        values = (user.user_id, user.username,
                  user.role, user.email, user.password_hash)
        query = "INSERT INTO users (user_id, username, role, email, password) VALUES\
        (%s, %s, %s, %s, %s)"
        values = (user.user_id, user.username,
                  user.role, user.email, user.password_hash)
        db.insert(query, values)

    @classmethod
    def check_if_user_exists(cls, email):
        query = "SELECT * FROM users WHERE email = '{}'".format(email)
        return db.fetch_one(query)

    @classmethod
    def fetch_user_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE user_id = '{}'".format(user_id)
        return db.fetch_one(query)
