#****************************************************************************
# Description:     Gets a list of names from a database and prints them
# Input:           Gets a name and gender from the user
#
# Output:          prints out the names of the list of top 20 names
# Sources:         Lab 7 specifications
#                  Murach's Python Programming
#****************************************************************************
#!/user/bin/env python3

from Name import Name

def main():

    year = 0
    gender = "M"

    #Gets the date
    while True:
        print("Select a year between 1915 and 2014:")
        try:
            year = int(input())
            if year < 1915 or year > 2014:
                print("The year must be between 1915 and 2014!")
                continue
        except:
            print("Please enter a whole number!")
            continue
        else:
            break

    #Gets the gender
    while True:
        print("Please enter a gender(M / F):")
        try:
            gender = input()
            if gender.lower() != "m" and gender.lower() != "f":
                print("Please type M or F!")
                continue
        except:
            print("Invalid input")
            continue
        else:
            break

    #reads names from the db
    names = Name.readNames(year, gender)
    i = 0

    print("20 most popular names for " + gender + "babies in " + str(year) + " ")
    print("")
    print("Year   Name           Gender    Count")
    #Will loop through each Name object and print out
    while i < len(names):
        print(names[i].year, names[i].text, names[i].gender, names[i].count)
        i += 1


if __name__ == "__main__":
    main()
