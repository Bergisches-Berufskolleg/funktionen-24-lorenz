
def isLeapYear(year):  
    if(year % 400 ==0):
        return True
    elif(year % 100 ==0 and year % 400 !=0):
        return False
    elif(year % 4 ==0):
        return True
    return False

def main():
    year = float (input("\ngeben sie ein Jahr ein und wir prüfen ob es ein schalt ja ist oder nicht:"))
    print(f"\n{isLeapYear(year)} \n")
    


if __name__ == "__main__":
    main()
