from os import getcwd

with open(f"{getcwd()}/input.txt") as f:
    lines = f.readlines()
    overlap =0
    for line in lines:
        line = line.replace("\n","").split(",")
        firstRange,secondRange = line[0],line[1]
        firstSet = set(range(int(firstRange.split("-")[0]),int(firstRange.split("-")[1])+1))
        secondSet = set(range(int(secondRange.split("-")[0]),int(secondRange.split("-")[1])+1))
        if firstSet.issubset(secondSet):
            overlap+=1
        elif secondSet.issubset(firstSet):
            overlap+=1
        else:pass
    print(overlap)


with open(f"{getcwd()}/input.txt") as f:
    lines = f.readlines()
    overlapAtAll=0
    for line in lines:
        line = line.replace("\n","").split(",")
        firstRange,secondRange = line[0],line[1]
        firstSet = set(range(int(firstRange.split("-")[0]),int(firstRange.split("-")[1])+1))
        secondSet = set(range(int(secondRange.split("-")[0]),int(secondRange.split("-")[1])+1))
        if firstSet.intersection(secondSet)!=set():
            overlapAtAll+=1

    print(overlapAtAll) 
