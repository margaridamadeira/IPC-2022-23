# Lab9

Esta era a Festa de Janeiro prevista para o ano letivo de 2020-2021, que não aconteceu. 

<div style="page-break-after: always"></div>

## Eleições

```{figure} ./figures/Votar.jpg
---
height: 100px
name: Votar
---
```


Neste fim de semana teremos a Eleição para a Presidência da República. 
Cada secção de voto, apurará os resultados dos candidatos e preciso do apuramento de votos de cada freguesia.

A ordem com que os candidatos surgem no boletim eleitoral é já conhecida:
Eduardo Nelson da Costa Baptista, Marisa Isabel dos Santos Matias, Marcelo Nuno Duarte Rebelo de Sousa, Tiago Pedro de Sousa Mayan Gonçalves, André Claro Amaral Ventura, Vitorino Francisco da Rocha e Silva, João Manuel Peixoto Ferreira e Ana Maria Rosa Martins Gomes.
Os votos em Eduardo Nelson da Costa Baptista serão nulos mas até ao apuramento final nacional serão mantidos.

Cada secção de voto apurará os votos de cada candidato, os brancos e os nulos e produzirá um ficheiro com o formato indicado em seguida, substituindo o 0 (zero) pelo valor adequado. 

```
Eduardo Nelson da Costa Baptista,0
Marisa Isabel dos Santos Matias,0
Marcelo Nuno Duarte Rebelo de Sousa,0
Tiago Pedro de Sousa Mayan Gonçalves,0 
André Claro Amaral Ventura,0
Vitorino Francisco da Rocha e Silva,0
João Manuel Peixoto Ferreira,0
Ana Maria Rosa Martins Gomes,0
Votos brancos,0
Votos nulos,0
```

Cada frequesia tem um número variável de secções de voto. 
A ideia era que o programa aceitasse ficheiros com a designação geral <nome>\*<.extensão>. Mas alguns não querem nome, outros não usam extensão, outros nem nome nem extensão. Enfim, acordou-se que cada freguesia escolherá a designação que pretender, sendo o número da secção será representado pelo caracter \*. 

Preciso de consolidar essa informação e assim quero um programa que leia a designação geral do ficheiro e o número de ficheiros e apresente o resultado apurado.

### Tarefa A

Faça um programa em Python que leia da consola uma linha com o nome genérico dos ficheiros e o número de secções.

#### Input
O programa deverá ler da consola uma linha com o nome genérico dos ficheiros e o número de secções.

#### Output
O programa deverá escrever na consola o resultado apurado, com o mesmo formato di ficheiro lido e os valores totais.

#### Exemplo

Considere que tinha o ficheiro *Freguesia1.txt* com o conteúdo

```
Eduardo Nelson da Costa Baptista,1
Marisa Isabel dos Santos Matias,2
Marcelo Nuno Duarte Rebelo de Sousa,3
Tiago Pedro de Sousa Mayan Gonçalves,4 
André Claro Amaral Ventura,5
Vitorino Francisco da Rocha e Silva,6
João Manuel Peixoto Ferreira,7
Ana Maria Rosa Martins Gomes,8
Votos brancos,9
Votos nulos,10
```
e o ficheiro *Freguesia2.txt* com o conteúdo

```
Eduardo Nelson da Costa Baptista,9
Marisa Isabel dos Santos Matias,8
Marcelo Nuno Duarte Rebelo de Sousa,7
Tiago Pedro de Sousa Mayan Gonçalves,6
André Claro Amaral Ventura,5
Vitorino Francisco da Rocha e Silva,4
João Manuel Peixoto Ferreira,3
Ana Maria Rosa Martins Gomes,2
Votos brancos,1
Votos nulos,0
```

**Input 1**

Freguesia*.txt 2

**Output 1**

```
Eduardo Nelson da Costa Baptista,10
Marisa Isabel dos Santos Matias,10
Marcelo Nuno Duarte Rebelo de Sousa,10
Tiago Pedro de Sousa Mayan Gonçalves,10
André Claro Amaral Ventura,10
Vitorino Francisco da Rocha e Silva,10
João Manuel Peixoto Ferreira,10
Ana Maria Rosa Martins Gomes,10
Votos brancos,10
Votos nulos,10
```

Submeta na tarefa A no concurso IPC_L8.

## Triângulo de Pascal

```{figure} ./figures/TrianguloPascal.jpg
---
height: 300px
name: Triângulo de Pascal
---
```

O [triângulo de Pascal](https://mathworld.wolfram.com/PascalsTriangle.html) é uma representação gráfica usada determinação de coeficientes polinomiais na expansão de binómios.

A fórmula geral para a determinação dos coeficientes é dada por 

$$ C_{n,k} = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$ 

para $ n $ e $ k $ inteiros positivos e $ k \in [0, n] $.

### Tarefa

Faça um programa que leia da consola um número inteiro $n$ e apresente os coeficientes para a expansão de um binómio de grau $n$.

#### Input

O programa deve ler da consola um número inteiro.

#### Output

O programa deverá apresentar na consola, numa mesma linha, os coeficientes separados por espaços.

#### Exemplos

**Input 1**

```
3
```

**Output 1**

```
1 3 3 1
```

**Input 2**

```
7
```

**Output 2**
```
1 7 21 35 35 21 7 1
```

Submeta na tarefa B no concurso IPC_L8.

## Conjetura de Collatz

```{figure} ./figures/Collatz_conjecture.png
---
height: 300px
name: Collatz Conjecture
---
```
Fonte da figura: https://imgs.xkcd.com/comics/collatz_conjecture.png

Considere a função 

$$ f(x_n)=\begin{cases}
			 \frac{1}{2}x_{n-1} & \textrm{se $x_{n-1}$ for um número par}\\
			 3x_{n-1}+1        & \textrm{se $x_{n-1}$ for ímpar} 
	     	 \end{cases}
$$

[Collatz](https://mathworld.wolfram.com/CollatzProblem.html) conjeturou se a aplicação sucessiva dessa função terminaria sempre com o valor de $1$ (um) para valores iniciais positivos.

### Tarefa

Queremos testar a conjetura de Collatz, determinando ao fim de quantos passos se atinge o número $1$ (um) e qual o maior valor da sequência.

#### Input 

O programa deve ler da consola um número inteiro.

#### Output

O programa deve apresentar na consola, numa mesma linha e separados pelo espaço, ao fim de quantos passos se atingiu o valor unitário e o maior valor da sequência.

#### Exemplos

**Input 1**

```
1
```

**Output 1**

```
0 1
```

**Input 2**

```
2
```

**Output 2**
```
1 2
```

**Input 3**

```
3
```

**Output 3**
```
7 16
```

**Input 4**

```
4
```

**Output 4**
```
2 4
```

**Input 5**

```
5
```

**Output 5**
```
5 16
```

Submeta na tarefa C no concurso IPC_L8.