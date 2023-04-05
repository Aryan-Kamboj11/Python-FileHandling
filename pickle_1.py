import pickle,stu

with open('pickle2.dat','wb') as pickle_file:
    n=int(input("Enter the students for database : "))
    for i in range(n):
        print("Enter the detail for {} student ".format(i))
        fname=input("Enter the first name of your student: ")
        lname=input("Enter the last name of your student: ")
        age=int(input("Enter the age for the student: "))
        gender=input("Enter gender: ")
        degree=input("Enter the degree he/she is pursuing: ")
        s=stu.Student(fname,lname,age,gender,degree)
        pickle.dump(s,pickle_file)
        