# Lab0

## Objetivos de aprendizagem

Com este guião:

1. vamos saber como se faz a submissão ao Mooshak
1. veremos como preparar os programas para submeter


## Tarefa A

### Enunciado
Prepare um programa que apresente a mensagem "Hello world!" (sem as aspas).

### Caso de teste


**Output**

```
Hello world!
```

Submeta no problema A do concurso IPC_L0.


### Resolução

Usando o Spyder, abra um ficheiro novo.

Depois das linhas de comentário, escreva
    
```
print('Hello world!')
```

Note que deve começar na primeira coluna, pois os espaços à esquerda têm significado nos programas em Python.

Guarde o ficheiro que criou e execute-o. Se não estiver satisfeito com o resultado do seu programa, altere, grave e execute, até que esteja satisfeito.

Passamos agora para a submissão do programa. Usando um *browser* à sua escolha, aceda ao [Mooshak](http://deei-mooshak.ualg.pt/~mmadeira). Entre, com as suas credenciais no concurso IPC_L0.

Verifique que o problema selecionado é o que pretende, neste caso o A, e submeta o programa que preparou. 

Se a submissão ficou aceite, e já validou, esta tarefa está concluída.

## Tarefa B

### Enunciado

Sabendo que uma polegada corresponde a 2.54 centímetro, pretendemos converter as medidas em polegadas para centímetros.

Prepare um programa que leia uma distância em polegadas e apresente essa distância em centímetros.

### Caso de teste

**Input**

```
10
```

**Output**

```
25.4
```

Submeta no problema B do concurso IPC_L0.



### Resolução

A definição de uma função que converte de polegadas para centímetros vai ser explicada em detalhe na próxima aula teórica da Semana 2 usando *jupyter-notebook*.

Neste caso, só temos uma função e acrescentamos no fim do ficheiro as instruções de leitura de dados e escrita de resultados.

Assim, o nosso programa completo é:

```
# -*- coding: utf-8 -*-

"""
Ficheiro de resolução para submissão ao Mooshak
(c) Margarida Madeira e Moura, 2022
"""

def converte_polegada_para_centimetro(dist_polegadas):
    """Função que converte uma distância de polegadas para centímetros."""

    centimetros_por_polegada = 2.54
    resultado = dist_polegadas * centimetros_por_polegada
    return resultado 

x = int(input())
z = converte_polegada_para_centimetro(x)
print(z)
```

Reproduza então este programa para um novo ficheiro do Spyder, teste-o e submeta no problema B.
Depois da submissão ser aceite, valide-o.