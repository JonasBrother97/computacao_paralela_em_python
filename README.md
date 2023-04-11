# computacao_paralela_em_python

## Experimento 01 – Multiplicação de Matrizes

Etapa I: Implementar um programa sequencial na linguagem Pythonpara multiplicação de duas matrizes NxN. Após a implementação faça os testes necessários.

EtapaII:Após  a  implementação  faça  uma  análise do  desempenho do  algoritmo implementadoe calcule o tempopara a computação da operação considerando umamatriz de dimensão 500X500. Inicialize com dados aleatórios antes do processamento.

EtapaIII: Implementar   um   programa   paralelo em Pythonusando Numbapara multiplicação   de   duas   matrizes   NxN. Utilize   um   conjunto   de   4   threads   para   o processamento paralelo.

Etapa IV: Calcule o tempo para a computação da operação considerando uma matriz de dimensão 500X500e conjuntos de 2, 4 e 9 threads. Inicialize com dados aleatórios antes do processamento.

Etapa V: Calcule o SpeedUp da solução paralela proposta na etapa III.Indique no final do cálculo as informações de configuração do hardware utilizado (CPU, Clock, Cache, memória RAM e SO).

## Experimento 02 – Produto Escalar

Etapa  I:  Implementar  um  programa  sequencial  na  linguagem Pythonque  calcule  o produto escalar entre dois vetores(u e v)de tamanho 100. Após a implementação faça os testes necessários.

Etapa  II:  Após  a  implementação  faça  uma  análise  do  desempenho do  algoritmo implementado  e  calcule  o  tempo  para  a  computação  da  operação  considerando dois vetores de tamanho 100. Inicialize com dados aleatórios antes do processamento.

Etapa  III:  Implementar  um  programa  paralelo  em Pythonusando Numbapara calculeproduto escalar de dois vetoresde tamanho 100. Utilize um conjunto de 4 threads para o processamento paralelo. 

## Experimento 03 – Análise do Projeto Integrador

1) Identifique no   projetoa(s)parte(s)da   implementaçãoque   poderia(m)ser otimizada(s)usando  Numba  e  o  paradigma  de  computação  paralela*. As seguintes   etapas   deverão   ser cumpridas:

    i)   descrever   as partes   do   projeto desenvolvido que poderiam ser otimizadas usando computação paralela. A descrição deverá  ser  compilada  em um  documento;

    ii)  implementar  as  partes  doprojeto identificadosusando os recursos disponibilizados pelo módulo Python Numba;

    iii)realizar a análise de desempenho da proposta de otimização do código desenvolvido usando  computação  paralela  e  otimização  de   código;

    iv) complementar o documento elaboradona  etapa (i)com  os  resultados  da  análise  de  desempenho realizada na etapa anterior.

2) Analisar seo algoritmo  de aprendizado de máquina utilizado no projeto  faz uso de algum  recurso  de  computação  paralela(paralelismo  de  dados  ou  tarefa). Deve-se tentar identificar qual o nível de paralelismo (instrução ou aplicação) e quais partes do  algoritmo  foram  otimizadaspor  código  nativocomo,  por  exemplo,  a  solução  jit Numba2ou CPython3(chamada de código em C no Python).