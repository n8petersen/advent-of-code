import os

# Part 1
def parser(in_file):
    left = []
    right = []
    
    for line in in_file:
        print(line)

# main
if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = "input_ex"
    
    with open(dir + "\\" + input, "r") as in_file:
        left, right = parser(in_file)
        