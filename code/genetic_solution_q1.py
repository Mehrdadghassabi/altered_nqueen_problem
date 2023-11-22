import DataGen as dg
import fitness as fi
import random


def generate_an_individual_phenotype(board):
    raw_soldiers_position = dg.raw_soldiers_pos(board.soldiers_info)
    queens_info = dg.Queens(BoardSize=board.boardSize, soldiers_position=raw_soldiers_position)
    queens_position = dg.unpack_queens_info(queens_info, board.boardSize)

    return queens_position


def generate_population(board, population_size):
    popu = []
    for _ in range(population_size):
        queens_position = generate_an_individual_phenotype(board)
        chromosome = phenotype_genotype_mapping(queens_position)
        popu.append(chromosome)
    return popu


def phenotype_genotype_mapping(phenotype):
    queens_position = phenotype
    chromosome = []
    for queen in queens_position:
        chromosome.append(int(queen[0]))
        chromosome.append(int(queen[1]))
    return chromosome


def genotype_phenotype_remapping(chromosome):
    phen = []
    for i in range(int(len(chromosome) / 2)):
        phen.append((chromosome[2 * i], chromosome[2 * i + 1]))
    return phen


def fitness(board, queens_position):
    return fi.fitness(board, queens_position)


def fit_population(population, board, n):
    # it selects nth fittest
    population_dic = []
    for individual in population:
        # print(individual)
        queens_position = genotype_phenotype_remapping(individual)
        fn = fitness(board, queens_position)
        population_dic.append((queens_position, fn))
    sorted_population_pheno = sorted(
        population_dic,
        key=lambda x: -x[1]
    )
    nfit_population = []
    for i in range(n):
        # print(sorted_population[i][1])
        nfit_population.append(phenotype_genotype_mapping(sorted_population_pheno[i][0]))
    return nfit_population


def merge_two_list(li1, li2):
    for el in li2:
        li1.append(el)
    return li1


def pair_random(parent_pool):
    parent_pairs = []
    while len(parent_pool) != 0:
        idx0 = random.randrange(0, len(parent_pool))
        parent_0 = parent_pool[idx0]
        parent_pool.remove(parent_0)
        idx1 = random.randrange(0, len(parent_pool))
        parent_1 = parent_pool[idx1]
        parent_pool.remove(parent_1)
        parent_pairs.append((parent_0, parent_1))
        # print("-----------------------------------")
    return parent_pairs


def recombination(parents_pair, Pc):
    off_springs = []
    for parents in parents_pair:
        if random.uniform(0, 1) < Pc:
            cross_over_point1 = len(parents[0]) / 2
            off_spring0 = []
            off_spring1 = []
            for i in range(len(parents[0])):
                if i < cross_over_point1:
                    off_spring0.append(parents[0][i])
                    off_spring1.append(parents[1][i])
                else:
                    off_spring0.append(parents[1][i])
                    off_spring1.append(parents[0][i])
            off_springs.append(off_spring0)
            off_springs.append(off_spring1)
        else:
            off_springs.append(parents[0])
            off_springs.append(parents[1])
    return off_springs


def mutation(offsprings, board, Pm):
    for offspring in offsprings:
        for i in range(len(offspring)):
            if random.uniform(0, 1) < Pm:
                offspring[i] = int(random.uniform(-board.boardSize / 2 - 1, board.boardSize / 2))
    return offsprings


def EA1(board,laambda,mio,Pc,Pm):
    popu = generate_population(board, laambda)
    fit_popu = fit_population(popu, board, laambda)
    generation = 1
    found = False
    while generation <= 300 and not found:
        best_fond_individual = genotype_phenotype_remapping(fit_popu[0])
        best_fond_individual_fitness = fitness(board, best_fond_individual)
        parent_pool = random.sample(fit_popu, mio)
        parent_pairs = pair_random(parent_pool)
        offspr = recombination(parent_pairs, Pc)
        offspr = mutation(offspr, board, Pm)
        fit_popu = fit_population(merge_two_list(fit_popu, offspr), board, laambda)
        print("=======================================================================================================")
        print("generation: " + str(generation))
        print("best_fond_individual: " + str(best_fond_individual))
        print("best_fond_individual_fitness: " + str(best_fond_individual_fitness))
        print("maximum possible fitness: " + str(board.max_fitness()))
        if board.max_fitness() == best_fond_individual_fitness:
            found = True
        generation += 1
