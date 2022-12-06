from os import getcwd
def parseStuff(l: str, num: int):
    parsed = 0
    firstPacket = l[parsed:num]
    while parsed >= 0:
        hasDuplicateString = not len(set(firstPacket)) == len(firstPacket)
        if (hasDuplicateString == True):
            parsed += 1
            firstPacket = f"{firstPacket[1:]}{l[len(firstPacket)+parsed-1]}"
        else:
            break
    return parsed+len(firstPacket)


with open(f"{getcwd()}/input.txt", "r") as f:
    fileContent = f.read().replace("\n", "")
    print(f"Solution for Part 1: {parseStuff(fileContent,4)}")
    print(f"Solution for Part 2: {parseStuff(fileContent,14)}")
