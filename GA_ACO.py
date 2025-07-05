import random
import time
import numpy as np

#required parameters for building timetable
population_size = 100 
periods = int(input("ENTER TOTAL REQUIRED PERIODS: "))
days = 5 # no of working days per week
t_subjects = 6 # total no of subjects 
t_prof = 3 # available profs for teaching the subjects

iterations = 100
evaporation_rate = 0.1
pheromone_constant = 1.0

# Mapping between the subject and prof
subjects = "ABCDEF"
profs = "XYZ"
map = "YXXZYX"

#Time constraints
sub_time  = [7, 3, 6, 4, 5, 5] #time required for subject respectively
prof_time = [13, 12, 5] #time prof will teach respectively

# Pheromone matrix (subject x day x period)
pheromone_matrix = np.ones((len(subjects), days, periods)) * 0.1

#Generatin random numbers for mutation, crossover
def random_number(str, end):
    return random.randint(str, end)

#creating a chromosome
def chromosome():
    return random.choice(subjects)

#creating thread of chromosomes i.e; timetable
def timetable():
    timetable = [] #empty list on which our timetable is gonna be stored in day wise
    for i in range(days):
        schedule =  "" # empty string in which the particular day's schedule will be stored
        for j in range(periods):
            schedule += chromosome()
        timetable.append(schedule)
    return timetable

#creating time table
class Ant:
    def __init__(self):
        self.path = []
        self.fitness = float('inf')

    def solution(self): #the previously created timetable using genetic algorithm is converted into an ant 
        self.path = timetable() 

# Optimizing the solution using ACO
class ACO: 
    def __init__(self):
        # Initialize ant colony
        self.ants = []
        for i in range(population_size):
            ant = Ant()  
            self.ants.append(ant)  
        
        # Track best solution found so far
        self.best_solution = None
        self.best_fitness = float('inf')

    def fitness(self, solution):
        # Return infinity for invalid solutions
        if not solution:
            return float('inf')
        
        violations = 0
        
        # Count how many times each subject appears
        subject_counts = {}
        for day_schedule in solution:
            for subject in day_schedule:
                subject_counts[subject] = subject_counts.get(subject, 0) + 1
        
        # Check if subjects meet their required time
        for i, subject in enumerate(subjects):
            required = sub_time[i]
            actual = subject_counts.get(subject, 0)
            if actual < required:
                violations += (required - actual) * 10  # Big penalty for missing time
            elif actual > required:
                violations += (actual - required) * 5   # Smaller penalty for extra time
        
        # Count professor workload
        prof_counts = {}
        for day_schedule in solution:
            for subject in day_schedule:
                subject_idx = subjects.index(subject)
                prof = map[subject_idx]
                prof_counts[prof] = prof_counts.get(prof, 0) + 1

        # Check professor time limits
        for i, prof in enumerate(profs):
            max_hours = prof_time[i]
            actual_hours = prof_counts.get(prof, 0)
            if actual_hours > max_hours:
                violations += (actual_hours - max_hours) * 15  # Heavy penalty for overwork
        
        # Penalize consecutive same subjects (boring!)
        consecutive_penalty = 0
        for day_schedule in solution:
            for i in range(len(day_schedule) - 1):
                if day_schedule[i] == day_schedule[i + 1]:
                    consecutive_penalty += 2
        violations += consecutive_penalty
        
        # Check subject distribution across days
        subject_days = {}
        for day_idx, day_schedule in enumerate(solution):
            for subject in day_schedule:
                if subject not in subject_days:
                    subject_days[subject] = set()
                subject_days[subject].add(day_idx)
        
        # Penalize subjects taught only on one day
        for subject, days in subject_days.items():
            if len(days) == 1:  
                violations += 3
        
        # Check for incomplete schedules
        for day_schedule in solution:
            if len(day_schedule) != periods:
                violations += 20  # Big penalty for incomplete days
        
        return violations 

    def update_pheromone(self, ant):
        # Skip if ant has invalid solution
        if ant.fitness == float('inf'):
            return
        
        # Calculate pheromone to deposit (better solutions = more pheromone)
        pheromone_amount = pheromone_constant / (1 + ant.fitness)
        
        # Update pheromone matrix based on this ant's path
        for day_idx, day_schedule in enumerate(ant.path):
            for period_idx, subject in enumerate(day_schedule):
                subject_idx = subjects.index(subject)
                pheromone_matrix[subject_idx, day_idx, period_idx] += pheromone_amount

    def evaporate_pheromone(self):
        # Evaporate pheromone to prevent stagnation
        global pheromone_matrix
        pheromone_matrix *= (1 - evaporation_rate)

    def aco(self):
        print("Starting ACO optimization...")
        print(f"Running {iterations} iterations with {population_size} ants...")
        
        # Main ACO loop
        for iteration in range(iterations):
            # Generate solutions for all ants
            for ant in self.ants:
                ant.solution()
                ant.fitness = self.fitness(ant.path)
                
                # Update best solution if we found a better one
                if ant.fitness < self.best_fitness:
                    self.best_solution = ant.path.copy()
                    self.best_fitness = ant.fitness
                    print(f"Iteration {iteration + 1}: New best fitness = {self.best_fitness}")
            
            # Evaporate old pheromone
            self.evaporate_pheromone()
            
            # Deposit new pheromone based on ant solutions
            for ant in self.ants:
                self.update_pheromone(ant)
            
            # Show progress every 20 iterations
            if (iteration + 1) % 20 == 0:
                print(f"Completed {iteration + 1}/{iterations} iterations. Best fitness: {self.best_fitness}")
        
        self.display()

    def display(self):
        print("\n" + "="*50)
        print("FINAL BEST SOLUTION:")
        print("="*50)
        if self.best_solution:
            for i, schedule in enumerate(self.best_solution):
                print(f"DAY {i + 1}: {schedule}")
            print(f"\nBest Fitness Score: {self.best_fitness}")
        else:
            print("No valid solution found!")

#main function
if __name__ == "__main__":
    random.seed(time.time())
    a = ACO()
    a.aco()