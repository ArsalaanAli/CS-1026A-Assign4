badUpdateFile = open("badupdates.txt", 'w')
def processUpdates(cntryFileName,updateFileName,badUpdateFile):
    return None
def isValidUpdate(record):
    record = record.replace(" ", "")
    record = record.split(";")
    if len(record) > 4:
        return False
    name = record[0]
    if name[0] != name[0].upper():
        return False
    for chr in name:
        if not chr.isalpha() and chr != "_":
            return False
    
    pop = ""
    area = ""
    continent = ""

    for update in record:
        if 

    print(record, name)
print(isValidUpdate(" United_States_of_America; P=328,566,312; A=83, 022, 544"))