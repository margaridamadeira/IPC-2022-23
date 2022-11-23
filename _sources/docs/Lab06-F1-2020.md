# Lab6


Esta foi a primeira festa do ano letivo de 2020-2021.

Com este este exercício, exercitaremos uma festa de programação. 
Reveja a [Informação sobre as Festas de Programação](https://tutoria.ualg.pt/2021/mod/resource/view.php?id=37418).
Idealmente, reserve três horas e tente resolver os exercícios da festa de forma contínua.

Antes disso, reúna todos os seus materiais para consulta durante a festa e os seus programas anteriores (os que estão no Mooshak pode sempre ir lá buscá-los). Prepare uma pasta para cada problema que vai abordar, e a versão inicial da sua resolução.


## IMC

```{figure} ./figures/Laurel_and_Hardy_Silhouette.jpg
---
height: 300px
name: LaurelHardy
---
[Laurel and Hardy Silhouette](https://commons.wikimedia.org/wiki/File:Laurel_and_Hardy_Silhouette.jpg), de Cls14 em English Wikipedia, Public domain, via Wikimedia Commons.
```

Foi noticiado em Março de 2020 que a [OMS aponta Portugal como referência para prevenir obesidade nas crianças](https://news.un.org/pt/story/2020/03/1706141).

Manter um peso saudável é muito importante. A [Fundação Portuguesa de Cardiologia](http://www.fpcardiologia.pt/saude-do-coracao/factores-de-risco/obesidade/) refere que a obesidade afeta a longevidade e a qualidade de vida e indica como calcular o índice de massa corporal (IMC) e até como classificar o peso de um indivíduo.

Sabemos que $IMC = \frac{peso}{altura^2}$ e que os valores normais estão entre $18.5$ e $24.9$.

Para ajudar, vamos preparar um programa que, a partir do peso e da altura, apresente o IMC.

### Tarefa A

Prepare um programa em Python que receba o peso e altura de uma pessoa e apresente o índice de massa corporal (IMC). O índice de massa corporal, em $kg / m^2$, calcula-se dividindo o peso pelo quadrado da altura.

O input é uma única linha contendo dois números reais separados pelo caráter espaço e que correspondem ao peso e altura. 
O output é um número real, com três casas decimais, que corresponde ao valor do índice de massa corporal.
Se o peso ou altura não forem maiores que zero, o programa deverá produzir a mensagem "Dados inválidos." (sem as aspas).



**Casos de teste**

**Input 1**

```
50.0 1.50
```

**Output 1**

```
22.222
```

**Input 2**

```
45.0 1.50
```

**Output 2**

```
20.000
```

**Input 3**

```
-45 1.50
```

**Output 3**

```
Dados inválidos.
```

**Input 4**

```
45 0

```

**Output 4**

```
Dados inválidos.
```

Submeta na tarefa A do concurso IPC_L5.

<div style="page-break-after: always"></div>

## Pluviosidade


```{figure} ./figures/chuva-pexels-pixabay-459451.jpg
---
height: 300px
name: chuva
---
[Chuva](https://www.pexels.com/photo/rain-drops-459451/), de Pixabay em [Pexels](https://www.pexels.com/), CC0.
```


Temos tido alguma chuva ultimamente, mas pouco chove no Algarve. O [Sistema Nacional de Informação de Recursos Hídricos](https://snirh.apambiente.pt/) disponibiliza, entre outros dados, os valores diários da precipitação.

Vamos querer alguns valores estatísticos pelo que, para testar o programa, fomos [buscar](https://snirh.apambiente.pt/snirh/_dadosbase/site/janela_verdados.php?sites=920685102&pars=413026594&tmin=01/01/2020&tmax=30/09/2021) os valores de precipitação diária da estação de Barranco do Velho desde o início do ano. Retirámos a informação que não precisávamos e ficámos apenas com os valores da precipitação: em cada dia, numa linha, um valor real. 

Queremos saber qual o valor da precipitação acumulada, qual o maior valor de precipitação diária e em quantos dias choveu.

### Tarefa B

Prepare um programa em Python que leia da consola, até ao fim do input, uma sequência de números e apresente a soma dos valores lidos, o maior valor e o número de dias em que choveu (ou seja, o valor da precipitação é maior que zero).

O programa lerá tantas linhas quantos os dias contidos no registo. Em cada linha haverá um número (inteiro ou real) correspondente à precipitação num dia. Quando não choveu, o valor da precipitação é 0 (zero).
Ao terminar a leitura, o programa escreverá na mesma linha três valores separados por espaços. Os primeiros dois valores, em notação científica, correspondem à soma dos valores lidos e ao maior valor registado; o terceiro valor é um número inteiro que indica quantos dias choveu. 

**Casos de teste**

**Input 1**

```
0.1
0.6
1.8
2.7
1.5
6.4
0
0
```

**Output 1**

```
1.310000e+01 6.400000e+00 6
```

**Input 2**

```
0
0
0
0
0
0
0.1
0
0
0
0
0
0
```

**Output 2**

```
1.000000e-01 1.000000e-01 1
```

**Input 3**

```
0
0
0
0
0
0
0.6
1.8
2.7
1.5
6.4
0
0
0.2
0.4
0.5
20.2
4.9
0.3
```

**Output 3**

```
3.950000e+01 2.020000e+01 11
```

Submeta na tarefa B do concurso IPC_Lab5.

<div style="page-break-after: always"></div>

## Química à toa

```{figure} ./figures/tp-ualg.jpeg
---
height: 300px
name: Tabela Periódica
---
[Exposição “Desafios da Tabela Periódica”, na Biblioteca da UAlg](https://ualg.pt/pt/content/exposicao-desafios-da-tabela-periodica-pode-ser-visitada-na-biblioteca-da-ualg)
```

Fonte: [Problema C do ToPAS 2016](https://eventos.fct.unl.pt/sites/default/files/topas-lx/files/problemas_topaslx_2016.pdf)

Quando o Rui estava a estudar Química, escrevendo fórmulas
de compostos no caderno (como $CaCO_3$ , $Na_2CO_3$ e $H_ 2SO_4$ ),
apareceu a irmã mais nova, que ficou fascinada com aquelas
sequências de letras e algarismos. O pior é que ela não se calava,
exigindo que ele lhe explicasse como dividia uma sequência
grande em pedacinhos. Desesperado, o Rui enunciou as regras:

* Cada sequência de letras que começa com uma letra
grande (a irmã não conhecia a palavra “maiúscula”) representa um elemento;

* Se houver algum número a seguir ao elemento, esse é o número de átomos do elemento;
se não houver, o número de átomos do elemento é 1.


Depois, exemplificou com a fórmula do carbonato de cálcio, $CaCO_3$ , que tem um átomo de
cálcio (Ca), um átomo de carbono (C) e três átomos de oxigénio (O).
A irmã ficou muito contente e queria aprender mais Química. Mas ele convenceu-a a praticar.
Para poder regressar ao estudo rapidamente, decidiu escrever “fórmulas químicas” à toa e
até inventou símbolos químicos com 1, 2, 3, 4 e 5 letras. Por exemplo, deu-lhe a fórmula
$Ai_{19}Xpto_5Uus$ (que tem tamanho 12) para decompor.

### Tarefa C

Escreva um programa que, dada uma fórmula química inventada pelo Rui e terminada por
“.”, apresenta os elementos que ocorrem na fórmula e o número de átomos de cada um.

**Input**

Uma linha com uma fórmula química (inventada pelo Rui) terminada por “.”. A fórmula é
uma sequência de $n$ letras e algarismos, que começa com uma letra maiúscula e que não tem o
algarismo zero imediatamente a seguir a uma letra, nem uma letra minúscula imediatamente
a seguir a um algarismo. Nenhum elemento tem mais de cinco letras, nem ocorre mais do que
uma vez na fórmula. O número de algarismos seguidos não excede $n − 1$.


**Output**

O output tem uma linha por cada elemento que ocorre na fórmula. Cada linha tem um
elemento, um espaço, o número de átomos desse elemento e uma mudança de linha. Os
elementos têm de aparecer pela ordem em que ocorrem na fórmula.


**Casos de teste**

**Input 1**

```
CaCO3.
```

**Output 1**

```
Ca 1
C 1
O 3
```

**Input 2**

```
Ai19Xpto5Uus.
```

**Output 2**

```
Ai 19
Xpto 5
Uus 1
```

Submeta na tarefa C do concurso IPC_L5.
