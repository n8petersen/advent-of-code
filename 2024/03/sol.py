import os

def cleaner(in_file):
    clean_file = []
    
    for line in in_file:
        # Initialize empty result for this line
        clean_line = ""
        i = 0
        
        while i < len(line):
            # Look for "mul" followed by proper format
            if line[i:i+3] == "mul" and i+3 < len(line):
                if line[i+3] == "(":
                    # Try to extract numbers between parentheses
                    j = i + 4
                    num1 = ""
                    while j < len(line) and line[j].isdigit() and len(num1) < 3:
                        num1 += line[j]
                        j += 1
                        
                    if j < len(line) and line[j] == "," and num1 != "":
                        j += 1
                        num2 = ""
                        while j < len(line) and line[j].isdigit() and len(num2) < 3:
                            num2 += line[j]
                            j += 1
                            
                        if j < len(line) and line[j] == ")" and num2 != "":
                            # Valid mul instruction found
                            clean_line += f"mul({num1},{num2})"
                            i = j + 1
                            continue
            
            i += 1
            
        if clean_line:
            clean_file.append(clean_line)
    
    return clean_file

def calculator(line):
    total = 0
    i = 0
    
    while i < len(line):
        if line[i:i+3] == "mul":
            # Find the numbers between parentheses
            start = line.find("(", i) + 1
            end = line.find(")", i)
            if start > 0 and end > 0:
                nums = line[start:end].split(",")
                # Multiply the two numbers and add to total
                total += int(nums[0]) * int(nums[1])
                i = end + 1
                continue
        i += 1
        
    return total




# main
if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    # input = "input_ex"
    input = "input"
    
    with open(dir + "\\" + input, "r") as in_file:
        clean_file = cleaner(in_file)

    sol = 0
    for line in clean_file:
        sol += calculator(line)

    print("Part 1: " + str(sol))