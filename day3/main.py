from string import ascii_letters
import os

letters = list(ascii_letters)
fileContent = open(f"{os.getcwd()}/input.txt","r").read().split("\n")

score = 0
def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0
            match = ''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and string1[i+lcs_temp] == string2[j+lcs_temp]):
                match += string2[j+lcs_temp]
                lcs_temp += 1
            if len(match) > len(answer):
                answer = match
    return answer
for e in fileContent:
    firstCompartment,secondCompartment = e[:len(e)//2],e[len(e)//2:]
    commonItem = set(longestSubstringFinder(firstCompartment,secondCompartment))
    for j in commonItem:score+=letters.index(j)+1
    

print(score)

index=0
newScore=0
for e in range(0,len(fileContent)//3):
    firstBagItems = set(fileContent[index])
    secondBagItems = set(fileContent[index+1])
    thirdBagItems = set(fileContent[index+2])
    index+=3
    finalIntersection = firstBagItems.intersection(secondBagItems).intersection(thirdBagItems)
    
    for j  in finalIntersection:newScore+=letters.index(j)+1


print(newScore)