import time

import numpy as np
from numba import jit

print('CPU: AMD Ryzen 7 5700G')
print('CPU Clock: Up to 4.6GHz')
print('L2 Cache: 4MiB')
print('L3 Cache: 16MiB')
print('RAM: 16GB')
print('SO: Fedora Linux')

print('------------------------')

print('Experimento 01 - Multiplicação de Matrizes')

threads = [2, 4, 8]

a = np.random.rand(500, 500)
b = np.random.rand(500, 500)

# Começo
if len(a[0]) != len(b):
    # verifica se o número de colunas de a é igual ao número de linhas de b
    raise ValueError('Error')

# cria uma matriz de zeros com o número de linhas de a e o número de colunas de b
c = np.zeros((len(a), len(b[0])))


def basic(a, b, c):
    for i in range(len(a)):  # percorre as linhas da matriz a
        for j in range(len(b[0])):  # percorre as colunas da matriz b
            for k in range(len(b)):  # percorre as linhas da matriz b
                # soma o resultado da multiplicação de cada elemento de a com b
                c[i][j] += a[i][k] * b[k][j]
    return i, j, k


@jit(nopython=True)
def numb(a, b, c):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return i, j, k


start = time.time()
basic(a, b, c)
end = time.time()
tempo_sequencial = end - start
print('Tempo de execução sequencial: ', tempo_sequencial)

for i in threads:
    start = time.time()
    numb(a, b, c)
    end = time.time()
    print('Tempo de execução numba com {} threads: '.format(i), end - start)
    print('SpeedUp: ', tempo_sequencial / (end - start))

print('------------------------')

print('Experimento 02 - Produto Escalar')

u = np.random.rand(100)
v = np.random.rand(100)


def prod_escalar(u, v):
    return u * v


@jit(nopython=True)
def prod_escalar_paralelo(u, v):
    return u * v


start = time.time()
prod_escalar(u, v)
end = time.time()
tempo_sequencial = end - start
print('Tempo de execução sequencial: ', tempo_sequencial)

for i in threads:
    start = time.time()
    prod_escalar_paralelo(u, v)
    end = time.time()
    print('Tempo de execução numba com {} threads: '.format(i), end - start)
    print('SpeedUp: ', tempo_sequencial / (end - start))

print('------------------------')

print('Experimento 03 - Análise do Projeto Integrador')

""" A única parte do projeto integrador que poderia ser otimizado com Numba
e o paradigma de computação paralela, seria quando formos realizar o treinamento
de nosso modelo de classificação. Entretanto, o desenvolvimento do projeto
ainda está em andamento, não sendo possível realizar a análise de tempo de
execução, já que o modelo ainda não está pronto.

Outras partes do projeto não sofreriam ganhos significativos com a utilização,
como a leitura dos dados, junto a biblioteca Pandas, já que o Numba não o reconhce,
e também a parte de banco de dados, que pode gerar problemas ao tentar popular."""

""" Por exemplo, o módulo DataParallel do PyTorch permite o uso de paralelismo de dados
e permite o treinamento simultâneo de um modelo em muitas GPUs. Por meio de bibliotecas
como o PyTorch Lightning, que oferecem uma interface direta para treinamento distribuído
em várias GPUs ou estações de trabalho, o paralelismo de tarefas pode ser usado.

O PyTorch permite a compilação JIT (Just-In-Time) para otimização de código nativo com a 
biblioteca TorchScript. Ao fazer isso, o código Python pode ser transformado em uma versão
otimizada para execução para uso em tempo de execução."""
