print("welcome to max and min mark finder")

students_marks = input("Input a list of student marks : ").split()


for n in range(0, len(students_marks)):
  students_marks[n] = int(students_marks[n])
print(students_marks)

max_number = 0
for max in students_marks :
  if max > max_number :
    max_number = max 
print(max_number)

min_number =0
for min in students_marks :
  if min < min_number:
    min_number = min
print(min_number)