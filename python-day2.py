## prime or not
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:  
        count += 1  
if count == 2:
    print(n, "is prime")
else:
    print(n, "is not prime")



#output:

Enter a number: 7
7 is prime
Enter a number: 6
6 is not prime



##find factorial of a number
n=int(input("enter a number: "))
fact = 1
for i in range(1,n+1):
      fact *=i
print("factorial of",n,"is",fact) 

#output

enter a number: 3
factorial of 3 is 6

enter a number: 7
factorial of 7 is 5040


enter a number: 1
factorial of 1 is 1


## fibonacci series
n=int(input("enter a number: "))
f1=0
f2=1
print(f1,f2, end=' ')
f3 = f1 + f2
while(f3<=n):
    print(f3, end=' ')
    f1 = f2
    f2 = f3
    f3 = f1 + f2

##output
enter a number: 7
0 1 1 2 3 5

enter a number: 80
0 1 1 2 3 5 8 13 21 34 55

## sum of digits of a number
n = int(input("enter a number: "))
a = n
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r
    n = n // 10
print("sum of digits of", a, "is", sum)


##output
enter a number: 67872
sum of digits of 67872 is 30

enter a number: 08102004
sum of digits of 8102004 is 15



##Reverse of a given number
n=int(input("enter a number: "))
rev=0
a = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev*10 + r
    n = n // 10
print("The reverse of", a, "is", rev)

#output

enter a number: 08102004
The reverse of 8102004 is 4002018

enter a number: 30082006
The reverse of 30082006 is 60028003





     
