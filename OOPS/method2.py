@classmethod
def showcount(cls):
      print (cls.empCount)
      
Employee.showcount()
 @classmethod
   def showcount(cls):
         print (cls.empCount)
         return
   @classmethod
   def newemployee(cls, name, age):
      return cls(name, age)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)

Employee.showcount()