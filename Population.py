import random
import string

from Individual import Individual


class Population:
    def __init__(self, population_size: int, target: str):
        self.population_size = population_size
        self.target = target
        self.individuals = []

    def initialize_population(self):
        for i in range(self.population_size):  # Loop through the number of individuals and initialize them at random
            genetics = self.random_genetic_material_creator()  # Create random genetic material for a single individual
            self.individuals.append(Individual(genetics, self.target))  # Create the individual and add it to the population

    def random_genetic_material_creator(self) -> str:
        genetic_choices = random.choices(string.ascii_lowercase + " ", k=len(self.target))  # Select 44 characters from a list of lower case characters and include the space
        genetics = "".join(genetic_choices)  # Join that list together into a single string
        return genetics

    def print_population(self):
        for individual in self.individuals:  # Loop through each individual
            print(individual)  # Pprint the individual
