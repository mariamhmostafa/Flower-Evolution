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

def initialize_population(size=8):
    return [Flower() for _ in range(size)]

def select(population):
    weights = []
    for flower in population:
        weights.append(flower.fitness)
    parents = random.choices(population, weights=weights, k=4)
    return parents

def duplicate(parents):
    duplicated_parents = parents * 2
    # random.shuffle(duplicated_parents)
    return duplicated_parents

def crossover(parents):
    children = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        child1 = Flower()
        child2 = Flower()
        crossover_point = random.randint(0, len(parent1.dna) - 1)
        child1.dna = parent1.dna[:crossover_point] + parent2.dna[crossover_point:]
        child2.dna = parent2.dna[:crossover_point] + parent1.dna[crossover_point:]
        children.append(child1)
        children.append(child2)
    return children

def mutate(children):
    for child in children:
        for i in range(len(child.dna)):
            if random.random() < mutation_rate:
                if i == 0:
                    child.dna[i] = random.randint(0, 10)
                elif i == 7:
                    child.dna[i] = random.randint(0, 7)
                else:
                    child.dna[i] = random.randint(0, 255)
    return children

def next_generation():
    global generation
    global population
    
    parents = select(population)

    duplicated_parents = duplicate(parents)
    print("parents:")
    for flower in duplicated_parents:
        print(flower.dna)

    children = crossover(duplicated_parents)
    print("children:" )
    for flower in children:
        print(flower.dna)

    new_population = mutate(children)
    print("new population:")
    for flower in new_population:
        print(flower.dna)

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
        print(flower.dna)
    print ("next generation")
    next_generation()
    print("Final flowers: ")
    for flower in population:
        print(flower.dna)
