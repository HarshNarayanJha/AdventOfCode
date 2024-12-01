class Card:
    def __init__(self, card_id: int, winning_cards, having_cards):
        self.id = card_id
        self.winning_cards = winning_cards
        self.having_cards = having_cards
        
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
    
cards = parse_input(data)
print(cards[0].winning_cards)
scores = [card.get_matching_cards() for card in cards]
print(sum(scores))
