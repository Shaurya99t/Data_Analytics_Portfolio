# x=24
# print("first variable x",x)
# def hello():
#     global x
#     x=25
#     return x
# print(x)
# def max(a,b,c):
#     if a>b and a>c:
#         print("a is bigger",a)
#     elif b>a and b>c:
#         print("b is biggest",b)
#     else:
#         print("c is biggest",c)

# # max(23,34,131)
# def c_list():
#     l=[]
#     for i in range(1,31):
#         l.append(i**2)
#     return l
# print(c_list())
# def prime(num):
#     if num==1:
#         print("It is not a prime number")
#     if num==2:
#         print("It is not a prime number")
#     for i in range(2,num):
#         if num%i==0:
#             print("it is not a prime number")
#             break
#     else:
#         print("it is a prime number")

# prime(1012)

# def add(num):
#     sum =0
#     for i in num:
#         sum=sum+i
#     return(sum)
# print(12,13,23,2,13,63)
def fs(num):
    if num== 1:
        return(0)
    elif num == (2):
        return(1)
    else:
        return(fs(num-1)+fs(num-2))
print(fs(7))