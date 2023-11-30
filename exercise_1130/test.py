class student :
     # Class-level variables for school name and address
    school_name = "STUST"
    school_address = "No. 1, Nantai Street, Yongkang District, Tainan City, Taiwan"

    def __init__(self,department,departmentBoss,name,id,grade,address,credits,GPA) :
        # Instance-level variables
        self.department = department
        self.departmentBoss = departmentBoss
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
        print("deparment : ",self.department)
        print("department Boss :", self.departmentBoss)
        print("student name : ", self.name)
        print("student id : ",self.id )
        print("student grade : ",self.grade)
        print("student address : ",self.address)
        print("student credits : ", self.credits)
        print("student GPA : ",self.GPA)

    
    def get_department(self):
         # Getter method for department
        return self.department
    def set_deparmant(self,new_departmant):
        # Setter method for department
        self.department = new_departmant

    def get_departmentBoss(self):
        # Getter method for department boss
        return self.departmentBoss
    def set_departmentBoss(self,new_departmantBoss):
        # Setter method for department boss
        self.departmentBoss = new_departmantBoss

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