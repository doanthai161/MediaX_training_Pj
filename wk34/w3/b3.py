import mysql.connector

# class PermissionManager:
#     def __init__(self, host, user, password, database):
#         self.connection = mysql.connector.connect(
#             host=host,
#             user=user,
#             passwd=password,
#             database=database
#         )
#         self.cursor = self.connection.cursor()
class PermissionManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="Th@idaica123",
            database="mor_db"
        )
        self.cursor = self.connection.cursor()


    # Thêm quyền
    def add_permission(self, name, description):
        sql = "INSERT INTO mor_permission (name, description) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, description))
        self.connection.commit()

    # Sửa quyền
    def edit_permission_name(self, permission_id, new_name, new_description=None):
        sql = "UPDATE mor_permission SET name = %s, description = %s WHERE id = %s"
        self.cursor.execute(sql, (new_name, new_description, permission_id))
        self.connection.commit()

    # Xóa quyền
    def delete_permission(self, permission_id):
        sql = "DELETE FROM mor_permission WHERE id = %s"
        self.cursor.execute(sql, (permission_id,))
        self.connection.commit()

    # Phương thức lấy danh sách quyền
    def get_permissions(self):
        sql = "SELECT id, name, description FROM mor_permission"
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # Trả về tất cả các quyền dưới dạng danh sách

    # Đóng kết nối
    def close(self):
        self.cursor.close()
        self.connection.close()
