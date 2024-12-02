import os
import copy

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

def getDistances(left, right):
    distances = []

    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        distances.append(diff)
    
    return sum(distances)


# main
if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = "input"
    
    with open(dir + "\\" + input, "r") as in_file:
        left, right = parser(in_file)

        left_sorted = copy.deepcopy(left)
        right_sorted = copy.deepcopy(right)
        left_sorted.sort()
        right_sorted.sort()

        distance = getDistances(left_sorted, right_sorted)
        print("Total Distance: " + str(distance))

        print("Done!")
