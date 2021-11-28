class CountryCatalogue:
    countryCat = dict()
    def __init__(self, countryFile):
        countryFileOpened = open(countryFile, 'r')
        countryInfo = countryFileOpened.readlines()
        for i in countryInfo:
            print(i)
x = CountryCatalogue("data.txt")