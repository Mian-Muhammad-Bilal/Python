# Q1
num = int(input("Enter number: "))
init=0
sum=0
print("The even numbers are: ")
while(init<num):
    print(init)
    sum+=init
    init=init+2
print("The sum is:", sum)
===================================================================
# Q2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
while num2 !=0:
    num1,num2 = num2 , num1%num2
    
print("HCF is: " ,num1)
===================================================================
# Q3
print("Enter the range, within you want to print prime numbers :")
st = int(input("From: "))
end = int(input("To: "))
for s in range(st,end+1):
     if s > 1:
       for i in range(2, s):
           if s%i==0:
               break
       else:
           print(s)
===================================================================
# Q4
num = int(input("Enter a decimel number: "))
fac = 1
if num < 0:
   print("negative number cannot have factorial.")
elif num == 0:
   print("The factorial of ",num," is 1")
else:
   for s in range(1,num + 1):
       fac = fac*s
   print("The factorial of ",num," is ",fac)

===================================================================
# Q5
num = int(input("Enter a decimel number: "))
bin = format(int(num), 'b')
print("The binary of ",num," is: ",bin)
