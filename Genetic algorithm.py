import random
import operator
from generation import Solution

RANDOM_GENEPOOL = [Solution(fitness=False) for x in range(1, 10)]

population_size = 15
oorspronkelijke_generatie = []
desired_Fitness_Score = 1
current_generation = 0
max_generations = 10


def genetic_algoritm(huidige_generatie: list[Solution], max_generations, current_generation, desired_Fitness_Score):
    if huidige_generatie == []:

        for i in range(0, population_size):
            huidige_generatie.append(Solution())  # returnd randomkinderen met fitness
    else:
        if current_generation == max_generations or sorted(huidige_generatie, key=operator.attrgetter('fitness_score'), reverse=True)[
                    0].fitness_score == desired_Fitness_Score:

            print("____________________________________________________________")
            if (current_generation == max_generations):
                print("Max iteraties bereikt")
            else:
                print("Desired fitness score is behaald")

            print("Dit is het beste kind:",
                  sorted(huidige_generatie, key=operator.attrgetter('fitness_score'), reverse=True)[0].fitness_score)
            print("____________________________________________________________")
            return


    sort_huidige_generatie = sorted(huidige_generatie, key=operator.attrgetter('fitness_score'), reverse=True)
    print("____________________________________________________________")
    print("Generatie",current_generation, "is succesvol gegenereerd")
    print("Beste kind deze generatie:", sort_huidige_generatie[0].fitness_score)



    new_generation = generateNewGeneration(sort_huidige_generatie,
                                           population_size)  # selection,crossover en mutation, (+parent en randomchildren)

    genetic_algoritm(new_generation, max_generations, current_generation + 1, desired_Fitness_Score)




def select_parent(total_fitness_score, huidige_generatie):
    bias = random.uniform(0, huidige_generatie[0].fitness_score)
    random_fs = random.uniform(0, (total_fitness_score + bias))

    partial_sum = bias
    count = 0

    while partial_sum <= random_fs:
        partial_sum += huidige_generatie[count].fitness_score

        count += 1

    if (count + 1) <= (len(huidige_generatie)) and random.randint(1, 6) == 5:
        count += 1
    return huidige_generatie[count - 1]


def generateNewGeneration(huidige_generatie: list[Solution], population_size):
    new_generation = []
    total_fitness_score = 0

    for i in range(5):
        huidige_generatie.append(Solution())

    for sol in huidige_generatie:
        total_fitness_score += sol.fitness_score

    for _ in range(0, (population_size) // 2):

        parent1 = select_parent(total_fitness_score, huidige_generatie)
        parent2 = select_parent(total_fitness_score, huidige_generatie)

        i = 0
        while parent1.genetic_pool == parent2.genetic_pool and i < (population_size + 10):
            parent2 = select_parent(total_fitness_score, huidige_generatie)
            i += 1
        child_list = crossover(parent1, parent2)

        print("Uit parent", parent1.fitness_score, parent2.fitness_score, "Komt:")
        for child in child_list:
            print(child.fitness_score)
            new_generation.append(child)

    # bereken totale fitness
    # geneer een random nummer tussen 0 en s

    # (µ + µ)-GA

    new_generation.extend(huidige_generatie)

    sorted_new_generation = sorted(new_generation, key=operator.attrgetter('fitness_score'), reverse=True)

    return sorted_new_generation[0: population_size]  # returnt lijst van random solutions


def crossover(p1: Solution, p2: Solution):
    # voer de crossover uit

    import random

    genetic_pool1 = p1.genetic_pool.copy()
    genetic_pool2 = p2.genetic_pool.copy()

    for gene in genetic_pool1:
        gene_chance = random.randint(1, 16)
        if gene_chance < 6:  # Switch
            genetic_pool1[gene], genetic_pool2[gene] = genetic_pool2[gene], genetic_pool1[gene]
        elif gene_chance == 8 or gene_chance == 9:
            genetic_pool1[gene] = RANDOM_GENEPOOL[random.randint(0, len(RANDOM_GENEPOOL) - 1)].genetic_pool[gene]
        elif gene_chance == 10 or gene_chance == 11:
            genetic_pool2[gene] = RANDOM_GENEPOOL[random.randint(0, len(RANDOM_GENEPOOL) - 1)].genetic_pool[gene]

    list_new_children = [Solution(genetic_pool1), Solution(genetic_pool2)]
    # ("dit zijn de kindjes:", list_new_children[0].fitness_score, list_new_children[1].fitness_score)

    return list_new_children


genetic_algoritm(oorspronkelijke_generatie, max_generations, current_generation, desired_Fitness_Score)
