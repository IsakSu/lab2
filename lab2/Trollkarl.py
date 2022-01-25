from linkedQFile import *
counter = 0

input = input("Please type a cardnumber followed by a blank space followed by a cardnumber and so on: ")
cards = Queue()
for i in range(len(input.split())):
    cards.enqueue(input.split()[i])

while(not cards.isEmpty()):
    if(counter%2 == 0):
        cards.enqueue(cards.dequeue())
    else:
        print(cards.dequeue())
    counter = counter + 1
