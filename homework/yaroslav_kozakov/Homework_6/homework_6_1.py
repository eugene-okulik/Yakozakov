# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову)
# в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка, этот знак препинания должен идти
# после того же слова, но уже преобразованного

text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
    + 'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
words = text.split()  # split by method split string to the list
new_words = []  # create a new list where will be added w+ing words
for word in words:  # go through the all words by the loop for in a list with a words
    new_words.append(word + 'ing')  # add to the end of each word of a splitted list a part 'ing'
new_words2 = []  # create a new list with w+ing words where will be adjusted a punctuation
for word in new_words:  # go through the all words by the loop for in a list with a w+ing words
    if ',' in word:
        new_words2.append(word.replace(',ing', 'ing,'))  # change in a final list a punctuation of w+ing words with ','
    elif '.' in word:
        new_words2.append(word.replace('.ing', 'ing.'))  # change in a final list a punctuation of w+ing words with '.'
    else:
        new_words2.append(word)  # or add a w+ing word to the final list it it doesn't consist of punctuation marks
print(' '.join(new_words2))  # collect all the worked out words from the final list back into the text
