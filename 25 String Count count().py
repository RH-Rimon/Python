# count() is used to findout the number of specific letters in a sentence

a = "bangla"

print("Original String: %s" %a)
print("In \"Bangla\" number of 'a' is: ", a.count('a'))

print("In \"Bangla\" after 2 index number of 'a' is: ",a.count('a',2))

print(a.count('a',5,9))

sentence = "How can a clam cram in a clean cream can?"

print(sentence.count('c'))
print(sentence.count('c',5))
