class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, testScores,numScores):
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores
        self.numScores = numScores

    def calculate(self):
        total = 0

        for testScore in self.testScores:
            total += testScore

        avg = total / self.numScores

        if 90 <= avg <= 100:
            return 'O'
        if 80 <= avg < 90:
            return 'E'
        if 70 <= avg < 80:
            return 'A'
        if 55 <= avg < 70:
            return 'P'
        if 40 <= avg < 55:
            return 'D'
        return 'T'


#line = input().split()
firstName = "Sayeed" #line[0]
lastName = "Hossen" #line[1]
idNum = 19952345 #line[2]
numScores = 2  #int(input())
scores = [100,55] #list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores,numScores)
s.printPerson()
print("Grade:", s.calculate())