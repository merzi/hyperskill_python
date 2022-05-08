face_cards = {'Jack': 11,
              'Queen': 12,
              'King': 13,
              'Ace': 14}
cards = []

for _ in range(6):
    card = input()
    if card in face_cards:
        value = face_cards.get(card)
    else:
        value = int(card)

    cards.append(value)

print(sum(cards) / len(cards))
