def display(m):
    print(m)

def average_absent(m):
    sum = 0
    absent = 0
    
    for i in range(0,len(m)):
        if(type(m[i])==type(" ")):
            absent = absent+1
        else:
            sum = sum + m[i]
    average = sum/( len(m)-absent)
    print("students who are absent : ", absent)
    print("Average marks are : ", average)
        
        
def HighestAndLowestScore(m):
    high = 0
    low = 100
    for i in range(0,len(m)):
        if( type(m[i])!=type(" ")):
            if(m[i]>high):
                high = m[i]
            if((m[i]<low) and type(m[i])!=type(" ")):
                low = m[i]
    print("\n Highest Score is: ",high)
    print("\n Lowest Score is: ",low)

def Frequency(m):
    f = [0] #not storing the frequency at 0th location
    for j in range(1,100):
        count = 0
        for i in range(1,len(m)):
            if( type(m[i])!=type(" ")):
                if(m[i] == j):
                    count = count + 1
        f.append(count)
    print("\nThe marks in the subject 'Fundamentals of Data Structures' are...")
    print(m)
    #counting the highest frequency of the marks
    high = 0
    for cnt in f:
        if(cnt>high):
            high=cnt
    print("\n Highest Frequency is: ",high)
    
    #obtaining marks of highest frequency
    for k in range(1,len(f)):
        if(f[k] == high):
            highest_marks=k
    print("\n Highest Frequency Marks are: ",highest_marks)
def mainList():
    

    ch='y'
    
    while ch=='y':
        print("menu driven program for FDS test" ,"\n"
"********************************************** \n"
"1.input the marks \n 2.Average marks scored by the class and Number of students absent for exam \n 3.Maximum marks scored and Minimum marks scored \n 4.Highest Frequency of marks")
        choice = input("enter the choice : ")
        if (choice=='1'):
            display(m)
            
        elif(choice=='2') :
            average_absent(m)
            
        elif (choice=='3'):
            HighestAndLowestScore(m)
            
        elif(choice=='4'):
            Frequency(m)   
        else:
            print("INVALID OPERATION")
        ch= input("do you like to continue (Press Y to continue)")        



m= eval(input("enter the marks : "))
mainList()














