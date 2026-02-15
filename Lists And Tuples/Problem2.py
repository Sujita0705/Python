# Write a program to accept marks of six students and display them in a sorted manner.

marks =[]

m1 = int(input("Enter the marks of student 1: "))
m2 = int(input("Enter the marks of student 2: "))
m3 = int(input("Enter the marks of student 3: "))
m4 = int(input("Enter the marks of student 4: "))
m5 = int(input("Enter the marks of student 5: "))
m6 = int(input("Enter the marks of student 6: "))

marks.append(m1)
marks.append(m2)
marks.append(m3)
marks.append(m4)
marks.append(m5)
marks.append(m6)

print(marks)

marks.sort()
print(marks)