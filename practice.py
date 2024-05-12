a = int(input("Enter the number of inputs: "))
marks=[]

for _ in range(a):
    marks.append(int (input("Enter the marks of student")))
print(marks)

#finding sum
total_marks=sum(marks)
print("Sum = ",total_marks)

min_marks=min(marks)
print("Minimum Marks", min_marks)

max_marks=max(marks)
print("Maximum Marks",max_marks)

average = total_marks/a
print("Average of Marks = ", average)

from task1 import fun as new_fun

new_fun()