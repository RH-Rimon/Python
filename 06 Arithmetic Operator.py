"""" + --> Add
    - --> Sub
    * --> Multiply
    / --> Division
    % --> Modulus (for remainder)
    ** --> Exponent Operator
    // --> Floor division operator(Ignore number after decimal point) """

num1 = int(input())
num2 = int(input())

result = num1 ** num2

print('Result','=', result)

num3, num4 = input().split()

num3 = int(num3)
num4 = int(num4)

result = num3//num4

print('Result', result)