import mysql.connector

class UserManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host, 
            user=user,
            password=password, 
            database=database
        )
        self.cursor = self.connection.cursor()

    def add_user(self, username, password):
        sql = "INSERT INTO mor_user (username, password) VALUES (%s, %s)"
        self.cursor.execute(sql, (username, password))
        self.connection.commit()

    def edit_user(self, user_id, new_username, new_password):
        sql = "UPDATE mor_user SET username = %s, password = %s WHERE id = %s"
        self.cursor.execute(sql, (new_username, new_password, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        sql = "DELETE FROM mor_user WHERE id = %s"
        self.cursor.execute(sql, (user_id,))
        self.connection.commit()

    def get_users(self):
        sql = "SELECT id, username FROM mor_user"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #close connection
    def close(self):
        self.cursor.close()
        self.connection.close()
    
    def get_user_by_id(self, user_id):
        query = "SELECT * FROM mor_user WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()
    
    