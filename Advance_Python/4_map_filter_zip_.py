#_________________[Map]_________________#
""" map transform the iterable """

ls = ["ansari ","shaikh", "khan","chauhan"]

#i need to return length of every string in the list by using map function respectively

Length = list(map(lambda a :len(a),ls))
print(Length)

temp_cel=[0,90,20,32,45,27]

def convertor(a):
    far =(a*9/5)+32
    return far

temp_far = list(map(convertor, temp_cel))
print(temp_far)

#________[Filter]____________#
"""  filter keeps the elements based on the condition  """

Age = [21,18,24,20,30,15,16,19]

result = list(filter(lambda a: a>=18,Age))
print(result)

#______[zip]_____#
""" zip combines coressponding elements into tuples """

name = ["ansari","shaikh", "khan", "chauhan"]
age = [25,24,22,21]
data = list(zip(name,age))
print(data)