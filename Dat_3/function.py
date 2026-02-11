# def rect(length,width):
#     print("the area of the rectangle is",length*width)
# rect(12,32)
# def hello(*name):
#     print("hello, my name is",name[1])
# hello("lisa","jhon","peter")
# def hello():
#     return("hello world")

# print(hello())

# def hello():
#     print("hello")
#     return hello()
# print(hello())

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print(fact(5))
