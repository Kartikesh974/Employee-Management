import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pass",
    database="employee_db"
)

cursor = conn.cursor()

def add_employee(name, age, department, salary):
    sql = "INSERT INTO employees (name, age, department, salary) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, age, department, salary))
    conn.commit()
    print("Employee added successfully.")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_employee(emp_id, name, age, department, salary):
    sql = "UPDATE employees SET name=%s, age=%s, department=%s, salary=%s WHERE id=%s"
    cursor.execute(sql, (name, age, department, salary, emp_id))
    conn.commit()
    print("Employee updated.")

def delete_employee(emp_id):
    sql = "DELETE FROM employees WHERE id=%s"
    cursor.execute(sql, (emp_id,))
    conn.commit()
    print("Employee deleted.")

def search_employee(emp_id):
    sql = "SELECT * FROM employees WHERE id=%s"
    cursor.execute(sql, (emp_id,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("Employee not found.")

# Sample CLI
while True:
    print("\n1. Add\n2. View\n3. Update\n4. Delete\n5. Search\n6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        age = int(input("Age: "))
        dept = input("Department: ")
        salary = float(input("Salary: "))
        add_employee(name, age, dept, salary)

    elif choice == '2':
        view_employees()

    elif choice == '3':
        eid = int(input("Employee ID to update: "))
        name = input("New Name: ")
        age = int(input("New Age: "))
        dept = input("New Department: ")
        salary = float(input("New Salary: "))
        update_employee(eid, name, age, dept, salary)

    elif choice == '4':
        eid = int(input("Employee ID to delete: "))
        delete_employee(eid)

    elif choice == '5':
        eid = int(input("Employee ID to search: "))
        search_employee(eid)

    elif choice == '6':
        break

    else:
        print("Invalid choice")
