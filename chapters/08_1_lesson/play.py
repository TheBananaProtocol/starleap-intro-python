
fruit = '🤣🤣🤔☺🐛'

index =4
while index < len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1



prefixes = 'TKLMNOPQ'
suffix = 'elker'

for letter in prefixes:
    print (letter + suffix)


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find)

word = banana

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')
