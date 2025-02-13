# print("hello", name)
# name = input("what is your name?")
# print("hello", name)
#
# '''
# This is a multiline
# comment.
# '''

# Task 1
print("Hello World")

# Task 2
print("Hello, Joshua!")

# Task 3
# over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
# converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
# displays both.

Celsius=input("What is the temperature in celsius?")
fahrenheit=float(Celsius)*1.8+32
print("The temperature in Fahrenheit is", fahrenheit)

# Task 4
# In a long career for Yorkshire, Geoﬀrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate
# and display Boycott's batting average.
# Note: A batting average is the number of runs scored divided by the number of
# completed innings (i.e. the total times batted minus the times not out).

total_runs = 48426
total_innings=1014
not_outs=162

completed_innings=total_runs-not_outs
batting_average=total_runs/completed_innings
print(f"The batting average is: {batting_average}")

# Task 5
# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "le  over"
# group

lab_size = 24
students_list = [113,175,12]

for student in students_list:
    full_groups = student // lab_size
    leftover_students = student % lab_size

    print(f"For {full_groups} groups, {leftover_students} leftovers")
