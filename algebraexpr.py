from deap import algorithms
from deap import creator
from deap import base
from deap import tools
import random
import numpy
NUMBER_GOAL = 50

def validateExp(individual):
    for i in range(0, len(individual)):
        if i % 2== 0:
            if type(individual[i]) is str:
                return False
        else:
            if type(individual[i]) is int:
                return False
    return True

#Se evaluan los individuos
def evaluateInd(individual):
    if validateExp(individual):
        val = individual[0]
        for i in range(1, 10, 2):
            if individual[i] == '+':
                val += individual[i + 1]
            elif individual[i] == "-":
                val -= individual[i + 1]
            elif individual[i] == "*":
                val = val * individual[i + 1]
            elif individual[i] == "/":
                val = val / individual[i + 1]
        peso = val - NUMBER_GOAL
        if peso == 0:
            print("Solución Optima: ", individual, peso)
        else:
            print(individual, peso)
        return abs(peso), #individual
    else:
        return NUMBER_GOAL,

#Se generan individuos
def generateIndivual():
    individual = list()
    for i in range(0, 11):
        if i%2 == 0:
            number = random.randint(1, 9)
            individual.append(number)
        else:
            operator = random.randint(1, 4)
            if operator == 1:
                individual.append("+")
            elif operator == 2:
                individual.append("-")
            elif operator == 3:
                individual.append("*")
            elif operator == 4:
                individual.append("/")
    return individual

#print(generateIndivual())

creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', list , fitness = creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register('individual', tools.initIterate, creator.Individual, generateIndivual)
#ind1 = toolbox.individual()
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('mate', tools.cxOnePoint)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb = 0.5)
toolbox.register('select', tools.selTournament, tournsize = 4)
toolbox.register('evaluate', evaluateInd)

def main():
    pop = toolbox.population(n = 200)
    hof = tools.HallOfFame(4)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    algorithms.eaSimple(pop, toolbox, 0.02, 0.2, 100, stats = stats, halloffame = hof)
    return pop

'''data = generateIndivual(10)
print(data)
print(evaluate(data))'''
main()
