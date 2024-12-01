def parse(puzzle_input):
    data = []
    for line in puzzle_input.splitlines():
        elem = line.split()
        vbar = elem.index("|")
        card = elem[1].rstrip(":")
        have = set(elem[2:vbar])
        want = set(elem[vbar + 1 :])
        data.append((card, len(have & want)))
    return data


def part1(data):
    return sum([1 << wins >> 1 for _, wins in data])


def part2(data):
    score = [1] * len(data)
    for c, (_, wins) in enumerate(data):
        i, j = c + 1, c + 1 + wins
        score[i:j] = [x + score[c] for x in score[i:j]]
    return sum(score)
with open("input4.txt", 'r') as fp:
    print(part2(parse(fp.read())))
"""class Card:
    def __init__(self, card_id: int, winning_cards, having_cards):
        self.id = card_id
        self.winning_cards = winning_cards
        self.having_cards = having_cards
    def __repr__(self):
        return f"Card {self.id}"#: {' '.join(map(str, self.winning_cards))} | {' '.join(map(str, self.having_cards))}"
        
    def get_matching_cards(self):
        count = 0
        score = 0
        for w in self.winning_cards:
            if w in self.having_cards:
                if count == 0:
                    score = 1
                else:
                    score *= 2
                count += 1
        return score
    
    def get_matching(self):
        count = 0
        for w in self.winning_cards:
            if w in self.having_cards:
                count += 1
        return count
            
def parse_input(data):
    cards = []
    for line in data:
        card_id = int(line.split(": ")[0].strip("Card "))
        winning, having = line.split(": ")[1].split(" | ")
        winning, having = list(map(int, winning.split())), list(map(int, having.strip().split()))
        cards.append(Card(card_id, winning, having))
        
    return cards
    
with open("input4.txt", 'r') as fp:
    data = fp.readlines()
    
cards = dict.fromkeys(parse_input(data), 1)
#cards = parse_input(data)
print(cards)

current_card = 0
ct = 0
while True:
    if current_card >= len(cards):
        break
    c = list(cards.keys())[current_card]
    for i in range(1, c.get_matching()+1):
        cards[list(cards.keys())[current_card+i]] += 1

    print(cards, current_card, c.get_matching())

    if ct == 0:
        if cards[c] > 1:
            ct = cards[c] - 1
    else:
         ct -= 1
         if ct < 1:
             ct = 0
             current_card += 1

print(cards)
exit()
current_card = 0
while True:
    c = cards[current_card]
    if c.get_matching() > 0:
       cards.extend(cards[current_card+1:current_card+c.get_matching()])
    cards.sort(key=lambda x: x.id)
    current_card += 1
    print(cards)"""