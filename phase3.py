import numpy as np
import pandas
import pandas as pd
import csv
import sys


def search():
    searchtype = int(input("Choose a search method:\n1.Search by position.\n2.Search by salary.\n3.Search by state\n"))

    while searchtype < 1 or searchtype > 3:
        searchtype = int(
            input(
                "Your search type must be between 1 and 3 (inclusive), Please enter your choice again: \n"))

    if searchtype == 1:
        nrchoice = int(
            input("Please choose one of the following positions:\n1.Production Technician\n2.Software Engineer\n3.Data "
                  "Analyst\n4.Sr.Network Engineer\n5.Network Engineer\n6.IT Support\n7.IT Director\n8.Database "
                  "Administrator\n9.Senior BI Developer\n"))
        while nrchoice < 1 or nrchoice > 9:
            nrchoice = int(input(
                "Your input must be between 1 and 9 (inclusive), Please enter your choice again: \n"))
        choice = ""
        if nrchoice == 1:
            choice = "Production Technician"
        if nrchoice == 2:
            choice = "Software Engineer"
        if nrchoice == 3:
            choice = "Data Analyst"
        if nrchoice == 4:
            choice = "Sr. Network Engineer"
        if nrchoice == 5:
            choice = "Network Engineer"
        if nrchoice == 6:
            choice = "IT Support"
        if nrchoice == 7:
            choice = "IT Director"
        if nrchoice == 8:
            choice = "Database Administrator"
        if nrchoice == 9:
            choice = "Senior BI Developer"

        csv_file = csv.reader(open('/Users/hikmatsultan/Documents/Phase3/finalhrdataset.csv', "r"), delimiter=",")
        i = 1
        for row in csv_file:
            try:
                if choice in row[11]:
                    print("Employee:", i)
                    print("Name:", row[0])
                    print("Salary USD:", row[9])
                    print("State:", row[12])
                    print("ZIP code:", row[13])
                    print("DOB:", row[14])
                    print("Gender:", row[15])
                    print("Phone Number:", row[28], "\n")
                    i = i + 1
            except IndexError:
                pass

    if (searchtype == 2):

        nrchoice = int(
            input(
                "Please choose one of the following range of salaries:\n1.45000-60000\n2.60000-90000\n3.90000-250000\n"))
        while nrchoice < 1 or nrchoice > 3:
            nrchoice = int(input(
                "Your input must be between 1 and 3 (inclusive), Please enter your choice again: \n"))

        if nrchoice == 1:
            choice = list(range(45000, 60000))

        if nrchoice == 2:
            choice = list(range(60000, 90000))

        if nrchoice == 3:
            choice = list(range(90000, 250000))

        csv_file = csv.reader(open('/Users/hikmatsultan/Documents/Phase3/finalhrdataset.csv', "r"), delimiter=",")
        i = 1

        for row in csv_file:
            for j in range(0, len(choice)):
                choice[j] = str(choice[j])

                try:
                    if choice[j] in row[9]:
                        print("Employee", i)
                        print("Name:", row[0])
                        print("Salary USD:", row[9])
                        print("State:", row[12])
                        print("ZIP code:", row[13])
                        print("DOB:", row[14])
                        print("Gender:", row[15])
                        print("Phone Number:", row[28], "\n")
                        i = i + 1
                except IndexError:
                    pass

    if searchtype == 3:
        nrchoice = int(
            input("Please choose one of the following States:\n1.Massachusetts \n2.TEXAS\n3.CONNECTICUT "
                  "\n4.VERMONT\n5.ALABAMA\n6.WASHINGTON\n7.OHIO\n8.INDIANA "
                  "\n9.TENNESSEE\n10.NEW HAMPSHIRE\n11.RHODE ISLAND\n12.PENNSYLVANIA\n13.COLORADO\n14.NEW YORK "
                  "\n15.UTAH\n16.NEW YORK\n"))
        while nrchoice < 1 or nrchoice > 16:
            nrchoice = int(input(
                "Your input must be between 1 and 16 (inclusive), Please enter your choice again: \n"))
        choice = ""
        if nrchoice == 1:
            choice = "MA"
        if nrchoice == 2:
            choice = "TX"
        if nrchoice == 3:
            choice = "CT"
        if nrchoice == 4:
            choice = "VT"
        if nrchoice == 5:
            choice = "AL"
        if nrchoice == 6:
            choice = "WA"
        if nrchoice == 7:
            choice = "OH"
        if nrchoice == 8:
            choice = "IN"
        if nrchoice == 9:
            choice = "TN"
        if nrchoice == 10:
            choice = "NH"
        if nrchoice == 11:
            choice = "RI"
        if nrchoice == 12:
            choice = "PA"
        if nrchoice == 13:
            choice = "CO"
        if nrchoice == 14:
            choice = "NY"
        if nrchoice == 15:
            choice = "UT"
        if nrchoice == 16:
            choice = "NY"

        csv_file = csv.reader(open('/Users/hikmatsultan/Documents/Phase3/finalhrdataset.csv', "r"), delimiter=",")
        i = 0
        for row in csv_file:
            try:
                if choice in row[12]:
                    i = i + 1
                    print("Employee:", i)
                    print("Name:", row[0])
                    print("Salary USD:", row[9])
                    print("State:", row[12])
                    print("ZIP code:", row[13])
                    print("DOB:", row[14])
                    print("Gender:", row[15])
                    print("Phone Number:", row[28], "\n")
            except IndexError:
                pass
        if i == 0:
            print("No employees working in this state")


def group_schedular():
    df1 = pandas.read_csv('/Users/hikmatsultan/Documents/Phase3/schedule1.csv', skiprows=0, usecols=range(1, 6)).values
    df2 = pandas.read_csv('/Users/hikmatsultan/Documents/Phase3/schedule2.csv', skiprows=0, usecols=range(1, 6)).values
    df3 = pandas.read_csv('/Users/hikmatsultan/Documents/Phase3/schedule3.csv', skiprows=0, usecols=range(1, 6)).values
    arrdf1 = np.ravel(df1)
    arrdf2 = np.ravel(df2)
    arrdf3 = np.ravel(df3)
    farray = []
    available = False
    counter = 0
    for x, y, z in zip(arrdf1, arrdf2, arrdf3):
        if x == y and x == z and x in "Free":
            farray.append(x)
        else:
            farray.append("Busy")

    print("Free time slots are:")
    for i in farray:
        counter = counter + 1
        if i == "Free":
            available = True
            if (counter - 1) % 5 == 0:
                print("Monday ")
            if (counter - 2) % 5 == 0:
                print("Tuesday ")
            if (counter - 3) % 5 == 0:
                print("Wednesday ")
            if (counter - 4) % 5 == 0:
                print("Thursday ")
            if (counter - 5) % 5 == 0:
                print("Friday ")
            if 1 <= counter <= 5:
                print("between 8:00 and 9:00\n")
            if 6 <= counter <= 10:
                print("between 9:00 and 10:00\n")
            if 11 <= counter <= 15:
                print("between 10:00 and 11:00\n")
            if 16 <= counter <= 20:
                print("between 11:00 and 12:00\n")
            if 21 <= counter <= 25:
                print("between 12:00 and 13:00\n")
            if 26 <= counter <= 30:
                print("between 13:00 and 14:00\n")
            if 31 <= counter <= 35:
                print("between 14:00 and 15:00\n")
            if 36 <= counter <= 40:
                print("between 15:00 and 16:00\n")
            if 41 <= counter <= 45:
                print("between 16:00 and 17:00\n")
    if not available:
        print("No common free time slot are available")


def risk_calculator():
    np.set_printoptions(suppress=True)
    csv_file = pandas.read_csv('/Users/hikmatsultan/Documents/Phase3/riskdataset.csv', skiprows=0,
                               usecols=range(1, 7)).values
    daysabsence = 0;
    count = 0;
    dayslateabsence = 0
    weightabsence = 0
    totaldays = 0
    weightthirdparty = 0
    probabilityabsence = 0
    daysthirdparty = 0
    dayslatethirdparty = 0
    probabilitythirdparty = 0
    daysunforeseenevents = 0
    dayslateunforeseenevents = 0
    probabilityunforeseenevents = 0
    weightunforeseenevents = 0
    finalprobability = 0
    riskeffect = 0
    conclusion = ""

    for row in csv_file:
        if row[1] >= 1:
            daysabsence = daysabsence + 1
        count = count + 1
        dayslateabsence = dayslateabsence + row[2]
        totaldays = totaldays + row[5]
    probabilityabsence = daysabsence / count
    weightabsence = dayslateabsence / totaldays

    for row in csv_file:
        if row[3] > 0:
            daysthirdparty = daysthirdparty + 1
        dayslatethirdparty = dayslatethirdparty + row[3]

    probabilitythirdparty = daysthirdparty / count
    weightthirdparty = dayslatethirdparty / totaldays

    for row in csv_file:
        if row[4] > 0:
            daysunforeseenevents = daysunforeseenevents + 1
        dayslateunforeseenevents = dayslateunforeseenevents + row[4]

    probabilityunforeseenevents = daysunforeseenevents / count
    weightunforeseenevents = dayslateunforeseenevents / totaldays

    finalprobability = (probabilityunforeseenevents + probabilityabsence + probabilitythirdparty) / 3
    riskeffect = (probabilitythirdparty * weightthirdparty) + (probabilityabsence * weightabsence) + (
            probabilityunforeseenevents * weightunforeseenevents) / 3
    print("Final probability is: ", finalprobability)

    if riskeffect < 0.01:
        conclusion = "Insignificant"
    if 0.01 < riskeffect < 0.10:
        conclusion = "Tolerable"
    if 0.10 <= riskeffect < 0.20:
        conclusion = "Serious"
    if riskeffect >= 0.20:
        conclusion = "Catastrophic"

    print("The level of risk is: ", conclusion)


def main():
    choice = int(input(
        "What do you wish to do?\n1.Search the database\n2.Access group scheduler\n3.Calculate risk of lateness\n "))
    while choice < 1 or choice > 3:
        choice = int(
            input(
                "Your choice must be between 1 and 3 (inclusive), Please enter your choice again: \n"))
    if choice == 1:
        search()
    if choice == 2:
        group_schedular()
    if choice == 3:
        risk_calculator()


if __name__ == "__main__":
    main()
