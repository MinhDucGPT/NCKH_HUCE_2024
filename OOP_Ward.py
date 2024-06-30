class Student():
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade
    def describe(self):
        print('Student - Name: ', self.name,' - YoB: ', self.yob, ' - Grade: ', self.grade )


class Teacher():
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject
    def describe(self):
        print('Teacher - Name: ', self.name,' - YoB: ', self.yob, ' - Subject: ', self.subject )
        
        
        
class Doctor():
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist
    def describe(self):
        print('Teacher - Name: ', self.name,' - YoB: ', self.yob, ' - Specialist: ', self.specialist )
        


global lst_person
class Ward(Teacher, Doctor, Student):
    def __init__(self, name):
        self.name = name
    
    lst_person = []
    def add_person(self, person):
        
        self.lst_person.append(person)
        
    def describe(self):
        print("Ward Name: ", self.name)
        for i in self.lst_person:
            i.describe()
    def count_doctor(self):
        doctor = 0
        for i in self.lst_person:
            if(type(i)== Doctor):
                doctor += 1
        return doctor  

    def sort_age(self):
        def trave_tuoi(self):
            return self.yob
        self.lst_person.sort(key= trave_tuoi, reverse=True)
        return self.lst_person  
    
    def compute_average(self):
        average = 0
        dem = 0
        for i in self.lst_person:
            if (type(i) == Teacher):
                average += i.yob
                dem += 1
        return average/dem
    
        
student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
student1 . describe ()

teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
teacher1 . describe ()

doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
doctor1 . describe ()


teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward ( name =" Ward1 ")
ward1.add_person (student1)
ward1.add_person (teacher1)
ward1.add_person (teacher2)
ward1.add_person (doctor1)
ward1.add_person (doctor2)
ward1 . describe ()

print ( f"Number of doctors : { ward1 . count_doctor ()}")


print ("After sorting Age of Ward1 people ")
ward1 . sort_age ()
ward1 . describe ()

print ( f"\ nAverage year of birth ( teachers ): { ward1 . compute_average ()}")
print('\n\n\n\n\n')