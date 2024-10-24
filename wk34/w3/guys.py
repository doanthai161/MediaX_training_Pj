import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  #use Treeview
from b3 import PermissionManager
import mysql.connector


try:
    pm = PermissionManager(host='127.0.0.1', user='root', password='Th@idaica123', database='mor_db')
except mysql.connector.Error as err:
    messagebox.showerror("Lỗi kết nối", f"Không thể kết nối cơ sở dữ liệu: {err}")
    exit()

def refresh_permissions():
    """Làm mới danh sách quyền, hiển thị các quyền đã nhập từ cơ sở dữ liệu"""
    for i in tree.get_children():  # Xóa danh sách hiện tại
        tree.delete(i)
    
    permissions = pm.get_permissions()  # Lấy danh sách quyền từ cơ sở dữ liệu
    for permission in permissions:
        tree.insert('', 'end', values=(permission[0], permission[1], permission[2]))  # Thêm vào bảng

def add_permission():
    """Thêm quyền mới vào cơ sở dữ liệu"""
    name = entry_name.get()
    description = entry_description.get()
    if name:
        pm.add_permission(name, description)
        refresh_permissions()  # Làm mới danh sách sau khi thêm
        messagebox.showinfo("Thành công", "Quyền đã được thêm!")
    else:
        messagebox.showwarning("Lỗi nhập liệu", "Tên quyền không được để trống.")

def edit_permission():
    """Sửa quyền đã chọn trong danh sách"""
    selected_item = tree.selection()
    if selected_item:
        permission_id = tree.item(selected_item)['values'][0]  # Lấy ID của quyền được chọn
        new_name = entry_name.get()
        new_description = entry_description.get()
        if new_name:
            pm.edit_permission_name(permission_id, new_name, new_description)
            refresh_permissions()  # Làm mới danh sách sau khi sửa
            messagebox.showinfo("Thành công", "Quyền đã được sửa!")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Tên quyền không được để trống.")
    else:
        messagebox.showwarning("Lỗi lựa chọn", "Vui lòng chọn quyền cần sửa.")

def delete_permission():
    """Xóa quyền đã chọn trong danh sách"""
    selected_item = tree.selection()
    if selected_item:
        permission_id = tree.item(selected_item)['values'][0]  # Lấy ID của quyền được chọn
        pm.delete_permission(permission_id)
        refresh_permissions()  # Làm mới danh sách sau khi xóa
        messagebox.showinfo("Thành công", "Quyền đã được xóa!")
    else:
        messagebox.showwarning("Lỗi lựa chọn", "Vui lòng chọn quyền cần xóa.")

root = tk.Tk()
root.title("Quản lý quyền")

# Giao diện nhập liệu
label_name = tk.Label(root, text="Tên quyền:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_description = tk.Label(root, text="Mô tả quyền:")
label_description.grid(row=1, column=0)
entry_description = tk.Entry(root)
entry_description.grid(row=1, column=1)

#button (Thêm, Sửa, Xóa)
btn_add = tk.Button(root, text="Thêm quyền", command=add_permission)
btn_add.grid(row=2, column=0)

btn_edit = tk.Button(root, text="Sửa quyền", command=edit_permission)
btn_edit.grid(row=2, column=1)

btn_delete = tk.Button(root, text="Xóa quyền", command=delete_permission)
btn_delete.grid(row=2, column=2)

# Danh sách quyền đã nhập
tree = ttk.Treeview(root, columns=("ID", "Tên quyền", "Mô tả"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Tên quyền", text="Tên quyền")
tree.heading("Mô tả", text="Mô tả")

# Đặt chiều rộng cho các cột
tree.column("ID", width=50)
tree.column("Tên quyền", width=150)
tree.column("Mô tả", width=250)

tree.grid(row=3, column=0, columnspan=3)

# Làm mới danh sách quyền khi khởi động ứng dụng
refresh_permissions()

# Chạy giao diện Tkinter
root.mainloop()

# Đóng kết nối với cơ sở dữ liệu khi đóng giao diện
pm.close()
