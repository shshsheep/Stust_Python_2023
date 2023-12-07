class student :
     # Class-level variables for school name and address
    school_name = "STUST"
    school_address = "No. 1, Nantai Street, Yongkang District, Tainan City, Taiwan"

    def __init__(self,department,departmentBoss,name,id,grade,address,credits,GPA) :
        # Instance-level variables
        self._department = department
        self._departmentBoss = departmentBoss
        self.name = name
        self.id = id 
        self.grade = grade
        self.address = address
        self.credits = credits
        self.GPA = GPA
    
    def print_details(self):
         # Print student details, including school name and address
        print("school name : ",self.school_name)
        print("school address : ",self.school_address)
        print("deparment : ",self._department)
        print("department Boss :", self._departmentBoss)
        print("student name : ", self.name)
        print("student id : ",self.id )
        print("student grade : ",self.grade)
        print("student address : ",self.address)
        print("student credits : ", self.credits)
        print("student GPA : ",self.GPA)

    
    @property
    def department(self):
         # Getter method for department
        return self._department

    @department.setter
    def department(self,new_department):
        # Setter method for department
        print(f"{self.department} was change to {new_department}")
        self._department = new_department

    @department.deleter
    def department(self):
        # deleter method for deparrtment
        del self._department

    @property
    def departmentBoss(self):
        # Getter method for department boss
        return self.departmentBoss
    @departmentBoss.setter
    def departmentBoss(self,new_departmantBoss):
        # Setter method for department boss
        print(f"{self.departmentBoss} was change to {new_departmantBoss}")
        self.departmentBoss = new_departmantBoss
    @departmentBoss.deleter
    def departmentBoss(self):
        # deleter method for deparrtmentBoss
        del self.departmentBoss

    def get_name(self):
        # Getter method for name
        return self.name
    def set_name(self,new_name):
        # Setter method for name
        self.name = new_name

    def get_id(self):
        # Getter method for student ID
        return self.id
    def set_id(self,new_id):
        # Setter method for student ID
        self.id = new_id

    def get_grade(self):
        # Getter method for grade
        return self.grade
    def set_grade(self,new_grade):
        # Setter method for grade
        self.grade = new_grade

    def get_address(self):
        # Getter method for address
        return self.address
    def set_address(self,new_address):
        # Setter method for address
        self.address = new_address
        
    def get_credits(self):
        # Getter method for credits
        return self.credits
    def set_credits(self,new_credits):
        # Setter method for credits
        self.credits = new_credits
        
    def get_GPA(self):
        # Getter method for GPA
        return self.GPA
    def set_GPA(self,new_GPA):
        # Setter method for GPA
        self.GPA = new_GPA

# Example usage:

student1 = student(
    "Computer Science",
    "Gwo-Jiun Horng",
    "Alex Lee",
    "4abg0037",
    "4",
    "709, Anping District, Tainan City, No. 1, Antong Street, Taiwan",
    120,
    4.5
    )

student1.print_details()

print(student1.department)
student1.department = "Math"
print(student1.department)
