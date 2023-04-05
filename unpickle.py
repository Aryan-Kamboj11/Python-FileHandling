import pickle,stu

with open('pickle2.dat','rb') as unpickle_file:
    while True:
        try:
            obj=pickle.load(unpickle_file)
            obj.display_student()
        except EOFError:
            print("Done!")
            break