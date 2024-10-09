import tkinter as tk
import random
import math

mutation_rate = 0.05
generation = 0;

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
            random.randint(0,7)      # num_petals
        ]
        self.pos = pos
        self.petal_ids = []
        self.center_id = None
        self.stem_id = None

    def draw_flower(self):
        self.center_size = self.dna[0]
        self.center_color = f'#{self.dna[1]:02x}{self.dna[2]:02x}{self.dna[3]:02x}'
        self.petal_color = f'#{self.dna[4]:02x}{self.dna[5]:02x}{self.dna[6]:02x}'
        self.stem_color = f'#3aba60'
        stem_length = 100
        stem_start = self.pos[1] + self.center_size * 2
        stem_end = stem_start + stem_length
        self.stem_id = self.canvas.create_line(self.pos[0], stem_start, self.pos[0], stem_end, fill=self.stem_color, width=4)
        
        if self.dna[7] > 0:
            angle = 360 / self.dna[7]
            petal_radius = self.center_size * 1.2
            distance_from_center = self.center_size * 1.8 

            for i in range(self.dna[7]):
                radian_angle = math.radians(i * angle)
                petal_x = self.pos[0] + math.cos(radian_angle) * distance_from_center
                petal_y = self.pos[1] + math.sin(radian_angle) * distance_from_center
                petal_id = self.canvas.create_oval(
                    petal_x - petal_radius, petal_y - petal_radius,
                    petal_x + petal_radius, petal_y + petal_radius,
                    fill=self.petal_color, outline=""
                )
                self.petal_ids.append(petal_id)

        self.center_id = self.canvas.create_oval(
            self.pos[0] - self.center_size * 2, self.pos[1] - self.center_size * 2,
            self.pos[0] + self.center_size * 2, self.pos[1] + self.center_size * 2,
            fill=self.center_color, outline=""
        )
        self.fitness_label_id = self.canvas.create_text(
            self.pos[0], self.pos[1] - self.center_size * 5, 
            text=f"Fitness: {self.fitness:.2f}", font=("Arial", 10), fill="black"
        )

    def update_fitness_label(self):
        self.canvas.itemconfig(self.fitness_label_id, text=f"Fitness: {self.fitness:.2f}")

    def is_hovered(self, mouse_pos):
        dist = math.sqrt((self.pos[0] - mouse_pos[0]) ** 2 + (self.pos[1] - mouse_pos[1]) ** 2)
        return dist <= self.center_size * 2.5
    
    def increase_fitness(self):
        self.fitness += 0.005  
        self.update_fitness_label()


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
    sorted_population = sorted(population, key=lambda flower: flower.fitness, reverse=True)
    parents = sorted_population[:4]
    return parents

def duplicate(parents):
    return parents * 2

def crossover(parents, canvas):
    children = []
    spacing = 100 
    y_position = 250

    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        x_position1 = 50 + i * spacing
        x_position2 = 50 + (i+1) * spacing
        crossover_point = random.randint(0, len(parent1.dna) - 1)
        child1_dna = parent1.dna[:crossover_point] + parent2.dna[crossover_point:]
        child2_dna = parent2.dna[:crossover_point] + parent1.dna[crossover_point:]
        child1 = Flower(canvas, dna=child1_dna, pos=(x_position1, y_position))
        child2 = Flower(canvas, dna=child2_dna, pos=(x_position2, y_position))
        children.append(child1)
        children.append(child2)
    return children


def mutate(children):
    for child in children:
        for i in range(len(child.dna)):
            if random.random() < mutation_rate:
                if i == 0:
                    child.dna[i] = random.randint(6, 15)
                elif i == 7:
                    child.dna[i] = random.randint(0, 7)
                else:
                    child.dna[i] = random.randint(0, 255)
    return children

def next_generation(canvas, population):
    global generation
    canvas.delete("all")
    parents = select(population)
    duplicated_parents = duplicate(parents)
    children = crossover(duplicated_parents, canvas)
    new_population = mutate(children)
    for flower in new_population:
        flower.draw_flower()
    generation += 1
    return new_population

def main():
    root = tk.Tk()
    root.title("Flower Evolution")

    canvas = tk.Canvas(root, width=800, height=500, bg="white")
    canvas.pack()

    control_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
    control_frame.pack(fill=tk.X)

    generation_label = tk.Label(control_frame, text=f"Generation: {generation}", font=("Arial", 16, "bold"), fg="#333", bg="#f0f0f0")
    generation_label.pack(side=tk.LEFT, padx=20)


    next_gen_button = tk.Button(
        control_frame, text="Next Generation", font=("Arial", 14, "bold"),
        bg="#007f8a", fg="white", activebackground="#3ae1f0", padx=10, pady=5,
        borderwidth=2, relief="raised", command=lambda: generate_next_generation()
    )
    next_gen_button.pack(side=tk.RIGHT, padx=20)

    population = initialize_population(canvas)
    for flower in population:
        flower.draw_flower()

    def on_mouse_move(event):
        cursor_changed = False
        for flower in population:
            if flower.is_hovered((event.x, event.y)):
                flower.increase_fitness()
                canvas.config(cursor="crosshair")
                cursor_changed = True
                break
        
        if not cursor_changed:
            canvas.config(cursor="")

    def generate_next_generation():
        nonlocal population
        global generation
        population = next_generation(canvas, population)
        
        generation_label.config(text=f"Generation: {generation}")


    canvas.bind("<Motion>", on_mouse_move)

    root.mainloop()

if __name__ == "__main__":
    main()