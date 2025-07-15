# 🐜 Timetable Optimization using Ant Colony Optimization (ACO)

This project implements a **Timetable Generator and Optimizer** using **Ant Colony Optimization (ACO)** in Python. It creates a weekly class schedule that allocates subjects and professors efficiently while minimizing violations related to time constraints, professor workload, and distribution of subjects.

---

## 📌 Features

- Generates an initial population of randomized timetables.
- Evaluates the fitness of each solution based on multiple constraints.
- Uses ACO to iteratively improve timetable quality.
- Incorporates pheromone evaporation and reinforcement to guide optimization.
- Penalizes unbalanced, overworked, or repetitive schedules.
- Outputs the optimal timetable found with the corresponding fitness score.

---

## 🧠 Problem Statement

Create a valid and optimized weekly timetable given:
- A fixed number of subjects and professors.
- Required teaching hours per subject.
- Maximum allowable hours per professor.
- A fixed number of periods per day and days per week.

The optimization ensures:
- Each subject is taught for the required time.
- No professor is over-assigned.
- Boring/repetitive subject sequences are avoided.
- Subjects are distributed fairly across all days.

---

## ⚙️ How It Works

1. **Initialization**  
   A set of ants (candidate solutions) are initialized with random timetables.

2. **Fitness Evaluation**  
   Each solution is scored based on violations like:
   - Subject time under/over allocation
   - Professor overload
   - Consecutive same-subject periods
   - Uneven distribution of subjects

3. **Pheromone Update**  
   Good solutions reinforce their structure using pheromone deposition.

4. **Evaporation**  
   Old pheromones are reduced to prevent local optima stagnation.

5. **Iteration**  
   The process continues for a defined number of iterations to find the best solution.

---

## 📥 Input

The program prompts for:


This is the number of periods per day. Default settings:
- `days = 5` (working days)
- `t_subjects = 6` (subjects A-F)
- `t_prof = 3` (professors X, Y, Z)
- Subject-professor map: `YXXZYX`

---

## 📦 Code Structure

- `Ant`: Represents a timetable (path) for an individual ant.
- `ACO`: Contains the full optimization loop, fitness logic, and pheromone updates.
- `pheromone_matrix`: Tracks the strength of pheromone trails for each (subject, day, period) combination.
- `fitness()`: Key function evaluating how good a timetable is based on violations.
- `aco()`: Main loop to run the optimization for a set number of iterations.

---

## 🚀 Getting Started

### Requirements

- Python 3.x
- `numpy`

### Run the Program

```bash
python timetable_aco.py
