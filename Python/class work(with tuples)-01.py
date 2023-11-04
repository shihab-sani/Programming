class Student:
    def __init__(self,name,id,subject):
        self.name = name
        self.id = id
        self.subject = subject
    def get_info(self):
        return self.name,self.id,self.subject
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_subject(self):
        return self.subject
    def set_name(self,new_name):
        self.name = new_name
    def set_id(self,new_id):
        self.id = new_id
    def add_subject(self,new_subjects):
        self.subject.append(new_subjects)
    def calculate_gpa(self,sub):
        grade = {"A":4.00,"A-":3.70,"B+":3.30,"B":3.00,"B-":2.70,"C+":2.30,"C":2.00,"C-":1.70,"D+":1.30,"D":1.00,"F":0.00}
        for i in range(len(self.subject)):
            if sub in self.subject[i]:
                return grade.get(self.subject[i][1])       
    def avarage_gpa(self):
        total = 0
        for i in range(len(self.subject)):
            gpa = self.calculate_gpa(self.subject[i][0])
            total += gpa
        return f"{total/len(self.subject):.2f}"
             
        

shihab = Student("Shihab",2320590,[("computer","A"),("phy","C")])
shihab.add_subject(("math","A-"))        
print(shihab.get_subject())
print(shihab.calculate_gpa("math"))
print(shihab.calculate_gpa("computer"))
print(shihab.calculate_gpa("phy"))
print(shihab.avarage_gpa())