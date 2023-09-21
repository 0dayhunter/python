class Employee:
    def __init__(self, name, eid, dept, sal):
        self.name = name
        self.eid = eid
        self.dept = dept
        self.sal = sal

if __name__ == "__main__":
    emp = []

    while True:
        print("\n1. Create Employee")
        print("2. Display All Employees")
        print("3. Update Employee Salary")
        print("4. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            n = input("Employee Name: ")
            i = int(input("Employee ID: "))
            d = input("Employee Department: ")
            s = int(input("Employee Salary: "))
            emp.append(Employee(n, i, d, s))
            print("Employee details created. Total employees:", len(emp))

        elif ch == 2:
            for i in emp:
                print("\nEmployee Name:", i.name)
                print("Employee ID:", i.eid)
                print("Employee Department:", i.dept)
                print("Employee Salary:", i.sal)

        elif ch == 3:
            eid = int(input("Enter Employee ID to update salary: "))
            for i in emp:
                if i.eid == eid:
                    new_sal = int(input("Enter new salary: "))
                    i.sal = new_sal
                    print("Salary updated for Employee ID", eid)
                    break
            else:
                print("Employee with ID", eid, "not found")

        elif ch == 4:
            break

        else:
            print("Invalid choice")
