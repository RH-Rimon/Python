

fruits = {'apple','orange','banana','pear','pineapple'}

""" We can only use remove() function to delete an item from set if it's 
exists. Otherwise it will be through KeyError"""


fruits.remove('orange')

print(fruits)

fruits.remove('grap')

print(fruits)