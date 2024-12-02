import os

# Part 1
def parser(in_file):
    left = []
    right = []
    
    for line in in_file:
        # print(line)
        nums = line.strip().split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    
    return left, right

def getDistances(left, right):
    left.sort()
    right.sort()
    distances = []

    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        distances.append(diff)
    
    return sum(distances)

# Part 2
def getSimilarity(num, right):
    count = 0
    for r in right:
        if r == num:
            count += 1
    return num * count


# main
if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    # input = "input_ex"
    input = "input"
    
    with open(dir + "\\" + input, "r") as in_file:
        left, right = parser(in_file)

        distance = getDistances(left, right)
        print("Total Distance: " + str(distance))

        similarity_score = 0
        for i in range(len(left)):
            sim = getSimilarity(left[i], right)
            similarity_score += sim
        print("Similarity Score: " + str(similarity_score))


