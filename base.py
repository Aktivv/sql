import sqlite3

with sqlite3.connect('person.db') as conn:
    per = conn.cursor()
    per.execute(''' 
    CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DepartmentID INTEGER)
    ''')

    per.execute('''
    CREATE TABLE IF NOT EXISTS Departments  (
    DepartmentID INTEGER,
    DepartmentName TEXT NOT NULL,
    FOREIGN KEY (DepartmentID) REFERENCES Employees (DepartmentID))
    ''')

    # per.execute('''
    # INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (101, 'HR'),
    # (102, 'IT'), (103, 'Sales')
    # ''')
    #
    # per.execute('''
    # INSERT INTO Employees (FirstName, LastName, DepartmentID) VALUES
    # ('Argen','Bey',101),
    # ('Almaz','Alayev',103),
    # ('Almagul','Aliyeva',102),
    # ('Beka','Bekbaev',103),
    # ('Ars','Belekov',101),
    # ('Aygul','Saliyeva',102)
    # ''')

    # per.execute('''
    # ALTER TABLE Departments RENAME COLUMN DepartmentID TO Department_ID
    # ''')

    per.execute('''
    SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
    FROM Employees
    JOIN Departments ON Department_ID = Departments.Department_ID
    ''')
    stop = 0
    for i in per.fetchall():
        print(i)
        stop += 1
        if stop == 6:
            break

    # per.execute('''SELECT * FROM Employees''')
    # for row in per.fetchall():
    #     print(row)
    #
    # per.execute('''SELECT * FROM Departments''')
    # for row in per.fetchall():
    #     print(row)


