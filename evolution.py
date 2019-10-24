blob = 0
day = 1
period = 600

birth_chance = 1
death_chance = 0.01

population = []

for i in range(period):
    blob = blob + birth_chance
    blob = blob - blob*death_chance
    population.append(blob)
    average = sum(population)/day
    print("Day " + str(day) + "\tblobs: " + str(round(blob)) + "\t" + str(average) )
    day = day + 1

import matplotlib.pyplot as plt

plt.plot(population)
plt.ylabel('population')
plt.xlabel('days')
plt.show()