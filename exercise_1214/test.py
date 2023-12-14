class student:
    def __init__(self,student_id,name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def add_course(self, course_code, course_name, semester)
        if semester not in self.courses:
            self.courses[semester] = []
        self.courses[semester].append({"code" : course_code, "name" : course_name})

    def delete_course(self, course_code, semester)
        if semester in self.courses and any(course["code"] == course_code for course in self.courses[semester]) :
            self.courses[semester] = [course for course in self.courses[semester] if course["code"] != course_code]
            print(f"刪除 {self.name} 在 {semester} 學期修習的 {course_code} 課程。")
        else:
            print(f"{self.name} 在 {semester} 學期找不到 {course_code} 課程。")    
    