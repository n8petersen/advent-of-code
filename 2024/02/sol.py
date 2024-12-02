import os

# Part 1
def parser(in_file):
    reports = []
    
    for line in in_file:
        report = [int(x) for x in line.strip().split()]
        # print(report)
        reports.append(report)
    
    return reports

def checkSafe(report):
    print(report)
    ## Check if increasing
    increasing = True
    for i in range(len(report)-1):
        if report[i] >= report[i+1] or abs(report[i] - report[i+1]) > 3:
            increasing = False
            break
    
    ## Check if decreasing 
    decreasing = True
    for i in range(len(report)-1):
        if report[i] <= report[i+1] or abs(report[i] - report[i+1]) > 3:
            decreasing = False
            break
            
    if not increasing and not decreasing:
        return False
    
    return True


# main
if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    # input = "input_ex"
    input = "input"
    
    with open(dir + "\\" + input, "r") as in_file:
        reports = parser(in_file)

    safeReports = 0
    for report in reports:
        if (checkSafe(report)):
            safeReports += 1
    print("Safe Reports: " + str(safeReports))


