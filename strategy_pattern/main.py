import sys

from player import Player
from prob_strategy import ProbStrategy
from hand import Hand
from winning_strategy import WinningStrategy


def main() -> None:
    args = sys.argv
    if len(args) != 3:
        # TODO:コメント
        print('python main ..')
        exit(0)

    seed1: int = int(args[1])
    seed2: int = int(args[2])
    player1: Player = Player('Taro', WinningStrategy(seed1))
    player2: Player = Player('Hana', ProbStrategy(seed2))

    for _ in range(10):
        next_hand1: Hand = player1.next_hand()
        next_hand2: Hand = player2.next_hand()
        if next_hand1.is_stronger_than(next_hand2):
            print(f'Winner:{player1}')
            player1.win()
            player2.lose()
        elif next_hand1.is_weeker_than(next_hand2):
            print(f'Winner:{player2}')
            player1.lose()
            player2.win()
        else:
            print('Even...')
            player1.even()
            player2.even()

    print('Total result:')
    print(player1)
    print(player2)


if __name__ == '__main__':
    main()
