import tkinter as tk
from tkinter import messagebox, ttk
from user_manager import UserManager
from role_manager import RoleManager

#connect to database
#u just need to fill in the information here n dont need to change samethings in the 2 files role_ma and user_ma
db_host = 'host'
db_user = 'root'
db_password = 'password'
db_name = 'database_name'

user_manager = UserManager(host=db_host, user=db_user, password=db_password, database=db_name)
role_manager = RoleManager(host=db_host, user=db_user, password=db_password, database=db_name)

def refresh_users():

    for i in user_tree.get_children():
        user_tree.delete(i)
    
    users = user_manager.get_users()
    for user in users:
        user_tree.insert('', 'end', values=(user[0], user[1]))

def refresh_roles():
    for i in role_tree.get_children():
        role_tree.delete(i)
    
    roles = role_manager.get_roles()
    for role in roles:
        role_tree.insert('', 'end', values=(role[0], role[1]))

#check input user
def validate_user_input(username, password):
    if not username or not password:
        messagebox.showwarning("Lỗi nhập! ", "User_name and password không được để trống.")
        return False
    return True

def add_user():
    username = entry_username.get()
    password = entry_password.get()
    if validate_user_input(username, password):
        user_manager.add_user(username, password)
        refresh_users()
        messagebox.showinfo("successfully.")

def edit_user():
    selected_item = user_tree.selection()
    if selected_item:
        user_id = user_tree.item(selected_item)['values'][0]
        new_username = entry_username.get()
        new_password = entry_password.get()
        if validate_user_input(new_username, new_password):
            user_manager.edit_user(user_id, new_username, new_password)
            refresh_users()
            messagebox.showinfo("Người dùng đã được sửa!")
    else:
        messagebox.showwarning("chọn người dùng cần sửa")

def delete_user():
    selected_item = user_tree.selection()
    if selected_item:
        user_id = user_tree.item(selected_item)['values'][0]
        user_manager.delete_user(user_id)
        refresh_users()
        messagebox.showinfo("Người dùng đã được xóa!")

#CRUD user
def on_user_double_click(event):
    selected_item = user_tree.selection()
    if selected_item:
        user_id = user_tree.item(selected_item)['values'][0]
        user_info = user_manager.get_user_by_id(user_id)
        if user_info:
            entry_username.delete(0, tk.END)
            entry_username.insert(0, user_info[1])
            entry_password.delete(0, tk.END)
            entry_password.insert(0, user_info[2])
            entry_password.config(show='')  #hiện mật khẩu

def add_role():
    name = entry_role_name.get()
    description = entry_role_description.get()
    if name:
        role_manager.add_role(name, description)
        refresh_roles()
        messagebox.showinfo("Vai trò đã được thêm ")
    else:
        messagebox.showwarning("Tên vai trò không được để trống")

def edit_role():
    selected_item = role_tree.selection()
    if selected_item:
        role_id = role_tree.item(selected_item)['values'][0]
        new_name = entry_role_name.get()
        new_description = entry_role_description.get()
        if new_name:
            role_manager.edit_role(role_id, new_name, new_description)
            refresh_roles()
            messagebox.showinfo("Vai trò đã được sửa")
    else:
        messagebox.showwarning("Vui lòng chọn vai trò cần sửa.")

def delete_role():
    selected_item = role_tree.selection()
    if selected_item:
        role_id = role_tree.item(selected_item)['values'][0]
        role_manager.delete_role(role_id)
        refresh_roles()
        messagebox.showinfo("Vai trò đã được xóa!")

def on_role_double_click(event):
    selected_item = role_tree.selection()
    if selected_item:
        role_id = role_tree.item(selected_item)['values'][0]
        role_info = role_manager.get_role_by_id(role_id)
        if role_info:
            entry_role_name.delete(0, tk.END)
            entry_role_name.insert(0, role_info[1])
            entry_role_description.delete(0, tk.END)
            entry_role_description.insert(0, role_info[2])

#4 Tkinter
root = tk.Tk()
root.title("Quản lý Người Dùng và Vai Trò")

# Khung cho người dùng
user_frame = tk.Frame(root)
user_frame.grid(pady=10, padx=10)

label_username = tk.Label(user_frame, text="Tên đăng nhập:")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(user_frame)
entry_username.grid(row=0, column=1)

label_password = tk.Label(user_frame, text="Mật khẩu:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(user_frame, show='*')  #hide password
entry_password.grid(row=1, column=1)

btn_add_user = tk.Button(user_frame, text="Thêm Người Dùng", command=add_user)
btn_add_user.grid(row=2, column=0)

btn_edit_user = tk.Button(user_frame, text="Sửa Người Dùng", command=edit_user)
btn_edit_user.grid(row=2, column=1)

btn_delete_user = tk.Button(user_frame, text="Xóa Người Dùng", command=delete_user)
btn_delete_user.grid(row=2, column=2)

#user list
user_tree = ttk.Treeview(root, columns=("ID", "Tên đăng nhập"), show="headings")
user_tree.heading("ID", text="ID")
user_tree.heading("Tên đăng nhập", text="Tên đăng nhập")
user_tree.grid(row=1, column=0, pady=(10, 0), padx=10)

# Thêm sự kiện nhấp đúp vào Treeview
user_tree.bind("<Double-1>", on_user_double_click)

refresh_users()

# Khung cho vai trò
role_frame = tk.Frame(root)
role_frame.grid(pady=10, padx=10)

label_role_name = tk.Label(role_frame, text="Tên vai trò:")
label_role_name.grid(row=0, column=0)
entry_role_name = tk.Entry(role_frame)
entry_role_name.grid(row=0, column=1)

label_role_description = tk.Label(role_frame, text="Mô tả vai trò:")
label_role_description.grid(row=1, column=0)
entry_role_description = tk.Entry(role_frame)
entry_role_description.grid(row=1, column=1)

btn_add_role = tk.Button(role_frame, text="Thêm Vai Trò", command=add_role)
btn_add_role.grid(row=2, column=0)

btn_edit_role = tk.Button(role_frame, text="Sửa Vai Trò", command=edit_role)
btn_edit_role.grid(row=2, column=1)

btn_delete_role = tk.Button(role_frame, text="Xóa Vai Trò", command=delete_role)
btn_delete_role.grid(row=2, column=2)

#role list
role_tree = ttk.Treeview(root, columns=("ID", "Tên vai trò"), show="headings")
role_tree.heading("ID", text="ID")
role_tree.heading("Tên vai trò", text="Tên vai trò")
role_tree.grid(row=3, column=0, pady=(10, 0), padx=10)

#Thêm sự kiện nhấp đúp vào Treeview
role_tree.bind("<Double-1>", on_role_double_click)

refresh_roles()

root.mainloop()

#close connection
user_manager.close()
role_manager.close()
