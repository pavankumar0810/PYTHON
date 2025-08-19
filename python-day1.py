## Reverse a String
a="pavan"
b=a[::-1]
print(b)

##output:
navap

## given string palindrome or not
a=input("enter a string:")
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")

##output
    enter a string:pavan
            not palindrome
    entera string:madamimadam
            palindrome


##count no.of vowels and consonants in a string
n = input("enter a string: ")
vowels_count=0
consonants_count=0
vowels="AEIOUaeiou"
for i in n:
    if i in vowels:
        vowels_count +=1
    else:
         consonants_count +=1
print("vowels_count: ",vowels_count)
print("consonants_count: ",consonants_count)

##output
enter a string: pavan
vowels_count:  2
consonants_count:  3

## Remove spaces from a given string
a = input("enter a string: ")
b=a.replace(" ","")
print(b)

#output
enter a string: pavan kumar
pavankumar


##count the frequency of the each character of a string
a = input("enter a string: ")
freq = {}
for char i a:
    freq[char] = freq.get(char,0)+1
print("character frequencies:")
for char,count in freq.items():
    print(char, ":",count)

##output 
enter a string: pavan
character frequencies:
p : 1
a : 2
v : 1
n : 1












