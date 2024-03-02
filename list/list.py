letters = ['a','b','c']
matrix=[[0,1],[2,3]]
zeros=[0]*100
#print(zeros)
combined=zeros+letters
#print(combined)
numbers = list(range(20))
#print(numbers)
chars = list("hello world")
#print(chars)
#print(len(chars))

letters = ['a','b','c','d']
#print(letters[0])
#print(letters[-1])
letters[0]='A'
#print(letters)
# print(letters[0:3])
#print(letters[::2])
numbers = list(range(20))
#print(numbers)
#print(numbers[::2])
#print(numbers[::-1])

#unpacking list
numbers = [1,2,3,4,5,5,5,5,4]
first, second,*other,last = numbers
#print(first , last)
#print(other)

letters = ['a','b','c']
# for letter in enumerate(letters):
#     print(letter[0],letter[1])
    
#add
letters.append('d')
letters.insert(0,'-')
print(letters)

#remove
# letters.pop(0)
# letters.remove('b')
# del letters[0:3]
# print(letters)

print(letters.index('a'))
print(letters.index('e'))



