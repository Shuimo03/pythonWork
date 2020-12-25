class Student:
    __name = ""
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.__name

if __name__=="__main__":
    student = Student("borphi")
    print(student.getName())

