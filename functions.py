
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))
    

def cube(num):
    return num**3

result = cube(4)
print(result)

def gender(is_male, is_tall):
    if is_male and not(is_tall):
        print("You are a short male")
    elif is_male and is_tall:
        print("You are a tall male")
    elif not(is_male) and is_tall:
        print("You are not a male but are tall")
    else:
        print("You are neither male nor tall")
        
is_male = False
is_tall = True
result2 = gender(is_male, is_tall)


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    

print(max_num(5, 6, 200000000))

