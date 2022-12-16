# Complemento da Festa

**Introdução à programação científica - Bioengenharia**

**16 de dezembro de 2022, das 10h40 às 11h30**

<hr>
Note bem:

+ Submeta a tarefa no concurso IPC_F31 do *Mooshak* em http://deei-mooshak.ualg.pt/~mmadeira

+ Prazo limite das validações das submissões aceites: 21 de dezembro de 2022
+ A cotação da submissão aceite no *Mooshak* e validadas: 40 pontos complementares.
<hr>



## O que é isto?



```{figure} ./figures/Roda.jpg
---
height: 300px
name: Codon wheel
---
Codon wheel
```

Publicado anteriormente como problema What da TIUP 2008.


Já lá estavam há algum tempo quando *o* encontraram. *Aquilo* era estranho, estranhamente moldado e feito de uma substância não identificada. Mesmo os veteranos mais experientes não conseguiam identificar o que era aquela coisa amarelada ou se tinha algum valor. Estavam a ficar sem tempo e em breve teriam de deixar o pequeno asteroide. Devem levá-lo? O peso do espaço e da bagagem para a viagem de volta à Terra era caro. E não era apenas o custo que tinha de ser considerado: se fosse um artefacto de uma cultura alienígena, todos falariam deles; da mesma forma, todos falariam deles se consumissem recursos escassos para trazer de volta ao planeta Terra um bocado de lixo centenário de uma expedição anterior. 

Só podiam fazer alguns testes rudimentares, rápidos, usando o computador da nave. Eles poderiam analisar a lama que cobria *aquilo* e procurar os aminoácidos das proteínas. Uma sequência comprimida das proteínas poderia ser enviada para a Terra para ser comparada com as bases de dados. Dependendo da resposta recebida, poderiam decidir se trariam *aquilo* de volta à Terra ou se *o* deixariam por lá.


### Tarefa 

A informação genética armazenada em moléculas de RNA pode ser representada por palavras de três letras chamadas codões. As letras são A, U, C ou G. Mas cada codão corresponde a um único aminoácido, que pode ser codificado por uma única letra. 

Considere que uma moldura de leitura aberta (*open reading frame*) começa sempre por AUG. Este é o codão do aminoácido metionina, codificado por 'M'. Cada quadro de leitura começa por AUG e é terminado por um dos codões UAG, UGA ou UAA. 
É-lhe pedido que crie um programa que leia uma sequência de letras, identifique a moldura de leitura aberta e produza a correspondente de proteínas de uma letra, utilizando as tabelas abaixo.


```{figure} ./figures/TabelaRNA.jpg
---
height: 300px
name: Tabela RNA
---
Tabela RNA
```


```{figure} ./figures/Cod3para1.jpg
---
height: 300px
name: Códigos
---
Códigos
```


A saída de qualquer um dos codões STOP deve ser representada por *(asterisco).
Todas as sequências de letras têm pelo menos um codão inicial. Um codão STOP termina a moldura de leitura atual. Se não aparecer nenhum codon STOP, a moldura de leitura atual, se houver uma, estende-se até à extremidade da string. As letras entre um codão STOP e um codão inicial devem ser ignoradas.


**Input**

O input tem apenas uma linha. Esta linha contém uma string composta inteiramente por letras maiúsculas 'A', 'C', 'G' e 'U'. O comprimento da string não excede 10000.

**Output**

O output tem apenas uma linha, contendo a string que representa a sequência de aminoácidos, cada um denotada por uma única letra, como explicado na descrição da tarefa.


**Casos de teste**

**Input 1**

```
AUGCAAUAA
```

**Output 1**

```
MQ*
```

**Input 2**

```
UGCAUGCAAUAGGU
```

**Output 2**

```
MQ*
```

**Input 3**

```
GUGCAUGCAAUGAAUGAACUAAU
```

**Output 3**

```
MQ*MN*
```

**Input 4**

```
UAUGCCCUAUAGGGCUUGCCUAUAGAUGCCCGUCACGCGGUACGUAAGAUCA
```

**Output 4**

```
MPYRACL*MPVTRYVRS
```



Submeta no concurso IPC_2021_P6.
