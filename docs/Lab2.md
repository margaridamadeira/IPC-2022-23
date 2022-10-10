# Lab2

Na resolução, tente simular o ambiente da festa: concentre-se e tente resolver no tempo atribuído.
<hr>

## Câmbio

```{figure} ./figures/MoneyExchange.jpg
---
width: 200px
name: Exchanging money
---
[Fonte da imagem: Money exchange vector image de art-sonik365. Acedido a 30 setembro 2022](https://www.vectorstock.com/royalty-free-vector/money-exchange-vector-7778171)
``` 

Vivemos num mundo global. Nem sempre a moeda é euros.
E para fazer compras online, é útil ter uns programas em Python para calcular os preços. Para já, quero saber qual o preço de um produto que está listado em libras esterlinas.

Para saber o preço em euros, preciso de saber a taxa de câmbio e o preço do produto na moeda original. Defino então a seguinte regra: primeiro leio a taxa de câmbio, depois leio o preço. Assim, com os dois valores, já posso chamar a minha função que calcula o preço em euros.


### Tarefa A

Prepare um programa em Python que leia a taxa de câmbio e o preço do produto e apresente o preço em euros. 

O input consiste em duas linhas, ambas representativas de números reais, sendo a primeira a taxa de câmbio e a segunda o preço do produto a converter. O output é um número real. 

**Casos de teste**

**Input 1**

```
0.8
100
```

**Output 1**

```
80.0
```

**Input 2**

```
1.20
100.0
```

**Output 2**

```
120.0
```

**Input 3**

```
1.1374283
1
```

**Output 3**

```
1.1374283
```

Submeta na tarefa A do concurso IPC_L2.

<div style="page-break-after: always"></div>

## Imperial para métrico

```{figure} ./figures/imperial2metric.png
---
width: 500px
name: Imperial to Metric
---
[Conversão de medidas de distância entre os sistemas imperial e métrico. Fonte da imagem: Pierce, Rod. "Metric - US/Imperial Conversion Charts" Math Is Fun. Ed. Rod Pierce. 15 Dec 2020. Acedido a 24 Nov 2021](http://www.mathsisfun.com/metric-imperial-conversion-charts.html)
```

O sistema imperial é usado por poucos países, mas queremos ser inclusivos. Vamos facilitar a conversão de medidas de distância do sistema imperial para o sistema métrico. 

Sabemos que uma polegada corresponde a 2.54 centímetro e que um pé corresponde a 12 polegadas.

Queremos então converter informação de distâncias de pé para centímetro.

    

### Tarefa B

Prepare um programa em Python que converta uma distância indicada pé para centímetro.

O input é uma única linha contendo um número inteiro que corresponde à distância em pé.
O output é um número real que corresponde à distância em centímetro.

**Requisito técnico**: deve usar a função ```converte_polegada_para_centimetro``` que foi fornecida no IPC_L0. 


**Casos de teste**

**Input 1**

```
1
```

**Output 1**

```
30.48
```

**Input 2**

```
10
```

**Output 2**

```
304.8
```

**Input 3**

```
5
```

**Output 3**

```
152.4
```

Submeta na tarefa B do concurso IPC_L2.

<div style="page-break-after: always"></div>
