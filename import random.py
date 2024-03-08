import random

def generar_poblacion(size, length):
    return [''.join(random.choice('01') for _ in range(length)) for _ in range(size)]

def evaluar_fitness(individuo, objetivo):
    return sum(1 for a, b in zip(individuo, objetivo) if a == b)

def seleccionar_padres(poblacion, objetivo, n_padres):
    padres = sorted(poblacion, key=lambda x: evaluar_fitness(x, objetivo), reverse=True)
    return padres[:n_padres]

def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

def mutar(individuo, prob_mutacion):
    return ''.join(bit if random.random() > prob_mutacion else random.choice('01') for bit in individuo)

def algoritmo_genetico(objetivo, tamano_poblacion, prob_mutacion, generaciones):
    poblacion = generar_poblacion(tamano_poblacion, len(objetivo))
    
    for _ in range(generaciones):
        padres = seleccionar_padres(poblacion, objetivo, 2)
        hijos = cruzar(padres[0], padres[1])
        poblacion = [mutar(hijo, prob_mutacion) for hijo in hijos]

    mejor_individuo = max(poblacion, key=lambda x: evaluar_fitness(x, objetivo))
    return mejor_individuo

# Parámetros
objetivo = "11011010101010111010101010101110"
tamano_poblacion = 100
prob_mutacion = 0.01
generaciones = 1000

# Ejecutar algoritmo genético
resultado = algoritmo_genetico(objetivo, tamano_poblacion, prob_mutacion, generaciones)

# Mostrar resultado
print("Resultado final:", resultado)
