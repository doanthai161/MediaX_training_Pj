def read_employee_data(file_path):
    employees = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            employee_id = int(data[0])
            name = data[1].strip()
            rate = int(data[2])
            employees[employee_id] = {'name': name, 'rate': rate}
    return employees

def calculate_salary(employee_id, employees, standard_salary, days_off):
    if employee_id in employees:
        rate = employees[employee_id]['rate']
        salary_vnd = standard_salary * rate * (days_off / 30)
        salary_usd = salary_vnd / 23000 
        return rate, salary_vnd, salary_usd
    else:
        return None

def write_salary_to_file(file_path, employee_id, employees, rate, salary_vnd, salary_usd, days_off):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Mã nhân viên: {employee_id}\n")
        file.write(f"Tên nhân viên: {employees[employee_id]['name']}\n")
        file.write(f"Rate: {rate}\n")
        file.write(f"Số ngày nghỉ: {days_off}\n")  
        file.write(f"Lương (VNĐ): {salary_vnd:.2f}\n")
        file.write(f"Lương (USD): {salary_usd:.2f}\n")

def main():
    file_path = 'employee_rate.txt'  
    output_file_path = 'salary.txt'  
    standard_salary = 10000000 
    employees = read_employee_data(file_path)

    employee_id = int(input("Nhập mã nhân viên cần tính lương: "))
    
    days_off = int(input("Nhập số ngày nghỉ: "))
    
    result = calculate_salary(employee_id, employees, standard_salary, days_off)
    
    if result is not None:
        rate, salary_vnd, salary_usd = result
        write_salary_to_file(output_file_path, employee_id, employees, rate, salary_vnd, salary_usd, days_off)
        print(f"Kết quả ở :{output_file_path}.")
    else:
        print("Mã nhân viên không tồn tại.")

if __name__ == "__main__":
    main()

