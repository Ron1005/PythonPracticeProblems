#Define a class named American which has a static method called printNationality.

class American:
    @staticmethod
    def printNationality():
        print("I am American")

class NewYorker(American):
    pass

American.printNationality()
NewYorker.printNationality()