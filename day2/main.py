import os

score={
    "rock":1,
    "paper":2,
    "scissors":3,
    "won":6,
    "draw":3,
    "lost":0,
    "X":"rock",
    "Y":"paper",
    "Z":"scissors"
}

fileContent = open(f"{os.getcwd()}/input.txt","r").read().split("\n")

totalPoints =0
for f in fileContent:

    elfPlay = f[0]
    userPlay =  f[len(f)-1]
    totalPoints+= score[ score[userPlay] ]
    if(elfPlay=="A" and userPlay=="Y"): totalPoints+=score["won"]
    elif(elfPlay=="B" and userPlay=="Z"): totalPoints+=score["won"]
    elif (elfPlay=="C" and userPlay=="X"): totalPoints+=score["won"]

    if(elfPlay=="A" and userPlay=="X"):totalPoints+=score["draw"]
    elif (elfPlay=="B" and userPlay=="Y"):totalPoints+=score["draw"]
    elif (elfPlay=="C" and userPlay=="Z"): totalPoints+=score["draw"]

print(totalPoints)

newScore=0

for f in fileContent:
    elfPlay = f[0]
    userPlay =  f[len(f)-1]
    
    if(elfPlay=="A"):
        if(userPlay=="X"):
            newScore+=score["scissors"]
        elif(userPlay=="Y"):
            newScore+=score["rock"]
            newScore+=score["draw"]

        else:
            newScore+=score["paper"]
            newScore+=score["won"]
    if(elfPlay=="B"):
        if(userPlay=="X"):
            newScore+=score["rock"]
        elif(userPlay=="Y"):
            newScore+=score["paper"]
            newScore+=score["draw"]

        else:
            newScore+=score["scissors"]
            newScore+=score["won"]
    if(elfPlay=="C"):
        if(userPlay=="X"):
            newScore+=score["paper"]
        elif(userPlay=="Y"):
            newScore+=score["scissors"]
            newScore+=score["draw"]

        else:
            newScore+=score["rock"]
            newScore+=score["won"]

print(newScore)

