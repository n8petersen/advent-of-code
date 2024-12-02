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
    # print(report)
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


def checkSafeTolerant(report):
    # if first report is safe, 2nd is safe too
    if checkSafe(report):
        return True
    
    # Try removing each number one at a time
    for i in range(len(report)):
        # Create new report without number at index i
        modified_report = report[:i] + report[i+1:]
        if checkSafe(modified_report):
            return True
    
    return False



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


    tolerantSafeReports = 0
    for report in reports:
        if (checkSafeTolerant(report)):
            tolerantSafeReports += 1
    print("Tolerant Safe Reports: " + str(tolerantSafeReports))


