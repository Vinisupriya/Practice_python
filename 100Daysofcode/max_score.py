student_scores = input("Input a list of student scores ").split()
max=0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
for score in student_scores:
  if score > max:
    max = score
print(f"The highest score:{max}")