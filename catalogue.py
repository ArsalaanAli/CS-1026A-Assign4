from country import Country
class CountryCatalogue:
    def __init__(self, countryFile):
        countryCat = set()
        countryFileOpened = open(countryFile, 'r')
        countryInfo = countryFileOpened.readlines()
        for country in countryInfo[1::]:
            country = country.split("|")
            tempName = country[0]
            tempContinent = country[1]
            tempPop = country[2]
            tempArea = country[3].strip("\n")
            tempCountry = Country(tempName, tempPop, tempArea, tempContinent)
            countryCat.add(tempCountry)
    
CountryCatalogue("data.txt")