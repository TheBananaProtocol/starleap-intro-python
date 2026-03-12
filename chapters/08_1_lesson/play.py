
fruit = '🤣🤣🤔☺🐛'
banana = 'banana'
prefixes = 'TKLSNOGJ'
suffix = 'ello world'
index =4
word = 'william'



while index < len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1



new_word = word.upper()

print(new_word)


for letter in prefixes:
    print (letter + suffix)



def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)



if word < 'banana':
    print(' hey, ' + word + ', arhhhhhhgggg.')
elif word > 'banana':
    print('hey, ' + word + ', no white monters for you.😈')
else:
    print('All right, bananas.')



