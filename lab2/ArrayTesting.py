from array import array
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
cards.append(14)
for i in range(len(cards)):
    print(cards[i])

cards.insert(4, 4)
for i in range(len(cards)):
    print(cards[i])
cards.remove(4)
for i in range(len(cards)):
    print(cards[i])

lollipop = cards.pop(3)
for i in range(len(cards)):
    print(cards[i])

print(lollipop)
