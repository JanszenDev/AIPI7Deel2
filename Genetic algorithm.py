import random
import operator

population_size = 30 
huidige_generatie = []
desired_Fitness_Score = 1
generations = 100

def genetic_algoritm(huidige_generatie, max_generations, current_generation, desired_Fitness_Score):

    if current_generation == max_generations or sort_huidige_generatie[0].fitness_score == desired_Fitness_Score :
        return sort_huidige_generatie[0] #returnt solutie met hoogste fitnessscore
    if huidige_generatie == []:

        for i in range(0, population_size):
            huidige_generatie.Add(GenerateRandomSolution()) #returnd randomkinderen met fitness


    sort_huidige_generatie = sorted(huidige_generatie, key=operator.attrgetter('fitness_score'))

    nieuwe_generatie = generateNewGeneration(sort_huidige_generatie) #selection,crossover en mutation, (+parent en randomchildren)

    genetic_algoritm(nieuwe_generatie, max_generations, current_generation, desired_Fitness_Score)




    #top 9 gemixt totdat er 15 children uitkomen Top 30 --> nieuwe 50%

    #top 10% slechtse kinderen gebruiken we niet


    #Deze worden random gemixt met andere solutions in de lijst
    #







def GenerateRandomSolution():
    #retourneert random solution voor initializatie eerste generatie en eventueel

    return solution

def select_parent(total_fitness_score, huidige_generatie):
    random_fs = random.uniform(0, total_fitness_score)

    partial_sum = 0
    count = 0


    while partial_sum <= random_fs:

        partial_sum += huidige_generatie[count].fitness_score


        count += 1
    return huidige_generatie[count-1]


def generateNewGeneration(solution, population_size):

    nieuwe_generatie = []
    total_fitness_score = 0
    for sol in huidige_generatie:
        total_fitness_score += sol.fitness_score

    for i in range(0,len(population_size)):

        parent1 = select_parent(total_fitness_score, huidige_generatie)
        parent2 = select_parent(total_fitness_score, huidige_generatie)

        nieuwe_generatie.Add(crossover(parent1, parent2))

    for i in range(5):
        nieuwe_generatie.Add(GenerateRandomSolution())

    #bereken totale fitness
    #geneer een random nummer tussen 0 en s


    #(µ + µ)-GA

    nieuwe_generatie.Add(huidige_generatie)
    sorted_nieuwe_generatie = sorted(huidige_generatie, key=operator.attrgetter('fitness_score'))



    return sorted_nieuwe_generatie[0: population_size] #returnt lijst van random solutions


def calculateFitness(solution.gpv):


    return fitness



def crossover(p1,p2):
    #voer de crossover uit



    if randomkans == True:
        solution = mutation(solution)

    return solution


def mutation(solution):

    return mutatedSolution

def getRandomInt(min_waarde, max_waarde):
    return random.randint(min_waarde,max_waarde)

def getRandomFloat(min_waarde, max_waarde):
    return random.uniform(min_waarde,max_waarde)