# Lab4

## Objetivos de aprendizagem

Com este guião, exercitaremos:

1. a validação de dados de entrada
1. o uso de condições no controlo de fluxo do programa (com *if* e *while*) 
1. o desenvolvimento de programas

## Enunciado

### Tarefa A

Na aula vimos o desenvolvimento de funções para o cálculo do fatorial de um número. 

Pretendemos agora incluir uma dessas funções num programa, incluindo na função de teste a verificação de que a entrada é válida.

Note que o fatorial de um número está definido para números inteiros positivos ($N_0^+$). Ou seja, não se aceitam valores negativos ou strings. 

Assim, se o cálculo não puder ser efetuado, o seu programa deverá produzir a mensagem (sem as aspas):
    "A função fatorial está definida para números inteiros maiores ou iguais a zero."
a um pedido de cálculo ilegal.

Prepare então um programa calcule o fatorial de um número e valide os dados de entrada.

**Dicas**:

Veja a ajuda sobre a função *str.isnumeric*

Para os diferentes casos de input, experimente na consola do Spyder:
```
temp = input()
temp.isnumeric()
```

#### Casos de teste 

**Input 1**

```
5
```

**Output 1**

```
120
```

**Input 2**

```
5.0
```

**Output 2**

```
A função fatorial está definida para números inteiros maiores ou iguais a zero.
```

**Input 3**

```
-5
```

**Output 3**

```
A função fatorial está definida para números inteiros maiores ou iguais a zero.
```

**Input 4**

```
asd
```

**Output 4**

```
A função fatorial está definida para números inteiros maiores ou iguais a zero.
```


Submeta no problema A do Lab2.

### Tarefa B

Pretende-se determinar os números pares de um intervalo. Para o efeito, considere o esboço apresentado em *proto_B.py*

```
# -*- coding: utf-8 -*-

"""
Determinar os números pares de um intervalo
(c) Margarida Madeira e Moura, 2021
"""

def par(n):
    """Função que determina se um número é par.
    
    par(n) devolve True se n for par; caso contrário, devolve False"""
    ## Apague esta linha e acrescente aqui o seu código

def escreve(n):
    """Função que imprime um valor"""
    print(n)
    
def test_par():
    """Função de teste da função par
    Apresenta o valor sse o número for par"""
    x = int(input())
    if (par(x)):
        escreve(x)

def pares_intervalo(x, y):
    """Função que apresenta os números pares de um intervalo"""
    
    ## Apague esta linha e acrescente aqui o seu código


def test_intervalo_inteiros():
    """Função que lê os valores extremos de um intervalo de números inteiros"""
    x = int(input())
    y = int(input())
    valido = False
    # acrescente a validação
    # # x tem que ser inferior a y
    if (valido):
        pares_intervalo(x,y)
    else:
        print('Valores inválidos.')


test_par()
# test_intervalo_inteiros()

```


Comece por completar a função *par*. 

Depois, comente a chamada à função *test_par* e descomente a linha seguinte que contém a chamada à função *test_intervalo_inteiros*. 

Depois, conclua a validação na função *test_intervalo_inteiros* e, finalmente, complete a função *pares_intervalo*.

#### Casos de teste

**Input 1**

```
1
5
```

**Output 1**

```
2
4
```

**Input 2**

```
10
1
```

**Output 2**

```
Valores inválidos.
```

**Input 3**

```
-5
-1
```

**Output 3**

```
-4
-2
```

**Input 4**

```
1
10
```

**Output 4**

```
2
4
6
8
10
```

Submeta no problema B do Lab2.

### Tarefa C

Pretende-se determinar os números de um intervalo de inteiros que são múltiplos de três e múltiplos de cinco.

#### Casos de teste

**Input 1**

```
1
20
```

**Output 1**

```
15
```

**Input 2**

```
10
1
```

**Output 2**

```
Valores inválidos.
```

Submeta no problema C do Lab2.

### Tarefa D

Pretende-se determinar um termo da [sequência de Fibonacci](https://www.wolframalpha.com/input/?i=fibonacci+sequence).

Prepare um programa que leia um inteiro $n$ e apresente o $n$-ésimo termo da sequência $F(n)$, considerando que

$ F(n) = F(n-1) + F(n-2)$ para $n \in N_0^+ $

sendo 

$F(0) = 0$ e $ F(1) = 1$.

Se o termo pedido não for válido, o programa apresenta a mensagem "Valor inválido." (sem as aspas).

Inclua a validação do inteiro lido na função de teste.

#### Casos de teste

**Input 1**

```
-5
```

**Output 1**

```
Valor inválido.
```

**Input 2**

```
0
```

**Output 2**

```
0
```

**Input 3**

```
1
```

**Output 3**

```
1
```

**Input 4**

```
7
```

**Output 4**

```
13
```


Submeta no problema D do Lab2.
