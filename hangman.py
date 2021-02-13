import random

lines = open('scrabblewords.txt', 'r')

answer = random.choice(lines.read().split())
answer = answer.lower()
lines.close()
print(answer)

viewer_list = []
for i in range(len(answer)):
    viewer_list.append('_')
print(viewer_list)
wrong_guesses = 0

while wrong_guesses < 6:
    guess = '                     '
    while len(guess) != 1:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please only enter one letter.')
    if guess in answer:
        for i in range(len(answer)):
            if guess == answer[i]:
                viewer_list[i] = guess
    else:
        print(f'{guess} is not in word.')
        wrong_guesses += 1
    print(viewer_list)
    if ''.join(viewer_list) == answer:
        break

if ''.join(viewer_list) == answer:
    print('You have correctly guessed all the letters!')
else:
    print('You have lost. :/(')