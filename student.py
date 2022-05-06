class Student:
    # constructor
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    # defining instance methods
    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def percentage(self):
        return (self.totalObtained() / 300) * 100