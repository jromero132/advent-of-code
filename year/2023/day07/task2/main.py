"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=7 ; task=2)
"""

import sys


def get_card_value(card: str) -> int:
    if card.isdigit():
        return int(card)

    return {"A": 14, "K": 13, "Q": 12, "T": 10, "J": 1}[card]


def get_hand_evaluation(hand: str) -> int:
    card_dic = {}
    jokers = 0
    for card in hand:
        if card == "J":
            jokers += 1

        else:
            card_dic[card] = card_dic.get(card, 0) + 1

    card_cnt = sorted(card_dic.values(), reverse=True)
    if card_cnt:
        card_cnt[0] += jokers

    else:
        card_cnt = [5]  # Since all cards were jokers

    match card_cnt[0]:
        case 5:  # Five of a kind
            return 6

        case 4:  # Four of a kind
            return 5

        case 3:  # Full house or three of a kind
            return 4 if card_cnt[1] == 2 else 3

        case 2:  # Two pair or one pair
            return 2 if card_cnt[1] == 2 else 1

        case _:
            return 0  # High card


def main() -> None:
    hands = [line.strip().split() for line in sys.stdin]
    hands_eval = [
        (
            get_hand_evaluation(hand[0]),
            tuple(get_card_value(c) for c in hand[0]),
            hand[0],
            int(hand[1]),
        )
        for hand in hands
    ]
    print(sum(i * hand[-1] for i, hand in enumerate(sorted(hands_eval), start=1)))


if __name__ == "__main__":
    main()
