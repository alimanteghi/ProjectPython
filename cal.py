import datetime

class Person:
    def __init__(self , name , age , sex ) :
        self.name = name
        self.age = age
        self.sex = sex
    def toString(self):
        print(self.name, self.age, self.sex,"\n")

    def toBirthDate(self):
        print("Birthdate= ",datetime.date.today().year-self.age)

class Robot:
    def __init__(self , name ) :
        self.name = name

    def toString(self):
        print(self.name,"\n")
    
    def moveLeft(self):
        print("Move left")
    def moveRight(self):
        print("Move right")


Robot1=Robot("Micky")
Robot1.toString()
Robot1.moveLeft()
Robot1.moveLeft()
Robot1.moveRight()

person1=Person("ali" , 35 , "male")
Person("John" , 15 , "male").toString()
person1.toString()
person1.toBirthDate()


        