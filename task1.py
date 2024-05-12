i = 1
subjects = list()
while i == 1:
    subject = input("Enter the name of the subject: ")
    subjects.append(subject)
    i = int(
        input("If you wish to add more subjects Press 1 or any other kry to exit: ")
    )


total_subjects = len(subjects)
print(subjects, total_subjects)

# jump = 1
marks = []
for n in range(total_subjects):
    mark = int(input(f"Enter the Marks of {subjects[n]} : "))
    marks.append(mark)
    # final_list.insert(jump, marks)
    # jump += 2


print(subjects)
final_dict = {}
for i in range(total_subjects):

    final_dict[subjects[i]] = marks[i]

print(final_dict)


def find_sum(arr):
    i = 0
    total_marks = 0
    while i < len(arr):
        total_marks += arr[i]
        i += 1
    return total_marks


print("Total Marks obtained are :", find_sum(marks))


def find_min(arr):
    i = 0
    min_marks = 10000

    while i < len(arr):
        if arr[i] < min_marks:
            min_marks = arr[i]
        i += 1
    return min_marks


print("Minimum Numbers obtained are :", find_min(marks))


def find_max(arr=[9, 7], ar2=[12, 3]):
    i = 0
    max_marks = 0
    while i < len(arr):

        if arr[i] > max_marks:
            max_marks = arr[i]
        i += 1
    return max_marks


print("Maximum Numbers obtained are :", find_max(ar2=[78, 8], arr=[6, 7]))


def find_average(sum, arr):
    return sum / len(arr)


print("Average Marks for all subjects : ", find_average(find_sum(marks), marks))


arr = [1, 2, 3, 4]

a = lambda x: x if x == 2 else -1


def fun(x):
    if x == 2:
        return x
    else:
        return -1


def higher(fun1):
    print("about to call fun...")
    fun1(8)


b = fun

higher(b)

print(a(4))


class A:
    def __init__(self):
        print("Constrructeoreuoiehf...")


a = A()


f = open("python practice/task1.py", "r")

for a in f:
    print(a)


a = "popop"


sub = a == a[::-1]
print(sub)
