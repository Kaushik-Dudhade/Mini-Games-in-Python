import random

n = int(input("Enter no. of players: "))
names = [''] * n
players = [0] * n

for i in range(n):
    names[i] = input(f'Player {i} name: ')

cur_score = 0

while True:
    play = input("Keep playing or quit? (p/q): ").lower()
    if play == 'q':
        quit()
    for i in range(n):

        cur_score = players[i]
        while True:
            command = input(f'Pass/Roll for {names[i]}: (p/r) ').lower()
            if command == 'p':
                players[i] = cur_score
                break

            roll = random.randint(1,6)
            if roll == 1:
                cur_score = 0
                players[i] = 0
                print(f'You got {roll}, score =', cur_score, " Next player")
                break

            cur_score += roll
            print(f'You got {roll}, score =', cur_score)
            if cur_score >= 50:
                print(names[i], " won !!")
                quit()


#hack


