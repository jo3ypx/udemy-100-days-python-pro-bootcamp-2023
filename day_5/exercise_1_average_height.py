student_heights = input("Input a list of student heights:\n").split()
average_height = 0
sum_height = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_height += student_heights[n]

average_height = round(sum_height / len(student_heights))
print(average_height)
