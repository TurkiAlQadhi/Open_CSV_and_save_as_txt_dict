# import libraries to be used
import os
# initiate variables
NumberOfStudents = 0
InputFileName = "ResultsData.csv"
OutputFileName = "OutputInformation.txt"
# initiate two list to hole the name and scores and list of three character of the name
Names = []
Scores = []
three_char = []
# the following lines to be used to get the current working directory and change the location to it to get the ResultsSata.csv file.
cwd = os.path.dirname(os.path.abspath(__file__))
# print(cwd)
# change the directory to the current folder where we at
#print(cwd)
os.chdir(cwd)
csv_file = open(InputFileName, "r")
# And put it into an array/list
reading = csv_file.readlines()
new_file = open("OutputInformation.txt", "w")
for Line in reading:
    StudentLine = Line.strip()
    # Separate the Name and Score values See: https://www.w3schools.com/python/ref_string_split.asp
    StudentAndResult = StudentLine.split(",")
    # Append them to the appropriate Lists
    Names.append(StudentAndResult[0])
    Scores.append(float(StudentAndResult[1]))
    three_char.append(StudentAndResult[0][0:3])
    
    # Increase the number of students
    NumberOfStudents = NumberOfStudents + 1

diction = dict(zip(three_char,Scores))
#print(diction)
# Order the file in decending order
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
#print("\nSort (descending) the said dictionary elements by value:")
#print(sort_dict_by_value(diction, True))
# adding the - to the name
scored = " - "
name_scored = [ items + scored for items in Names]
print("\n" , name_scored)
# making scors as string to join it with the names
strscore = Scores
strscore = [str(Scores) for Scores in strscore]
print("\n" , strscore , "\n")
#join the two striings
combine = [name_scored + strscore for name_scored, strscore, in zip(name_scored, strscore)]
dictionary = sort_dict_by_value(diction, True)
with open(OutputFileName, 'w') as OP:
    for key, value in dictionary.items(): 
        OP.write('%s - %s\n' % (key, value))
new_file.close()
csv_file.close()
print ("Reading information from: ",  InputFileName)
print (NumberOfStudents, " records output to: ", OutputFileName) 

# End of you main program - nothing after this.

