import random

mutation_rate = 0.05
generation = 0
population = []
class Flower:
    def __init__(self):
        self.fitness = 0.01
        self.dna = [
            random.randint(0, 10),    # center_size
            random.randint(0, 255),   # center_red
            random.randint(0, 255),   # center_green
            random.randint(0, 255),   # center_blue
            random.randint(0, 255),   # petal_red
            random.randint(0, 255),   # petal_green
            random.randint(0, 255),   # petal_blue
            random.randint(0, 7)      # num_petals
        ]
        

    def __repr__(self):
        return f"Flower(DNA={self.dna})"

def initialize_population(size=8):
    return [Flower() for _ in range(size)]

def selection(population):
    weights = []
    for flower in population:
        weights.append(flower.fitness)
    parent1 = random.choices(population, weights=weights, k=1)
    parent2 = random.choices(population, weights=weights, k=1)
    if parent1 == parent2:
        return selection(population)
    return parent1[0], parent2[0]

def crossover(parent1, parent2):
    child = Flower()
    crossover_point = random.randint(0, len(parent1.dna)-1)
    child.dna = parent1.dna[:crossover_point] + parent2.dna[crossover_point:]
    return child

def mutate(flower):
    for i in range(len(flower.dna)):
        if random.random() < mutation_rate:
            flower.dna[i] = random.randint(0, 10) if i == 0 else random.randint(0, 255)
    return flower

def next_generation():
    global generation
    global population
    new_population = []
    for _ in range(len(population)):
        parent1, parent2 = selection(population)
        print("parents:")
        print(parent1, parent2)
        child = crossover(parent1, parent2)
        print("child:" , child)
        child = mutate(child)
        print("child:" , child)
        new_population.append(child)
    population = new_population
    generation += 1
    return population

def increment_fitness(flower):
    flower.fitness += 0.02

if __name__ == "__main__":
    population = initialize_population()
    random_flower_fitness = random.randint(0, 7)
    print (random_flower_fitness)
    increment_fitness(population[random_flower_fitness])
    random_flower_fitness = random.randint(0, 7)
    print (random_flower_fitness)
    increment_fitness(population[random_flower_fitness])
    random_flower_fitness = random.randint(0, 7)
    print (random_flower_fitness)
    increment_fitness(population[random_flower_fitness])
    random_flower_fitness = random.randint(0, 7)
    print (random_flower_fitness)
    increment_fitness(population[random_flower_fitness])
    for flower in population:
        print(flower)
    print ("next generation")
    next_generation()
    for flower in population:
        print(flower)
