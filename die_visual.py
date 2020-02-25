from die import Die
import pygal

die1 = Die()
die2 = Die(10)
#print(die1.roll())
results = []
for i in range(100000):
    result1 = die1.roll()
    result2 = die2.roll()
    results.append(result1+result2)
a = list(set(results))
a.sort()


print(a)

#print(results)
frenquences = []
for value in range(2,die1.num_side+die2.num_side+1):
    frenquence = int(results.count(value))
    frenquences.append(frenquence)

print(frenquences)

hist = pygal.Bar()
hist.title = "Result of D10 and D6 rolling 10000 times die1"
hist.x_labels = a

hist.x_title = "Result"
hist.y_title = "frenquence of result"
hist.add("D6 and D10",frenquences)
hist.render_to_file('D10_and_D6_visual.svg')


