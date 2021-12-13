import random

# Create a black box object that generates random numbers
rng = random.Random()

dice_throw = rng.randrange(1,7) # Return an int, one of 1,2,3,4,5,6
delay_in_seconds = rng.random() * 5.0

random_odd = rng.randrange(1, 100, 2)

cards = list(range(52)) # Generate ints [0 .. 51]
# representing a pack of cards.
rng.shuffle(cards) # Shuffle the pack

print(cards)

##### Rather Functional
import random

cards = list(range(52)) # Generate ints [0 .. 51]
new_cards = cards[:]
rng.shuffle(new_cards) # Shuffle the pack

print(cards)
print(new_cards)

drng = random.Random(123) # Create generator with known starting state
