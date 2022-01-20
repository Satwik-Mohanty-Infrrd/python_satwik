import random
value= random.random()
print(value)

val= random.uniform(1,10)
print(val)

val= random.randint(1,6)
print(val)

greetings= ['Hello', 'Hi', 'Hey']
val= random.choice(greetings)
print(val+ ' , Corey!')

colors=['Red', 'Black', 'Green']
res= random.choices(colors, k=10)
print(res)

res= random.choices(colors, weights=[18,18,2], k=10)
print(res)

deck= list(range(1, 53))

random.shuffle(deck)
print(deck)

hand= random.sample(deck, k=5)
print(hand)