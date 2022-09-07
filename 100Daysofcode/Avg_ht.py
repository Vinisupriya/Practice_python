
student_heights = input("Input a list of student heights ").split()
sums= 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sums += student_heights[n]
avg = round(sums / (n+1))
print(avg)
