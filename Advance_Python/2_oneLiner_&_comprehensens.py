
""" a=20

if a % 2 == 0:
    print("even number")
else:
    print("odd number")
 """
# a=230

# print("even number") if a % 2 ==0 else print("odd number") # ternary oprators

""" COMPREHENSIONS """

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]

# for i in a:
#     if i%2==0:
#         b.append(i)   

# print(a)
# print(b)
"""  by  using comprehensions we can shorten it"""

a=[1,2,3,4,5,6,7,8,9,10]

b=[i for i in a if i%2==0]

print(b)