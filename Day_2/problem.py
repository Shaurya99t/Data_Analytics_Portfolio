# a=0
# b=1
# print(a,end=" ")
# print(b, end=" ")
# for i in range(2,100):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
# num = int(input("Enter the number"))
# for i in range (2,num):
#     if num%i==0:
#         print("Not prime")
#         break
# else:
#     print("Prime")
    
# a= input("Enter the number")
# b=a[::-1]
# if a==b:
#     print("Plendrom")
# else:
#     print("NOt palendrom")
# num = int(input("Enter the number"))
# temp=num
# rev=0
# while num >0:
#     dig =num%10
#     rev= rev*10+dig
#     num = num//10
# if rev ==temp:
#     print("Palindrom")
# else:
#     print("Not Palindrom")

# a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# b=a.split(".")
# print(b)
# c= a.replace(".","")
# c= sorted(a)
# print(c)
# b= a.count("O")
# print(b)
a = input("Enter anything")
vowels=0
for i in a:
    if i=="a" or i=="e" or i=="o" or i=="i" or i=="u" or i=="A" or i=="E" or i=="O" or i=="I" or i=="U":
        vowels+=1
print("Vowels in string are",vowels)