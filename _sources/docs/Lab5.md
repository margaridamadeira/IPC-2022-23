# Lab5

## Objetivos de aprendizagem

Com este guião, exercitaremos:

1. a leitura da consola, vários valores por linha e até ao fim dos dados
1. escrita formatada
1. a utilização de listas



### Tarefa A

Pretende-se a ordenação crescente de sequências de números. Não sabemos quantas sequências temos nem quantos elementos por sequência. Para cada linha lida, ordenamos os elementos e apresentamos a sequência ordenada.

Vamos então preparar um programa que receba da consola, até ao fim dos dados, linhas com sequências de inteiros e, para cada linha, apresente a sequência por ordem crescente, com cada elemento separado por um espaço. 

Porque queremos um programa "completo", começamos pelas linhas que indicam ao Python que deve começar pela função de teste, ou seja

```
test_ordem_crescente()
```

Em seguida, sabemos que precisaremos da função de  *test_ordem_crescente*, responsável pela leitura, da função *ordem_crescente* e de uma função para apresentação dos resultados, seja *mostra_sequência_separada_por_espaços*. 
Mantemos as funções vazias (*pass* para indicar que não há nada a fazer).


O esboço do nosso programa fica assim:

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Resolução guiada
L4 - A
Programa que recebe da consola, até ao fim dos dados, 
linhas com sequências de inteiros e, 
para cada linha, apresenta a sequência por ordem crescente, 
com cada elemento separado por um espaço.

"""


def ordem_crescente():
    """Ordena uma sequência de números inteiros"""
    pass

def mostra_sequência_separada_por_espaços():
    """Apresenta os números inteiros separados por espaço"""
    pass

def test_ordem_crescente():
    """Lê várias linhas e, para cada linha lida, manda ordenar e mostrar."""
    pass  

test_ordem_crescente()
```

Usamos a abordagem apresentada para a {ref}`Leitura`.
Começamos por passar cada linha para uma lista e, para verificar, usamos uma primeira versão da função *mostra_sequência_separada_por_espaços*, que apresenta a lista ainda não formatada.

Usamos também algo que nos ajuda quando as funções começam a ser muitas: identificamos os tipos de dados, para que fique claro como estamos a organizar as atividades do programa. E depois a ajuda em linha também apresenta essa informação. Isto é opcional e apenas indicativo, o Python não vai verificar se os argumentos usados na chamada da função são ou não do tipo sugerido.


O nosso programa ficaria então assim:

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Resolução guiada
L4 - A
Programa que recebe da consola, até ao fim dos dados, 
linhas com sequências de inteiros e, 
para cada linha, apresenta a sequência por ordem crescente, 
com cada elemento separado por um espaço.

"""
import sys

def ordem_crescente(a: list) -> list:
    """Ordena uma sequência de números inteiros"""
    pass

def mostra_sequência_separada_por_espaços(a: list) -> None:
    """
    Função que apresenta uma lista, cada elemento separado por espaço.
    """
    print(a)

def test_ordem_crescente():
    """Lê várias linhas e, para cada linha lida, manda ordenar e mostrar."""
    while True:
        try:
            linha = input().split()
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)
        if linha:
            mostra_sequência_separada_por_espaços(linha)
        else:
            sys.exit(0)

    

test_ordem_crescente()

```


Com o nosso código num ficheiro chamado *ordenar_lista.py*, experimentamos.

```
python ordenar_lista.py 
1 4 7 3 6 2
['1', '4', '7', '3', '6', '2']
```

O resultado ainda não é exatamente o que pretendíamos.

Em primeiro lugar, a lista devia ser de inteiros. Há que converter! Podemos conseguir isso alterando o bloco do *try* para

```
            linha = input().split()
            lista = [int(x) for x in linha]
```

e, claro, revendo as utilizações da lista *linha*.


Em segundo lugar, era pedido que entre cada dois elementos existisse um espaço.
Aliás, deve haver um espaço entre cada dois elementos, mas não pode haver um espaço antes do primeiro elemento nem um espaço depois do último.

A nossa função *mostra_sequência_separada_por_espaços* poderia ficar assim, criando a string de saída e depois apresentando-a.

```
def mostra_sequência_separada_por_espaços(a: list) -> None:
    """
    Função que apresenta uma lista, cada elemento separado por espaços.
    """
    resultado = ''
    for i in a: 
        if len(resultado) == 0:
            resultado = str(i)
        else:
            resultado = resultado + ' ' + str(i)
    print(resultado)
```

Experimentemos outra vez. Deveremos ver o que introduzimos.

Ora o que falta agora é a ordenação da lista. O Python tem essa função mas há que ter cuidado pois essa função altera a lista original. Complete agora a função *ordem_crescente* para a ordenação crescente dos elementos inteiros de uma lista, inclua a chamada na função *test_ordem_crescente* e teste.


#### Casos de teste 

**Input 1**

```
2 9 1 8 6

```

**Output 1**

```
1 2 6 8 9
```

**Input 2**

```
1 4 7 3 6 2
34 27 39 6 2 100
5 -5 10 -10 -50 250


```

**Output 2**

```
1 2 3 4 6 7
2 6 27 34 39 100
-50 -10 -5 5 10 250
```

Submeta no problema A do concurso Lab4.

### Tarefa B

Fizemos uma série de experiências e a duração foi cronometrada de forma automática, em segundos. Queremos saber a duração de cada experiência em horas, minutos e segundos.

Prepare um programa em Python que leia uma sequência de números, um por linha e, para cada número lido, apresente esse valor no formato HH:MM:SS.

#### Casos de teste 

**Input 1**

```
7505
```

**Output 1**

```
02:05:05
```

**Input 2**

```
44135
```

**Output 2**

```
12:15:35
```


**Input 3**

```
7505
44135
```

**Output 3**

```
02:05:05
12:15:35
```

Submeta no problema B do Lab4.

### Tarefa C

Atualizamos os equipamentos e agora os tempos das experiências são apresentados em horas, minutos e segundos. Queremos saber o tempo total gasto nas experiências, em dias, horas, minutos e segundos.

Podíamos converter os tempos para segundos e depois de termos um total, converter então para o formato desejado. Mas a nossa conversão não considerava a possibilidade de traduzir valores de horas superiores a 24 em dias e horas. Assim, vamos lendo a duração das experiências e atualizando o tempo total.

Prepare um programa que leia os tempos da consola, um por linha, até ao fim dos dados e apresente, para cada linha lida, o tempo acumulado em dias, horas, minutos e segundos. Cada linha contém uma string com o formato *HH:MM:SS* em que *HH* correponde às horas, *MM* corresponde aos minutos e *SS* aos segundos. O tempo total, que deve ser apresentado num única linha, deverá respeitar o formato "DD:HH:MM:SS" (sem as aspas), em que *DD*, *HH*, *MM* e *SS* correspondem ao valores de dias, horas, minutos e segundos, respetivamente. Note que deve usar dois dígitos para cada valor.



#### Casos de teste 

**Input 1**

```
02:05:05
```

**Output 1**

```
00:02:05:05
```

**Input 2**

```
02:05:05
12:15:35
24:00:00
12:45:20
```

**Output 2**

```
00:02:05:05
00:14:20:40
01:14:20:40
02:03:06:00
```

Submeta no problema C do Lab4.

### Tarefa D

Estamos a registar o trabalho e verificámos que muitas vezes há erros na introdução das datas. É preciso então validar as datas introduzidas. 

Usamos o [formato padrão](https://pt.wikipedia.org/wiki/ISO_8601), *YYYY-MM-DD* em que *YYYY* representa o ano, *MM* representa o mês e *DD* o dia. Para simplificar, vamos considerar o [calendário gregoriano](https://pt.wikipedia.org/wiki/Ano_bissexto), ou seja, que temos datas a partir de 1582.

Relembremos agora as regras para as datas. Os meses são 12, isso é simples. Os dias variam, como sabemos do ditado popular: "Trinta dias tem novembro, abril, junho e setembro, vinte e oito terá um e os mais têm trinta e um". Fevereiro terá 28 dias, ou, num ano bissexto, 29. Um ano bissexto é divisível por quatro mas, se for um ano secular só será bissexto se for divisível por 400. E um ano secular é um ano divisível por 100.

Prepare um programa que leia as datas da consola, uma por linha, até ao fim dos dados. Por cada linha lida, o seu programa deve repetir a data lida, indicando se é válida ou não. Cada linha do input conterá *YYYY-MM-DD* em que *YYYY*, *MM* e *DD* são inteiros maiores que zero e representam ano, mês e dia, respetivamente. 
Cada linha do output repetirá o input acrescentando " -> Válida" (sem as aspas) ou " -> Inválida" (sem as aspas), se a data for válida ou não, respetivamente. 

#### Casos de teste

**Input 1**

```
2020-03-31
2020-03-45
2020-04-30
2020-04-31
2020-04-45
2019-02-28
2019-02-29
1600-02-29
1700-02-29
1800-02-29
1900-02-29
2000-02-29
2019-02-29
2020-02-29
2020-02-30
```

**Output 1**

```
2020:03:31 -> Válida
2020:03:45 -> Inválida
2020:04:30 -> Válida
2020:04:31 -> Inválida
2020:04:45 -> Inválida
2019:02:28 -> Válida
2019:02:29 -> Inválida
1600:02:29 -> Válida
1700:02:29 -> Inválida
1800:02:29 -> Inválida
1900:02:29 -> Inválida
2000:02:29 -> Válida
2019:02:29 -> Inválida
2020:02:29 -> Válida
2020:02:30 -> Inválida
```


Submeta no problema D do Lab4.
