import mysql.connector

class RoleManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host, 
            user=user,
            password=password, 
            database=database
        )
        self.cursor = self.connection.cursor()#used control 'self.cursor' connect to database

    def add_role(self, name, description):
        sql = "INSERT INTO mor_role (name, description) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, description)) #query to SQL
        self.connection.commit() #confirm changes

    def edit_role(self, role_id, new_name, new_description):
        sql = "UPDATE mor_role SET name = %s, description = %s WHERE id = %s"
        self.cursor.execute(sql, (new_name, new_description, role_id))
        self.connection.commit()

    def delete_role(self, role_id):
        sql = "DELETE FROM mor_role WHERE id = %s"
        self.cursor.execute(sql, (role_id,))
        self.connection.commit()

    def get_roles(self):
        sql = "SELECT id, name FROM mor_role"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
    
    def get_role_by_id(self, role_id):
        query = "SELECT * FROM mor_role WHERE id = %s"
        self.cursor.execute(query, (role_id,))
        return self.cursor.fetchone()
