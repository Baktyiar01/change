

from functools import wraps

def change_number_to_sharp(func):
    
    @wraps(func)
    def wrapper():
        number = func()
        result = ''
    
        for i in number[:-2]:
            result += '#'

        result += number[-2:]

        return result

    return wrapper



@change_number_to_sharp
def get_number():
    my_number = '+996700123456'
    return my_number


print(get_number())
