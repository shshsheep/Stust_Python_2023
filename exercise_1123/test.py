class MyShape:
    def __init__(self,name ,id, salary ,department):
        self.id = id 
        self.name = name 
        self.salary = salary 
        self.departmeant = department 
    
    def calculate_salary(self,hour_works): #計算超時工作
        if hour_works > 50 :
            overtime = hour_works - 50
            overtime_amount = (overtime*(self.salary/50))
            total_salary = self.salary + overtime_amount
            return total_salary
        else :
            return self.salary
    
    def assign_department(self,new_department): #給予新職位
        self.departmeant = new_department
        
    def print_employee_details(self): #輸出答案
        print("Employee 's id :", self.id)
        print("Employee 's name :", self.name)
        print("Employee 's salary :", self.salary)
        print("Employee 's department :", self.departmeant)

sample_id1 = MyShape("ADAMS", "E7876", 50000, "ACCOUNTING")
sample_id2 = MyShape("JONES", "E7499", 45000, "RESEARCH")
sample_id3 = MyShape("MARTIN", "E7900", 50000, "SALES")
sample_id4 = MyShape("SMITH", "E7698", 55000, "OPERATIONS")

sample_id1.assign_department("Chef")

sample_id1.print_employee_details()

print("Salary after 'overtime' for employee : ", sample_id1.calculate_salary(100))