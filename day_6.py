def sim_population(population_data, n_days):
    for day in range(n_days):
        pop_growth = population_data[0]
        for age in range(8):
            population_data[age] = population_data[age + 1]
        population_data[6] += pop_growth
        population_data[8] = pop_growth
    return sum(population_data.values())


data = open('data/day_6.txt').read()
data = list(map(int, data.split(',')))
population = {k: 0 for k in range(9)}
for k in population.keys():
    population[k] = len([t for t in data if t == k])

print('part 1:', sim_population(population, 80))
print('part 1:', sim_population(population, 256 - 80))
