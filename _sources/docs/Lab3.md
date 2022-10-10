# Lab3

## Objetivos de aprendizagem

Com este guião, exercitaremos:

1. a utilização de strings
1. o uso de condições no controlo de fluxo do programa 
1. a utilização de funções do Python

e continuaremos a usar o Mooshak para verificar o resultado dos programas desenvolvidos.



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


Submeta no problema A do Lab3.

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

Submeta no problema B do Lab3.

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


