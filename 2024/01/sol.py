import os

# Part 1
def parser(in_file):
    left = []
    right = []
    
    for line in in_file:
        print(line)
        nums = line.strip().split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    
    return left, right

# main
if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = "input_ex"
    
    with open(dir + "\\" + input, "r") as in_file:
        left, right = parser(in_file)
        print(left)
        print(right)