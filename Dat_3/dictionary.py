# employee={"name":"john","age":34,"gender":"male"}
# print(employee)
# print(employee["age"])
# for i in employee:
#     print(i)
# for i in employee:
#     print(employee[i])
#     print("using value function")
#     for x in employee.values():
#         print(x)
# print("using item function")
# for x,y in employee.items():
#     print(x,y)
# x=employee.get("name")
# print(x)
# a=employee.items()
# print(a)
# b=employee.keys()
# print(b)
# c=employee.values()
# print(c)
# d=employee.copy()
# print(d)
# employee={1:{"name":"john","age":34,"gender":"male"},
#           2:{"name":"rohn","age":24,"gender":"male"},
#           3:{"name":"cvbk","age":54,"gender":"male"},
#           4:{"name":"dfgf","age":24,"gender":"male"}}
# print(employee[2]["age"])
a={"a":22,"b":21,"c":32,"d":73,"e":43}
a=sorted(a.values())
print(a)
b={}
for i in range (1,5):
    b[i]=i**3
print(b)
mul=1
for i in b:
    mul*=b[i]
print(mul)
c={21:"a",23:"b",54:"c",43:"d",35:"e",37:"f"}
c=sorted(c.keys())
print(c)