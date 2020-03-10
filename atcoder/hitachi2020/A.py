s = input()
next_word = 'h'
is_correct = False

for word in s:
    if word != next_word:
        print('No')
        exit()
    elif word == next_word:
        if next_word == 'h':
            next_word = 'i'
            is_correct = False
        elif next_word == 'i':
            next_word = 'h'
            is_correct = True

if is_correct:
    print('Yes')
else:
    print('No')
