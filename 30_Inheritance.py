class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        Person.__init__(self, firstName, lastName, idNumber)
        #or, super().__init__(firstName, lastName, idNumber) at the top of the init method
    
    def calculate(self):
        print(self.scores)
        avg = int(sum([score for score in self.scores])/len(self.scores))
        
        if avg in range(90, 101):
            return 'O'
        
        elif avg in range(80, 90):
            return 'E'
        
        elif avg in range(70, 80):
            return 'A'
        
        elif avg in range(55, 70):
            return 'P'
        
        elif avg in range(40, 55):
            return 'D'

        else:
            return 'T'
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    

line = input().split()

firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()

print("Grade:", s.calculate())