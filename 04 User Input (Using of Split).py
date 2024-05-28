#We can take two input at a time by using input().split()

num1, num2 = input().split()

num1 = int(num1)
num2 = int(num2)
sum = num1+num2
mul = num1*num2

print('Sum is:', sum)
print('Multiplication is:', mul)
