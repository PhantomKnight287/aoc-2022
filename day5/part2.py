from os import getcwd
from time import time

startTime = time()

with open(f"{getcwd()}/input.txt", "r") as f:
    lines = f.readlines()

    stack = {"start": 0, "end": None}
    instructions = {"start": None}

    stacks = {}
    for f in lines:
        if f in ["\n", "\r\n"]:
            instructions["start"] = lines.index(f)+1
            stack["end"] = lines.index(f)-1

            _stacks = lines[stack["end"]]
            for index, s in enumerate(_stacks):
                if s in [" ", "\n"]:
                    continue
                stacks[s] = []
                for idx, l in enumerate(lines):
                    if (idx == stack["end"]):
                        break
                    item = l[index]
                    if item not in [" ", "]", "["]:
                        stacks[s].append(item)
            # print(stacks)
            for l in lines[instructions["start"]:]:
                if l not in ["\n", "\r\n"]:
                    l = l.replace("\n", "").split()
                    if (int(l[1]) == 1):
                        stacks[f"{l[5]}"] = [
                            stacks[f"{l[3]}"].pop(0), *stacks[f"{l[5]}"]]

                    else:
                        for i in range(0, int(l[1])):
                            stacks[f"{l[5]}"].insert(i,stacks[f"{l[3]}"].pop(0))

    required_sq = ""
    for k in stacks.keys():
        required_sq += stacks[f"{k}"][0]
    print(required_sq)

endTime = time()

print(f"The Shitty code took: {endTime-startTime}ms")
