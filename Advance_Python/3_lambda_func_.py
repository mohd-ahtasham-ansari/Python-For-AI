#________________[Lambda expression]________________#

""" normal code function """
def check(a):
    if a%2==0:
        print("even number")
    else:
        print("odd number")

check(10)

""" by using lambda code """

check = lambda a:print("even number") if a%2==0 else print("odd number")

check(19)
check(40)

addition = lambda a,b: a+b

print(addition(10,20))

#_________{lambd using k args with **args}____________#
total_sum = lambda *args: sum(args)

print(total_sum(10,20,30,40,50))

