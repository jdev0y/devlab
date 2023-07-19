print("Feature")

def get_value(x):
    return x + 5

try:
    x = int(input('select number'))
    result = get_value(x)
    print(result)
except ValueError:
    print('please add a valid intger')

