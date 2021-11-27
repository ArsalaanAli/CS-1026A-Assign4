class Country:
    def __init__(self, name, pop, area, continent):
        self.name = name
        self.pop = pop
        self.area = area
        self.continent = continent
    
    #getter methods
    def getName(self):
        return self.name
    def getPopulation(self):
        return self.pop
    def getArea(self):
        return self.area
    def getContinent(self):
        return self.continent

    #setter methods
    def setName(self, newName):
        self.name = newName
    def setPopulation(self, newPop):
        self.pop = newPop
    def setArea(self, newArea):
        self.area = newArea
    def setContinent(self, newContinent):
        self.continent = newContinent
