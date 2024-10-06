import tkinter as tk
import random
import math

mutation_rate = 0.05

class Flower:
    def __init__(self, canvas, dna=None, fitness=0.01, pos=(0, 0)):
        self.fitness = fitness
        self.canvas = canvas
        self.dna = dna if dna else [
            random.randint(6, 15),    # center_size
            random.randint(0, 255),   # center_red
            random.randint(0, 255),   # center_green
            random.randint(0, 255),   # center_blue
            random.randint(0, 255),   # petal_red
            random.randint(0, 255),   # petal_green
            random.randint(0, 255),   # petal_blue
            random.randint(8,12)      # num_petals
        ]
        self.pos = pos
        self.petal_ids = []
        self.center_id = None
        self.draw_flower()

    def draw_flower(self):
        self.center_size = self.dna[0]
        self.center_color = f'#{self.dna[1]:02x}{self.dna[2]:02x}{self.dna[3]:02x}'
        self.petal_color = f'#{self.dna[4]:02x}{self.dna[5]:02x}{self.dna[6]:02x}'
        if self.dna[7] != 0:
            angle = 360 / self.dna[7]
            for i in range(self.dna[7]):
                radian_angle = math.radians(i * angle)
                petal_x = self.pos[0] + math.cos(radian_angle) * (self.center_size + self.center_size + 5)
                petal_y = self.pos[1] + math.sin(radian_angle) * (self.center_size + self.center_size + 5)
                petal_id = self.canvas.create_oval(
                    petal_x - self.center_size / 1 , petal_y - self.center_size / 1,
                    petal_x + self.center_size / 1 , petal_y + self.center_size / 1,
                    fill=self.petal_color, outline=""
                )
                self.petal_ids.append(petal_id)

        self.center_id = self.canvas.create_oval(
            self.pos[0] - self.center_size * 2, self.pos[1] - self.center_size * 2,
            self.pos[0] + self.center_size * 2, self.pos[1] + self.center_size * 2,
            fill=self.center_color, outline=""
        )

    def is_hovered(self, mouse_pos):
        dist = math.sqrt((self.pos[0] - mouse_pos[0]) ** 2 + (self.pos[1] - mouse_pos[1]) ** 2)
        return dist <= self.center_size

    def increase_fitness(self):
        self.fitness += 0.005  

    def clear_flower(self):
        self.canvas.delete(self.center_id)
        for petal_id in self.petal_ids:
            self.canvas.delete(petal_id)
        self.petal_ids.clear()

def initialize_population(canvas, size=8):
    population = []
    spacing = 100 
    y_position = 250
    for i in range(size):
        x_position = 50 + i * spacing
        flower = Flower(canvas, pos=(x_position, y_position))
        population.append(flower)
    return population

def select(population):
    weights = [flower.fitness for flower in population]
    parents = random.choices(population, weights=weights, k=4)
    return parents

def crossover(parents, canvas, size=8):
    children = []
    spacing = 100 
    y_position = 250

    for i in range(size):
        parent1 = parents[i % len(parents)]
        parent2 = parents[(i + 1) % len(parents)]
        child_dna = parent1.dna[:4] + parent2.dna[4:]
        x_position = 50 + i * spacing
        child = Flower(canvas, dna=child_dna, pos=(x_position, y_position))
        children.append(child)

    return children

def mutate(children):
    for child in children:
        for i in range(len(child.dna)):
            if random.random() < mutation_rate:
                if i == 0:
                    child.dna[i] = random.randint(3, 10)
                elif i == 7:
                    child.dna[i] = random.randint(5, 8)
                else:
                    child.dna[i] = random.randint(0, 255)
    return children

def next_generation(canvas, population):
    parents = select(population)
    children = crossover(parents, canvas)
    new_population = mutate(children)

    for flower in population:
        flower.clear_flower()

    for flower in new_population:
        flower.draw_flower()

    return new_population

def main():
    root = tk.Tk()
    root.title("Flower Evolution")

    canvas = tk.Canvas(root, width=800, height=500, bg="white")
    canvas.pack()

    population = initialize_population(canvas)

    def on_mouse_move(event):
        for flower in population:
            if flower.is_hovered((event.x, event.y)):
                flower.increase_fitness()

    def generate_next_generation():
        nonlocal population
        population = next_generation(canvas, population)

    canvas.bind("<Motion>", on_mouse_move)
    next_gen_button = tk.Button(root, text="Next Generation", command=generate_next_generation)
    next_gen_button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
