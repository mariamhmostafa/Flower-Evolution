# 🌸 Flower Evolution

A visual **genetic algorithm simulation** using Python and Tkinter, where a population of flowers evolves over time based on color, petal count, and size. The user can influence evolution by hovering over flowers to increase their fitness.

---

## 🎮 Demo

Each flower is made up of a unique DNA sequence controlling:
- 🌼 Center size and color
- 🌸 Petal color and number
- 🌿 Stem rendering

You can:
- Hover over flowers to increase their **fitness**
- Click **"Next Generation"** to evolve flowers using:
  - **Selection**
  - **Crossover**
  - **Mutation**

---

## 🧬 Evolution Mechanics

- **Fitness** is influenced by user interaction (hovering)
- **Selection** chooses the top 4 fittest flowers
- **Crossover** combines DNA of two parents to create new children
- **Mutation** randomly alters parts of the DNA based on a small rate
- **DNA structure**:
[center_size, center_r, center_g, center_b, petal_r, petal_g, petal_b, petal_count]

---

## 🖼️ GUI Preview

<img width="802" height="587" alt="Screenshot 2025-08-07 at 9 04 17 PM" src="https://github.com/user-attachments/assets/ddec2b70-7543-418b-9092-529ae467802d" />
<img width="802" height="587" alt="Screenshot 2025-08-07 at 9 04 24 PM" src="https://github.com/user-attachments/assets/de9920ee-4501-4619-bd6c-520c1ba1fe60" />
<img width="802" height="587" alt="Screenshot 2025-08-07 at 9 04 34 PM" src="https://github.com/user-attachments/assets/1bd63a8c-eb2b-49e8-b5e1-07a6e55921d4" />
<img width="802" height="587" alt="Screenshot 2025-08-07 at 9 04 45 PM" src="https://github.com/user-attachments/assets/937189fc-0d07-4611-900c-ff2a303ae1ae" />
<img width="802" height="587" alt="Screenshot 2025-08-07 at 9 04 50 PM" src="https://github.com/user-attachments/assets/3ab3982b-96fa-4a64-85cb-0a8471a0ca81" />


## 🛠️ Technologies Used
* Python 3
* Tkinter for GUI rendering
* Math & Random for DNA generation and simulation

## 🚀 How to Run
1. Clone the repo
<pre>
  git clone https://github.com/mariamhmostafa/Flower-Evolution.git
  cd Flower-Evolution
</pre>


2. Run the app
Make sure Python 3 is installed. Then run:

<pre>python3 Flower-Evolution.py</pre>

## 🎯 Controls
Move your mouse over flowers to increase their fitness

Click "Next Generation" to evolve the next population

## 🧪 Sample DNA Example
<pre>
[10, 255, 100, 80, 200, 90, 60, 5]
Center size = 10

Center color = RGB(255,100,80)

Petal color = RGB(200,90,60)

Petal count = 5
</pre>


