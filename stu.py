class Student :
    def __init__(self,fname,lname,gender,age,degree):
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.age=age
        self.degree=degree

    def display_student(self):
        dict1= {'student_name':self.fname+' '+self.lname,'age':self.age,'gender':self.gender,
                'degree':self.degree}
        print(dict1)
