# Lab1

## Objetivos de aprendizagem

Com este guião:

1. exercitaremos o desenvolvimento de funções simples
1. exercitaremos o desenvolvimento de funções aninhadas (funções que chamam outras funções)


## Enunciado

A unidade padrão de medida da temperatura é kelvin (K), mas não é algo que usemos no dia-a-dia. Normalmente trabalhamos com graus Celsius (C) e alguns preferem referir-se à temperatura em graus Fahrenheit (F).

Quando falamos em zero absoluto, estamos a referir-nos a 0 K. Se nos perguntarem a que temperaturas a água congela e ferve, se calhar respondemos 0⁰ e 100⁰. Felizmente que um grau Celsius corresponde a um intervalo de 1 K. Sabendo que 0⁰C corresponde a 273.15 K, já podemos converter de Celsius para Kelvin e vice-versa.

Para a conversão de e para Fahrenheit, precisamos saber que 0⁰C corresponde a 32⁰F e que um intervalo de um grau Celsius corresponde a um intervalo de 1.8 graus Fahrenheit.

Queremos pois um conjunto de programas que convertam as temperaturas de e para as várias unidades ou escalas. 

Submeta cada uma das tarefas no problema correspondente do concurso IPC_L1.

Cada tarefa aceite e validada vale 1 ponto.

### Tarefa A

Prepare um programa que contenha uma função *k2c* que converta uma temperatura em kelvin para graus Celsius.

#### Caso de teste

**Input**

```
273.15
```


**Output**

```
0.0
```

### Tarefa B

Acrescente ao seu programa uma função *c2k* que converta uma temperatura em graus Celsius para kelvin.

Altere as linhas finais para que a nova função seja agora chamada.
De futuro, faça sempre a alteração correspondente no conjunto principal de instruções.

#### Caso de teste

**Input**

```
37
```


**Output**

```
310.15
```


### Tarefa C

Acrescente ao seu programa uma função *c2f* que converta uma temperatura em graus Celsius para graus Fahrenheit.

#### Caso de teste

**Input**

```
37
```

**Output**

```
98.60000000000001
```

### Tarefa D

Acrescente ao seu programa uma função *f2c* que converta uma temperatura em graus Fahrenheit para graus Celsius.

#### Caso de teste

**Input**

```
98.6
```

**Output**

```
36.99999999999999
```

### Tarefa E

Acrescente agora uma função *k2f* que converta uma temperatura em kelvin para graus Fahrenheit. A função *k2f* deve usar as funções *k2c* e *c2f*. 

#### Caso de teste

**Input**

```
273.15
```

**Output**

```
32.0
```

### Tarefa F

Acrescente ao seu programa uma função *f2k* que converta uma temperatura em graus Fahrenheit para kelvin. A função *f2k* deve usar as funções *f2c* e *c2k*. 

#### Caso de teste

**Input**

```
98.6
```

**Output**

```
310.15
```

