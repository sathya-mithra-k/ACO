# Timetable Optimization using Hybrid GA + ACO (Genetic Algorithm + Ant Colony Optimization)

This project implements a **hybrid optimization system** combining **Genetic Algorithms (GA)** and **Ant Colony Optimization (ACO)** to generate optimal weekly timetables. It simulates intelligent scheduling by modeling each timetable as a candidate solution and uses swarm intelligence to iteratively improve the fitness of generated timetables.


## Features

- Generates an initial population of randomized timetables (GA-like initialization).
- Evaluates each solution using a constraint-based fitness function.
- Applies ACO principles to reinforce better schedules via pheromone trails.
- Penalizes undesirable scheduling patterns (like repetitive subjects or overworked professors).
- Outputs the most optimal timetable found after iterative learning.


## Optimization Strategy

This solution **hybridizes Genetic Algorithm and Ant Colony Optimization**:

### Genetic Algorithm Aspects
- **Chromosome Representation**: A timetable is a chromosome where each gene is a subject assigned to a period.
- **Population Initialization**: A population of random schedules is generated.
- **Random Variation**: Initial random schedules act as mutation-like operators.

### Ant Colony Optimization Aspects
- **Ants as Solutions**: Each ant represents a candidate timetable.
- **Pheromone Trails**: A 3D pheromone matrix guides the subject selection based on historical success.
- **Evaporation**: Older pheromones decay over time to avoid premature convergence.
- **Pheromone Reinforcement**: High-fitness solutions deposit more pheromone, influencing future generations.


## How It Works

1. **User Input**: Total periods per day.
2. **Initialize Population**: Randomly generate timetables (ants).
3. **Evaluate Fitness**: Measure violations (missing hours, overwork, repetition, etc.).
4. **Pheromone Update**: Improve probabilities for better choices.
5. **Evaporation**: Reduce stale influence.
6. **Repeat**: Iterate until the best solution is found.


## Input

The program asks:
ENTER TOTAL REQUIRED PERIODS:

This defines the number of periods per day.

### Default Parameters

- `days = 5` (Working Days)
- `subjects = "ABCDEF"`
- `profs = "XYZ"`
- `subject-professor map = "YXXZYX"`
- `sub_time = [7, 3, 6, 4, 5, 5]` (required hours)
- `prof_time = [13, 12, 5]` (max hours per prof)
- `population_size = 100`
- `iterations = 100`
- `evaporation_rate = 0.1`
- `pheromone_constant = 1.0`
note: These parameter can also be set as user defined

## Running the Code

### Requirements

- Python 3.x
- `numpy` library

### Run

```bash
python timetable_aco.py

