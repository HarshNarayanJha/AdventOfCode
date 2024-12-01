
from collections import Counter


class Card:
    def __init__(self, label: str) -> None:
        self.label = label
        self.strength = ['2', '3', '4', '5','6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'].index(label) + 1

    def __repr__(self) -> str:
        return self.label
    
    @staticmethod
    def get_card_strength(label):
        return ['2', '3', '4', '5','6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'].index(label) + 1

class Hand:
    def __init__(self, cards: "list[str]", bid: int) -> None:
        self.cards = cards
        self.bid = bid
        self.internal_rank = self.hand_to_value()
        # print(set(self.cards))
        # if len(set(self.cards)) == 1:                       # five of a kind AAAAA
        #     self.internal_rank = 7
        # elif len(set(self.cards)) == 2:
        #     if self.cards.count(max(self.cards)) == 4:      # Four of a Kind AA8AA
        #         self.internal_rank = 6
        #     elif self.cards.count(max(self.cards)) == 3 and self.cards.count(min(self.cards)) == 2:    # Full House 23332
        #         self.internal_rank = 5
        #     elif self.cards.count(max(self.cards)) == 3 and self.cards.count(min(self.cards)) == 1:    # Three of a kind TTT98
        #         self.internal_rank = 4
        # elif len(set(self.cards)) == 3:
        #     if self.cards.count(max(self.cards)) == 3:      # Four of a Kind AA8AA
        #         self.internal_rank = 4
        #     elif self.cards.count(max(self.cards)) == 2:
        #         self.internal_rank = 3                          # Two Pair 23432
        # elif len(set(self.cards)) == 4:                         # One Pair A23A4
        #     self.internal_rank = 2
        # elif len(set(self.cards)) == 5:
        #     self.internal_rank = 1

    def hand_to_value(self) -> int:
        match sorted(Counter(self.cards).values()):
            case [5]:  # 5 of a kind
                return 7
            case [1, 4]:  # 4 of a kind
                return 6
            case [2, 3]:  # full house
                return 5
            case [1, 1, 3]:  # 3 of a kind
                return 4
            case [1, 2, 2]:  # 2 pair
                return 3
            case [1, 1, 1, 2]:  # 1 pair
                return 2
            case [1, 1, 1, 1, 1]:  # high card
                return 1
            case _:
                raise ValueError(f"unknown hand: {self.cards} ({sorted(Counter(self.cards).values())})")

    def __lt__(self, other: "Hand") -> bool:
        if self.internal_rank == other.internal_rank:
            for i in range(len(self.cards)):
                if Card.get_card_strength(self.cards[i]) != Card.get_card_strength(other.cards[i]):
                    return Card.get_card_strength(self.cards[i]) < Card.get_card_strength(other.cards[i])
        else:
            return self.internal_rank < other.internal_rank

    def __gt__(self, other: "Hand") -> bool:
        if self.internal_rank == other.internal_rank:
            for i in range(len(self.cards)):
                if Card.get_card_strength(self.cards[i]) != Card.get_card_strength(other.cards[i]):
                    return Card.get_card_strength(self.cards[i]) > Card.get_card_strength(other.cards[i])
        else:
            return self.internal_rank > other.internal_rank

    def __repr__(self) -> str:
        return f"{''.join(self.cards)} {self.bid}"

with open("input7.txt", 'r') as fp:
    lines = fp.read().split("\n")

data = {}
for line in lines:
    cards, bid = line.split()
    data[cards] = int(bid)

hands: "list[Hand]" = []
for d in data:
    cards = []
    for ch in d:
        cards.append(ch)
    hands.append(Hand(cards, data[d]))


# print(hands[0].internal_rank)
print([(x, x.internal_rank) for x in hands])
hands_sorted = sorted(hands)

answer = 0
for rank, hand in enumerate(hands_sorted, start=1):
    answer += rank * hand.bid

print(answer)