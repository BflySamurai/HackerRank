#https://www.hackerrank.com/challenges/finding-the-percentage

N = int(raw_input()) #Get the number of students
my_dict = {} #Instantiate the dictionary

#Map input data into dictionaries
for i in range(0,N):
    new_entry = raw_input().split(" ") #Parse the input string
    student = new_entry[0] #Get the name of the student out of the parsed data
    grades = map(float, new_entry[1:]) #Get the grades of the student out of the parsed data as float
    my_dict[student] = grades #Add the student and their grades to the dictionary
    i += 1

#Find the average grade of particular student
my_name = raw_input() #Get the name of the student we want to know about
if (my_name in my_dict):
    data = my_dict[my_name] #Get the person's data
    average_grades = sum(data) / float(len(data)) #Average the person's grades
    print("%.2f" % average_grades) #Print their averaged grades to 2 decimal places
else:
    print ("Student records do not exist.")