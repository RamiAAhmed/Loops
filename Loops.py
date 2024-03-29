#Q1
numbers = [12,75,150,180,145,525,50]

for number in numbers:
    if number%5==0 and number <=150:
        print(number)
    elif number>500:
        break    

#Q2
number_d=input("Eneter a number ")
i=1
while i <len(number_d):
    i+=1
print(i)

#Q3
list_1=[10,20,30,40,50]
for i in reversed(list_1):
    print(i)

#Q4
for i in range(-10,0):
    print(i)
    i+=1

#Q5
num=int(input("Enter a number for muliplication "))
for x in range (1,11):
    print(x*num)

#Q6
list=[0,1]
for i in range (0,10):
    num_list= list[i]+list[i+1]
    list.append(num_list)
print(list)
