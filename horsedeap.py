from deap import algorithms
from deap import creator
from deap import base
from deap import tools
import random
import numpy

def generateIndividual():
    individual = list()
    for y in range(0, 8):
        individual.append(list())
        for x in range(0,8):
            if random.randint(0, 50) == 3:
                individual[y].append(1)
            else:
                individual[y].append(0)
    return individual

def createMatrizEval():
    e = list()
    for x in range(0,8):
        e.append(list())
        for y in range(0,8):
            e[x].append(0)
    return e

def generateMatrizEvaluacion(individual):
    evalu = createMatrizEval()
    for y in range(0,8):
        for x in range(0,8):
            if individual[y][x] == 1:
                evalu[y][x] = 1
                if (y - 2) >= 0 and (y - 2) < 8 and (x - 1) >= 0 and (x - 1) < 8 and evalu[y - 2][x - 1] == 0:
                    evalu[y - 2][x - 1] = 2
                if (y - 2) >= 0 and (y - 2) < 8 and (x + 1) < 8 and (x - 1) >= 0 and evalu[y - 2][x + 1] == 0:
                    evalu[y - 2][x + 1] = 2
                if (y + 2) < 8 and (y + 2) >= 0 and (x - 1) >= 0 and (x - 1) < 8 and evalu[y + 2][x - 1] == 0:
                    evalu[y + 2][x - 1] = 2
                if (y + 2) < 8 and (y + 2) >= 0 and (x + 1) < 8 and (x - 1) >= 0 and evalu[y + 2][x + 1] == 0:
                    evalu[y + 2][x + 1] = 2
                
                if (y - 1) >= 0 and (y - 1) < 8 and (x - 2) >= 0 and (x - 2) < 8 and evalu[y - 1][x - 2] == 0:
                    evalu[y - 1][x - 2] = 2
                if (y - 1) >= 0 and (y - 1) < 8 and (x + 2) < 8 and (x - 2) >= 0 and evalu[y - 1][x + 2] == 0:
                    evalu[y - 1][x + 2] = 2
                if (y + 1) < 8 and (y + 1) >= 0 and (x - 2) >= 0 and (x - 2) < 8 and evalu[y + 1][x - 2] == 0:
                    evalu[y + 1][x - 2] = 2
                if (y + 1) < 8 and (y + 1) >= 0 and (x + 2) < 8 and (x + 2) >= 0 and evalu[y + 1][x + 2] == 0:
                    evalu[y + 1][x + 2] = 2
    return evalu

def evaluateIndividual(individual):
    e = generateMatrizEvaluacion(individual)
    cantidadAtaques = 0
    cantidadCaballos = 0
    cantidadBlancos = 0
    for y in e:
        for x in y:
            if x == 1:
                cantidadCaballos += 1
            elif x == 2:
                cantidadAtaques += 1
            else:
                cantidadBlancos += 1
    return abs((cantidadAtaques+cantidadCaballos)/64), 
    #return (cantidadCaballos/cantidadAtaques) + cantidadBlancos

'''d = generateIndividual()
for x in d:
    print(x)

print("Evaluacion: ")
ev = evalu'''

creator.create('FitnessMin', base.Fitness, weights = (1.0, ))
creator.create('Individual', list, fitness = creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register('individual', tools.initIterate, creator.Individual, generateIndividual)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('mate', tools.cxOnePoint)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb = 0.2)
toolbox.register('select', tools.selTournament, tournsize = 4)
toolbox.register('evaluate', evaluateIndividual)


def main():
    pop = toolbox.population(n = 2000)
    hof = tools.HallOfFame(4)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    algorithms.eaSimple(pop, toolbox, 0.02, 0.2, 50, stats = stats, halloffame = hof)
    print("Hall of fame: ", hof[0])
    print("Evaluacion: ", generateMatrizEvaluacion(hof[0]))

main()