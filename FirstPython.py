print("Hello ML/AI COURSE" )
A= 9;
B=5;
print(A+B)

a= 6+6+6+6;
b=1;
print(a+b)
b=6*9;
a=6;
print(a+b)
# print("my name is pooja ", "I am working as salesforce developer ")----Press ctl+ /
Name="pooja"
age=24
price=90.90
print(Name,age,price)

Age=25
age1= Age
print(age1)
print(type(Name))
print(type(age))
print(type(price))

a= 5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(b**a)
print(a)
str="I am pooja bharti as a salesforce developer\n.Now currently working with this CRM."
print(str)
str1= "pooja "
print(len(str1))
str2 ="apna company"
print(str2[1:6])
print(str2[3:])
# str3=" I love Python"
# print(str3.replace{"python" , "java"})
text = "I love python"
print(text.replace("python", "java"))

age1= 10

if(age1>=18):
    print("can vote & apply the licence")

elif(age1 <10):
    print("can be get licence only not use it")    

else:
    print("not applicable for vote")


marks = 85

if (marks >90):
    grade ="A"
elif(marks >80  and marks<90):
    grade ="b"
else:
    grade ="c"    
print("student of grade", grade)    

# List in python
marks =["pooja" ,89 ,"bharti" ,90,"developer"]
print(marks[0:10])


# check number is palindrome or not 
List1=[1 ,2 ,1]
Copy_List1= List1.copy()
Copy_List1.reverse()
if(Copy_List1 ==List1):
    print('palindrome')
