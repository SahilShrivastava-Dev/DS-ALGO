x= eval(input("enter the list of students: "))
print("total number of students in class are", len(x) ,"\n"
"the sum of all students marks is : ", sum(x) ,"\n"
"the average of all student marks is : ", sum(x)/len(x),"\n"
"the maximum of all student marks is : ", max(x),"\n"
"the minimum of all student marks is : ", min(x))
y=0
for i in x:
    if i ==-1:
        y+=1

print("student who were absent in exams : ", y)     


