import os

fileContent = open(f"{os.getcwd()}/input.txt").read()

calories = fileContent.strip().split("\n\n")
totalCal = []
for cal in calories:
    s=0
    c = cal.split("\n")
    for c_ in c:
        s+=int(c_)
    totalCal.append(s)

print(max(totalCal))
sumOfCal=0
for i in range(3):
    biggestNumber = max(totalCal)
    sumOfCal+=biggestNumber
    del totalCal[totalCal.index(biggestNumber)]
print(sumOfCal)

