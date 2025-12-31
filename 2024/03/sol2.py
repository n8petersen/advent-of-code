import os
import re

# def findMults(file):
#     matches = []
#     for line in file:
#         regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
#         find = regex.findall(line)
#         matches.append(find)
#     return matches

# def runMults(file):
#     sum = 0
#     for line in file:
#         for mult in line:
#             sum += sum([a * b for (a, b) in mult])

PATTERN = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')


def parse_multiplies(string):
    matches = PATTERN.findall(string)
    matches = [(int(a), int(b)) for (a, b) in matches]

    return matches


# main
if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = "input_ex"
    # input = "input"
    
    sol = 0
    
    with open(dir + "\\" + input, "r") as in_file:
    #     mults = findMults(in_file)
        parse_multiplies(in_file)
    
    # sol = runMults(mults)


    print("Part 2: " + str(sol))