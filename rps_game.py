import random


def rsp_game(comp, player):
    result = False
    if comp == 'rock' and player == 'paper':
        result = True
    elif comp == 'paper' and player == 'scissor':
        result = True
    elif comp == 'scissor' and player == 'rock':
        result = True
    return result

def game_play():
    rsp = ['rock', 'paper', 'scissors']

    while(True):
        print('Rock... Paper... Scissors... ')
        shoot = random.choice(rsp)
        shot = input('Shoot!\n')
        if shot.lower() not in rsp:
            print('Input is null')
        else:
            if shoot == shot.lower():
                print(f'I also played {shoot}. Its a tie!')
            elif rsp_game(shoot, shot.lower()):
                print(f'I play {shoot}. You did it!')
            else:
                print(f'I play {shoot}. Sorry for your lost!')
            new_game = input('Want to play again? (y/n)\n')
            if new_game.lower() == 'y':
                print('You ready!')
                continue
            else:
                print('Well at least you tried!')
                break

game_play()







