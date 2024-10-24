# permission_manager.py

import mysql.connector

class PermissionManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def add_permission(self, name, description):
        sql = "INSERT INTO mor_permission (name, description) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, description))
        self.connection.commit()

    def edit_permission_name(self, permission_id, new_name, new_description=None):
        sql = "UPDATE mor_permission SET name = %s, description = %s WHERE id = %s"
        self.cursor.execute(sql, (new_name, new_description, permission_id))
        self.connection.commit()

    def delete_permission(self, permission_id):
        sql = "DELETE FROM mor_permission WHERE id = %s"
        self.cursor.execute(sql, (permission_id,))
        self.connection.commit()

    def get_permissions(self):
        sql = "SELECT id, name, description FROM mor_permission"
        self.cursor.execute(sql)
        return self.cursor.fetchall()  

    def close(self):
        self.cursor.close()
        self.connection.close()
