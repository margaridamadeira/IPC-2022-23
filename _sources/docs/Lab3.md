# Lab3

Note bem:

+ Cotação deste guião: 2 pontos
+ Submeta cada uma das tarefas no problema correspondente do concurso IPC_L3.
+ Prazo limite de submissão: 23h59m de 18 de outubro
+ Prazo limite de validação das submissões aceites: 25 de outubro, horário de atendimento de terça-feira (9h30 às 10h30).

## Objetivos de aprendizagem

Com este guião, exercitaremos:

1. a utilização de strings
1. o uso de condições no controlo de fluxo do programa 
1. a utilização de funções do Python
1. desenvolvimento de programas

e continuaremos a usar o Mooshak para verificar o resultado das soluções desenvolvidas.

## Modelo geral de um programa

Em Python, como em muitas linguagens, um programa é essencialmente uma coleção de funções. Entre elas há uma função especial, a função main. Esta função main é especial porque é pela função main que o programa começa as operações, quando o mandamos correr. Inversamente, quando a função main esgota as suas instruções, o programa termina.

Considere o exemplo apresentado abaixo de um programa completo que informa se um número é par ou ímpar.

```
# -*- coding: utf-8 -*-

"""
Informar se um número é par
(c) Margarida Madeira e Moura, 2022
"""

def par(n):
    """Função que determina se um número é par.
    
    par(n) devolve True se n for par; caso contrário, devolve False"""
    resultado = n % 2 == 0
    return resultado

def informa_par(n):
    """Função que imprime um valor com a informação que é par."""
    print('{} é par'.format(n))
    
def informa_impar(n):
    """Função que imprime um valor com a informação que é ímpar"""
    print('{} é impar'.format(n))

def test_par():
    """Função de teste da função par
    Apresenta o valor sse o número for par"""
    x = int(input())
    if (par(x)):
        informa_par(x)
    else:
        informa_impar(x)

if __name__ == '__main__':
    test_par()
```

Estude-o bem, para perceber onde estão as ideias e como as funções estão organizadas. De agora em diante, a submissão de soluções deverá considerar a organização que é ilustrada no exemplo acima.


### Tarefa A

Considere o [problema do DNA](http://rosalind.info/problems/dna/) em que se pretende apresentar, numa única linha, o número de carateres 'A', 'C', 'G' e 'T' existentes numa string.

Sabendo que não existem linhas vazias, prepare uma solução que contenha a função visada e uma função de teste para a leitura de uma linha e escrita da resposta.

Dica:

Pode criar uma string pela concatenação de strings, usando '+'

```
As = '5'
Cs = '2'
AsCs = As + ' ' + Cs
```


#### Casos de teste 

**Input 1**

```
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```

**Output 1**

```
20 12 17 21
```

**Input 2**

```
AGATTTTAATTATGAATGAAAAGGGAAATATGTATATGTGTGGATTAAAAAAAGAGTGTATGATAGAAGA
```

**Output 2**

```
32 0 17 21
```


Submeta no problema A.

### Tarefa B

Considere agora a [transcrição de DNA para RNA](http://rosalind.info/problems/rna/) em que se pretende obter uma string $u$ a partir de uma string $t$, sendo que as ocorrências do carater 'T' em $t$ são substituídas por 'U' em $u$.

Sabendo que não existem linhas vazias, prepare uma solução que contenha a função visada e uma função de teste para a leitura de uma linha e escrita da resposta.

#### Casos de teste 

**Input 1**

```
GATGGAACTTGACTACGTAAATT
```

**Output 1**

```
GAUGGAACUUGACUACGUAAAUU
```

**Input 2**

```
AGCAAAACAAACAGACA
```

**Output 2**

```
AGCAAAACAAACAGACA
```

Submeta no problema B.

### Tarefa C

Considere a determinação do [complemento de uma cadeia](http://rosalind.info/problems/revc/) de DNA. 

Numa string de DNA os símbolos 'A' e 'T' são complementares assim como os símbolos 'C' e 'G'. Pretende-se, a partir de uma string de DNA $s$, obter a string $s^c$ o que é conseguido pela inversão dos símbolos de $s$ e substituição de cada símbolo pelo símbolo complementar.

Sabendo que não existem linhas vazias, prepare uma solução que contenha a função, ou funções, visada(s) e uma função de teste para a leitura de uma linha e escrita da resposta.

#### Casos de teste 

**Input 1**

```
GTCA

```

**Output 1**

```
TGAC
```

**Input 2**

```
AAAACCCGGT
```

**Output 2**

```
ACCGGGTTTT
```

Submeta no problema C do Lab3.



## Referências 

As tarefas A, B e C são inspiradas nos exercícios da plataforma [Rosalind](http://rosalind.info/problems/locations/), sendo em cada uma das tarefas apresentada a fonte respetiva.


