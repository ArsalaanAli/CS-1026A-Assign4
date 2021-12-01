from country import Country
class CountryCatalogue:
    def __init__(self, countryFile):
        countryCat = dict()
        self.countryCat = countryCat 
        countryFileOpened = open(countryFile, 'r')
        countryInfo = countryFileOpened.readlines()
        for country in countryInfo[1::]:
            country = country.split("|")
            tempName = country[0]
            tempContinent = country[1]
            tempPop = country[2]
            tempArea = country[3].strip("\n")
            tempCountry = Country(tempName, tempPop, tempArea, tempContinent)
            countryCat[tempName] = tempCountry
        print(countryCat)

    def setPopulationOfCountry(self, countryName, value):
        if countryName in countryCat:
            countryCat[countryName].setPopulation(value)
        else:
            print(countryName, "is not in the Country Catalogue")
    def setAreaOfCountry(self, countryName, value):
        if countryName in countryCat:
            countryCat[countryName].setArea(value)
        else:
            print(countryName, "is not in the Country Catalogue")
    def setContinentOfCountry(self, countryName, value):
        if countryName in countryCat:
            countryCat[countryName].setContinent(value)
        else:
            print(countryName, "is not in the Country Catalogue")

    def findCountry(self, country):
        if country in countryCat.values():
            return country
        else:
            return None



    def addCountry(self, countryName, pop, area, cont):
        if countryName in self.countryCat:
            return False
        newCountry = Country(countryName, pop, area, continent)
        self.countryCat[countryName] = newCountry

    def printCountryCatalogue(self):
        for country in self.countryCat.keys():
            print(self.countryCat[country])
        
x = CountryCatalogue("data.txt")
x.printCountryCatalogue()
