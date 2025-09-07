class Student:
    
    def __init__(self):
        self.id=""
        self.name=""
        self.course=""

    # Setter Functions

    def setId(self,id):
        self.id=id 

    def setName(self,name):
        self.name=name

    def setCourse(self,course):
        self.course=course

    # Getter Functions
    
    def getId(self):
        return self.id 
    
    def getName(self):
        return self.name
    
    def getCourse(self):
        return self.course

# s1=Student()
# s1.id=1 
# s1.name="Suraj Sahani"
# s1.course="Python Programming"

# print(s1.id,s1.name,s1.course)

# s2=Student()
# s2.id=2 
# s2.name="Coder Bhaiya"
# s2.course="Python Programming"

# print(s2.id,s2.name,s2.course)

s3=Student()
s3.setId(3)
s3.setName("Coding With Coder Bhaiya")
s3.setCourse("Python Programming")

print(s3.getId(),s3.getName(),s3.getCourse())