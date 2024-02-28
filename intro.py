# user_input=input("enter your age: ")
# print(user_input)
# result=not(2>4)
# print(result)

# a=11//3   floor operator (devision)
# print(a)

# a=2
# if a>1:
#  print(a)
# print(a>1) 

# a=["suraj","sudhir","sujal"]
# for i in a:
#     print(i)
#     for j in i:
#         print(j)

# a=["suraj","sudhir","sujal"]
# for i in a[::-1]:
#     print(i)
#     for j in i:
#         print(j)

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()    
        
# for i in range(1,10,2):
#     print(i,end=" ")

# a = int(input(""))
# b = int(input(""))
# c = a + b
# print(c)

# x=int(input())
# y=int(input())
# print(x*y)

# x,y=map(int,input().split())
# print(x,y)

# for i in range(1,5,2):
#     print(i)   
#     print(f"number{i}")


# l=[1,2,3,4]
# s_l=[]
# for i in l:
#         s_l.append(i**2) 
# for i in s_l:
#         print(i,end=" ")

# i=0
# while i<10:
#     print(i,end=" ")
#     i+=2

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=(" "))
#     print()

# def a(name):
#     print(f"hello {name},how are you?")
# a("suraj")    

# def mul(x,y):
#     return x*y
# print(mul(4,5))


"""def arrgument(name,massage,* arg):
    print(name)
    print(massage)
    for a in arg:
     print(a)

arrgument("suraj hudda",'hi',1,2,3,4)"""


"""
doc string:
use of this function

x
y
operation

return

"""

# def cal(x,y,oper):
#     if(oper=='+'):
#        return x+y
#     elif(oper=='-'):
#        return x-y
#     elif(oper=='*'):
#        return x*y
#     elif(oper=='/'):
#        return x/y
# print(cal(2,5,"*"))


# anonymous function
# add=lambda a ,b :a+b
# print(add(1,2))

# sq=lambda a:a**2
# print(sq(3))

# cel_to_feh=lambda c: 9/5*c+32
# print(cel_to_feh(-40))

# complex number
# c=4+5j
# print(c.real)
# print(c.imag)  #hello mere jaan

"""
to show all keywords
print(help('keywords'))
"""
# x,y=map(int,input().split())
# print(x,y)

# name1=input('enter your name:')
# print(name1)

# a='suraj'
# print(a[0])
# print(a[-1])
# membership operator
# print('s' in a)
# print('v' not in a)

# a=3
# b=a
# print(a is b)

# bitwise operator
# & |
# print(18 & 3)
# print(bin(18))

# ~ negative
# print(~6)

# bitwise xor operator >> return 1 when exactly 1 operand is 1
# print(5^3)
# a=3
# b=4

# swaping two numbers
# a=a^b
# b=a^b
# a=a^b
# print(a,b)

# shift operator left & right
# left shift
print(35<<3)
# right shift
print(35>>3)