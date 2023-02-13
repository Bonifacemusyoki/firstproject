dict={"names" :["James", "ken", "Joy"]}
print(dict.get("names"))



pens={"brand1" : {"name" : "bic"},
"brand2" : {"name" : "obama"}}
print(pens["brand2"] ["name"])


def my_function(first_name):
    print(first_name+ "hello")


my_function("cynthia ")

def my_function(first_name):
    print("hello "+ first_name)

my_function(input("Enter your name:"))


num1=eval(input("Enter num1:"))5
num2=eval(input("Enter num2"))
sum_1=num1+num2
print(sum_1)