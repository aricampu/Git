import random

def play():
    user = input("Que eliges? 'r' piedra, 'p' para papel, 's' para tijeras\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'Es un empate'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'Ganaste!'

    return 'Perdiste!'

def is_win(player, opponent):
    # Retorna true si player gana
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
