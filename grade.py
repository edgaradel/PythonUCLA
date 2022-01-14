def read_grades(gradefile):
    '''(file open reading) -> list of float
    Read and return the list of grades in the gradefile
 
    Precondition: gradefile starts with a header that contains no blank lines
    and then lines containting student id and grades
 
    '''
    # skip over the header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
    # read each line into a list
    grades = []
    line = gradefile.readline()
    while line != '':
        grade = line[line.rfind('') + 1 :]
        grade.append(float(grade))
        #print(line[line.rfind(" ") + 1:])
        line = gradefile.readline()
    return grades
 
def count_grade_ranges(grades_list):
    '''(list of float) -> list of int
    0-9: index 0
    10 - 19: 1
    :
    100 - 10
    >>>count_grade_ranges([77.5, 37.5, 0.5, 9.5, 72.5, 100.0, 55.0, 70.0, 79.5])
    [2, 0, 0, 1, 0, 1, 0, 4, 0, 0,1]
    '''
    range_counts = [0] * 11
    for grade in grades_list:
        which_count = int(grade // 10)
        range_counts[which_range] = range_counts[which_range] + 1
    return range_counts

def write_histogram(range_counts, histfile):
    '''(list of int, file open for writing) -> NoneType
    Write a histogram of * grades based on the number grades in each range
    Output Format:
 
    0-9:   **
    10-19: *
    20-29: *
    30-39: ***
    40-49: ******
    50-59: ********
    60-69: **
    70-79: *****
    80-89: *********
    90-99: ****
    100:   *
 
    '''
 
    histfile.write('0-9:   ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')
    
    # Write the 2-digit ranges.
    for i in range(1,10):
        low = i * 10
        high = low + 9
        histfile.write(str(low) + '-' + str(high) + ': ')
        histfile.write('*' * range_counts[i])
        histfile.write('\n')
    histfile.write('100:   ')
    histfile.write('*' * range_counts[10])

