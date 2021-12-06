badUpdateFile = open("badupdates.txt", 'w')
def processUpdates(cntryFileName,updateFileName,badUpdateFile):
    return None
def isValidUpdate(record):
    record = record.replace(" ", "")
    record = record.split(";")
    if len(record) > 4:
        return False
    if invalidName(record[0]):
        return False
    
    pop = ""
    area = ""
    cont = ""

    for update in record[1::]:
        if update[0:2]=="P=":
            if pop != "":
                return False
            if invalidDigit(update[2::]):
                return False
            pop = update[2::]
            
        elif update[0:2]=="A=":
            if area != "":
                return False
            if invalidDigit(update[2::]):
                return False
            area = update[2::]
        
        elif update[0:2]=="C=":
            if cont != "":
                return False
            if invalidCont(update[2::]):
                return False
            cont = update[2::]
        else:
            if update != "":
                return False
    return True

def invalidDigit(digit):
    digit = digit.split(",")
    if not digit[0].isdigit():
        return True
    if len(digit[0]) > 3 or len(digit[0])<1:
        return True
    for nums in digit[1::]:
        if len(nums) != 3:
            return True
        if not nums.isdigit():
            return True
    return False
def invalidCont(cont):
    continents = ["Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America"]
    if cont in continents:
        return False
    return True
def invalidName(name):
    if name[0] != name[0].upper():
        return True
    for char in name:
        if not char.isalpha() and char != "_":
            return True
    return False
records = ["Canada;P=37,591,023 ", "       Germany;A=213,000;P=83,022,544       ", "       Germany ; A=213 , 000 ; P=83, 022, 544 ", "       Vietnam;P=94,469,067       ", "Mexico       ", "       Mexico;   ", "       France;;A=213,000;P = 67,067,112 ", "       France; A=213,000 ; P = 67,067,112 ; C=Europe ", "United_States_of_America;P=328,566,312 ", "United_states_of_america;P=328,566,312"]
badRecs = ["Canada ; P=37591023  ", "Canada       P=37,591,02", "Indonesia;P 260,581,345", "Indonesia;P 260,581,345", "germany;A=213,000;P=83,022,544", "A=213,000;P=83,022,544     ", "Mexico;A=213,000;P=83,022,544;A=213,000;P=83,022,544", "France;A=213,000;A=213,067", "Vietnam;P=94,469,067;C=asia"]
for rec in records:
    print(isValidUpdate(rec))
print("break")
for rec in badRecs:
    print(isValidUpdate(rec))