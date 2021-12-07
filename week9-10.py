import json
#created a class named Individual
class Individual:
    def __init__(self):
        #intiliazation of the global variables
        self.name = ''
        self.ID = -1
        self.email = ''

#created a class Instructor
class Instructor(Individual):
    def __init__(self):
        #Creating the validator object go that we can use its p=functions to valida data
        self.validator = Validator()
        self.last_institution_name = ''
        self.highest_degree = ''

    def set_id(self, _id):
        # Using validator to validate the instructor ID
        isValid = self.validator.isValidInstructorID(_id)
        if not isValid:
            print(" Please Enter valid Instructor ID .....")
            return False
        self.ID = _id
        return True

    def get_id(self):
        return self.ID

    #Function to populate the ID until it reaches the validations.
    def populate_id(self):
        isValidID = False
        while not isValidID:
            _id = input("\n Enter ID: ")
            isValidID = self.set_id(_id)

    def get_name(self):
        return self.name
#Function to populate the instructor name until it reaches the validations.
    def set_name(self, _name):
        isValid = self.validator.isValidName(_name)
        if not isValid:
            print(" Please Enter valid Instructor Name .....")
            return False
        self.name = _name
        return True

    #Function to populate the NAME until it reaches the validations.
    def populate_name(self):
        isValidName = False
        while not isValidName:
            _name = input("\n Enter Name: ")
            isValidName = self.set_name(_name)

    def get_email(self):
        return self.email
#Function to populate the email until it reaches the validations.
    def set_email(self, _email):
        isValid = self.validator.isValidEmail(_email)
        if not isValid:
            print(" Please Enter valid Insturctor Email .....")
            return False
        self.email = _email
        return True

#Function to populate the EMAIL until it reaches the validations.
    def populate_email(self):
        isValidEmail = False
        while not isValidEmail:
            _email = input("\n Enter Email: ")
            isValidEmail = self.set_email(_email)
#function for last_institution_name
    def set_last_institution_name(self, institution_name):
        self.last_instiution = institution_name
    
    def get_last_institution_name(self):
        return self.last_instiution

#Function to populate the LAST INSTITUTION NAME until it reaches the validations.
    def populate_last_institution_name(self):
        isValidInstitutionName = False
        while not isValidInstitutionName:
            _institution_name = input("\n Enter Last Institution Name: ")
            if len(_institution_name) == 0:
                print("Please enter the Institution Name")
            else:
                self.set_last_institution_name(_institution_name)
                isValidInstitutionName = True

    def set_highest_degree(self, highest_degree):
        self.highest_degree = highest_degree

    def get_highest_degree(self):
        return self.highest_degree

#Function to populate the HIGHEST DEGREE until it reaches the validations.
    def populate_highest_degree(self):
        isValidHighestDegree = False
        while not isValidHighestDegree:
            _highest_degree = input("\n Enter Last Highest Degree: ")
            if len(_highest_degree) == 0:
                print("Please enter the Valid Highest Degree:")
            else:
                self.set_highest_degree(_highest_degree)
                isValidHighestDegree = True

 # Function to return the record in a json format.
    def json(self):
        record = {
                "Instructor ID"              : self.get_id(),
                "Instructor Name"            : self.get_name(),
                "Instructor Email"           : self.get_email(),
                "Instructor Last Institution": self.get_last_institution_name(),
                "Instructor High Degree"     : self.get_highest_degree()
                }
        return record

#created a class Student
class Student(Individual):
    def __init__(self):
        self.validator = Validator()
        self.program = ''

    def set_id(self, _id):
        isValid = self.validator.isValidStudentID(_id)
        if not isValid:
            print(" Please Enter valid student ID .....")
            return isValid
        self.ID = _id
        return isValid

    def get_id(self):
        return self.ID

#Function to populate the ID until it reaches the validations.
    def populate_id(self): 
        isValidID = False
        while not isValidID:
            _id = input("\n Enter Student ID: ")
            isValidID = self.set_id(_id)

    def get_name(self):
        return self.name

    def set_name(self, _name):
        isValid = self.validator.isValidName(_name)
        if not isValid:
            print(" Please Enter valid student Name .....")
            return False
        self.name = _name
        return True

#Function to populate the NAME until it reaches the validations.
    def populate_name(self):
        isValidName = False
        while not isValidName:
            _name = input("\n Enter Name: ")
            isValidName = self.set_name(_name)

    def get_email(self):
        return self.email

    def set_email(self, _email):
        isValid = self.validator.isValidEmail(_email)
        if not isValid:
            print(" Please Enter valid student Email .....")
            return False
        self.email = _email
        return True

#Function to populate the EMAIL until it reaches the validations.
    def populate_email(self):
        isValidEmail = False
        while not isValidEmail:
            _email = input("\n Enter Email: ")
            isValidEmail = self.set_email(_email)

    def set_program(self, program):
        self.program = program

    def get_program(self):
        return self.program

#Function to populate the PROGRAM until it reaches the validations.
    def populate_program(self):
        isValidProgram = False
        while not isValidProgram:
            _program = input("\n Enter Program Name: ")
            if len(_program) == 0:
                print("Please enter the programName")
            else:
                self.set_program(_program)
                isValidProgram = True

    # Function to return student record in json format.
    def json(self):
        record = {
                "Student ID"    : self.get_id(),
                "Student Name"   : self.get_name(),
                "Student Email"  : self.get_email(),
                "Student Program": self.get_program()
                }
        return record
 #Create a method that displays all collected information for an individual called "displayInformation".       
    def displayInformation(self):
        return self.json   

#created a class Validator
class Validator:
    #Function to validate the Instructor ID
    def isValidInstructorID(self, instructor_ID):
        if len(instructor_ID) <= 5 and instructor_ID.isdigit(): #if entered length of  number is greater than 5 it will not accepct
            return True
        return False

    #Function to validate the Student ID
    def isValidStudentID(self,student_ID):
        if len(student_ID) <= 7 and student_ID.isdigit(): #this is required, and must be a number that is 7 or less digits long, if entered a number greater than 7 it will not accepct
            return True
        return False

    #Function to validate the Instructor/Student Email ID validator as it is same for anyone
    def isValidEmail(self, email):
        chars = set(["!", '"', "#", "$","%","^","&","*","(",")","=","+",",","<",">","/","?",";",":","[","]","{","}","\\"]) #if entered these characters it will not allow
        if email:
            for character in email:
                if character in chars:
                    return False
            return True
        else:
            print("User email is missing, try again")

    #Function to validate the Instructor/Student Name validator as it is same for anyone
    def isValidName(self, name):
        chars = set(["!", '"',"@", "#", "$", "%","^","&","*","(",")","_","=","+",",","<",">","/","?",";",":","[","]","{","}","\\","."]) #if entered these characters it will not allow
        if name:
            for character in name:
                if character in chars or character.isdigit():
                    return False
            return True
        else:
            print("Name is missing Please enter again")
            return False


college_records = [] #creted an empty list college_records
while True:
    user = (input("Please select type of user (Student/Instructor): ")).lower() #user can select type Student/instructor
    if user == "instructor":
        #Getting the info of the Instructor using the instructor class.
        instructor = Instructor()
        instructor.populate_id()
        instructor.populate_name()
        instructor.populate_email()
        instructor.populate_last_institution_name()
        instructor.populate_highest_degree()
        college_records.append(instructor.json())
    elif user == "student":
        #Getting and populate their Student related data.
        student = Student()
        student.populate_id()
        student.populate_name()
        student.populate_email()
        student.populate_program()
        college_records.append(student.json()) #appending into college_records
    else:
        print("Input user type is not valid. Please enter the valid user type")
        continue
#asking user if want to re enter the data
    stop = input("Do you want to re-enter the data If--YES enter y or Y, If NO--enter n or N :")
    if stop == 'n' or stop == 'N':
        # Print the output in a json pretty way.
        print(json.dumps(college_records, indent = 3))
        break
#GitHub Link-- https://github.com/
#Repository Name--week 9-10
