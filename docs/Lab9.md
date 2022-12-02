# Lab9


Note bem:

+ Cotação deste guião: 2 pontos
+ Submeta cada uma das tarefas no problema correspondente do concurso IPC_L9.
+ Prazo limite de submissão: 23h59m de 9 de dezembro
+ Prazo limite de validação das submissões aceites: 16 de dezembro.

## Objetivos de aprendizagem

Com este guião, exercitaremos:

+ o uso de listas
+ o uso de dicionários


## Combustíveis

Felizmente o preço dos combustíveis parece estar a baixar, ou assim ouvi nos noticiários. Para verificar, fui ao [site oficial](https://precoscombustiveis.dgeg.gov.pt/estatistica/preco-medio-diario/#download) e obtive os dados do último mês.

Agora só preciso de os tratar, tirar as minhas próprias conclusões e quem sabe, publicá-las num artigo ou relatório.

A primeira coisa que preciso é de ser capaz de tratar os dados.

Depois, nas próximas semanas, tratarei de obter os dados de um ficheiro, bastando indicar o nome. 
Esses dados estão num ficheiro `.csv` um formato também considerado pelo Microsoft Excel. Em Python também há formas de tratar estes ficheiros, e isso será ainda outro aspeto do mesmo tema.

Para já, vou manter as coisas simples. `csv` quer dizer *comma-separated values*, ou seja, valores separados por *ponto e vírgula*. 

Um extrato do ficheiro está disponível em [extrato_Postos.csv](https://tutoria.ualg.pt/2022/mod/resource/view.php?id=82660).

### Ler e escrever

Para ler esses valores pela linha de comandos, sabendo que os valores estão separados por *ponto e vírgula*, basta-me indicar que quero uma lista onde o separador dos elementos é o *ponto e vírgula*.

#### Tarefa A
Pretendo ler e apresentar o cabeçalho e, até ao fim dos dados, ler as demais linhas e apresentá-las.
Prepare um programa em Python que leia os dados até ao fim do input e apresente as linhas lidas.

Na apresentação, quer do cabeçalho quer das linhas, considere a formatação definida para o cabeçalho do esboço de programa dado abaixo, ou seja, as barras verticais devem ficar alinhadas. Para tanto, o primeiro campo ocupa 13 espaços, é seguido por " | " (sem as aspas), seguindo-se o segundo campo centrado em 45 espaços, seguido por " | " (sem as aspas) e, finalmente, o terceiro campo com 11 espaços e justificado à direita.

Para o efeito, considere o esboço de programa fornecido abaixo e complete a função `mostra_linha`.

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Tue Nov 29 20:03:19 2022

    @author: mmadeira
    """

    import sys


    def mostra_linha(linha: list)-> None:
        """
        Apresenta os dados no formato pedido

        Parameters
        ----------
        linha : list
            linha do ficheiro (excluindo cabeçalho).

        >>> mostra_linha(['"2022-10-30"', '"Gasolina especial 98"', '"2,0687 €"'])
        "2022-10-30"  |             "Gasolina especial 98"            |  "2,0687 €"
        >>> mostra_linha(['"2022-10-30"', '"Gasolina 98"', '"2,0616 €"'])
        "2022-10-30"  |                 "Gasolina 98"                 |  "2,0616 €"
        """
        pass
        

    def test_combustíveis():
        cabeçalho = input().split(';')
        topo_data, topo_tipo_combustível, topo_preço = cabeçalho
        print('{0:14s} | {1:45s} | {2:>11s}'.format(topo_data.title(), topo_tipo_combustível.title().center(45), topo_preço.title()))
        while True:
            try:
                line = input().split(';')
            except (EOFError, KeyboardInterrupt):
                sys.exit(0)
            if line:
                mostra_linha(line)
            else:
                sys.exit(0)

    if __name__ == '__main__':
        test_combustíveis()


No Spyder, use o teste da docstring para aferir a correção da apresentação de resultados, fazendo

    import doctest

e, a cada nova versão da função que carregar para a consola

    doctest.testmod()

Submeta na tarefa A.


### Tratar os dados lidos

Pretendo ler e apresentar o cabeçalho e, até ao fim dos dados, ler as demais linhas e apresentá-las de forma mais cuidada: vou retirar as aspas das strings e vou apresentar o preço depois de convertido para um número real.

#### Tarefa B

Prepare um programa em Python que leia os dados até ao fim do input e apresente as linhas lidas.
A primeira linha de input contém o cabeçalho sendo seguida pelas linhas de dados. Cada linha de dados contém três campos, separados por ';' e delimitados por '"'; a informação nesses campos corresponde respetivamente à data, ao tipo de combustível e ao preço do combustível. O formato usado no preço inclui a vírgula como separador decimal e o símbolo da moeda usada (€).



Para o efeito, acrescente a função `converte_dados` ao programa da tarefa anterior e complete-a.


    def converte_dados(linha:list) -> list:
        """
        Retira as aspas da data e tipo de combustível e converte o preço para real.

        Parameters
        ----------
        linha : list
            linha do ficheiro (excluindo cabeçalho).

        Returns
        -------
        list
            lista contendo uma strings para data e tipo de combustível e 
            um número real para preço.
            
        >>> converte_dados(['"2022-10-30"', '"Gasolina especial 98"', '"2,0687 €"'])
        ['2022-10-30', 'Gasolina especial 98', 2.0687]
        """
        pass


Submeta na tarefa B.

### Separar os tipos de combustíveis

Pretendo agora separar os preços de cada tipo de combustível e saber o preço médio de cada tipo de combustível.

#### Tarefa C

Prepare um programa em Python que apresente o preço médio de cada tipo de combustível.
A primeira linha de input contém o cabeçalho sendo seguida pelas linhas de dados. Cada linha de dados contém três campos, separados por ';' e delimitados por '"'; a informação nesses campos corresponde respetivamente à data, ao tipo de combustível e ao preço do combustível. O formato usado no preço inclui a vírgula como separador decimal e o símbolo da moeda usada (€).

O output é composto por tantas linhas quantos os tipos de combustível e cada linha contém a designação do tipo de combustível seguida por ": " (sem as aspas) e o valor médio desse tipo de combustível.

**Requisito técnico**: carregue os dados lidos para um dicionário onde o tipo de combustível é a chave e associado à chave está uma lista com os preços desse tipo de combustível.

Sugestão de resolução: 

+ Implemente uma função que receba uma string e um número real e os apresente no formato pretendido.

+ Implemente uma função que receba uma lista e devolva o valor médio dos elementos dessa lista.
+ Implemente uma função que receba uma linha lida e guarde, num dicionário, o preço na coleção de valores associados à chave que é a designação do tipo de combustível. 
+ Implemente uma função que receba um dicionário e, para cada chave do dicionário, obtenha a média dos valores e apresente a chave e valor.

Considere usar os esboços seguintes:

    def mostra_combustivel_valor(tipo: str, valor: float) -> None:
        """
        Apresenta o tipo de combustível e o valor.

        Parameters
        ----------
        tipo : str
            O tipo de combustível
        valor : float
            o valor a apresentar

        >>> mostra_combustivel_valor('Exemplo de tipo de combustível', 3.5)
        Exemplo de tipo de combustível: 3.5
        """
        pass



    def calcula_média(lista: list) -> float:
        """
        Devolve a média de uma lista de valores numéricos.

        Parameters
        ----------
        lista : list
            Uma lista não nula de valores numéricos.

        Returns
        -------
        float
            A média aritmética dos valores da lista.

        >>> calcula_média([3])
        3
        >>> calcula_média([3, 5])
        4
        >>> calcula_média([3, 5.0, 12, -1])
        4.75
        """
        pass


    def guarda_no_dicionário(dicio: dict, tipo: str, valor: float) -> dict:
        """
        Guarda no dicionário o valor associado à chave representada pelo tipo.
        
        Se a chave não existir, cria essa chave e associa uma lista com o valor;
        se a chave existir, acrescenta o valor à lista associada a essa chave.

        Parameters
        ----------
        tipo : str
            DESCRIPTION.
        valor : real
            DESCRIPTION.

        >>> guarda_no_dicionário({}, "Gasóleo", 0.7)
        {'Gasóleo': [0.7]}
        >>> guarda_no_dicionário({'Gasóleo': [0.7]}, "Gasóleo", 0.8)
        {'Gasóleo': [0.7, 0.8]}
        >>> guarda_no_dicionário({'Gasóleo': [0.7, 0.8]}, "Gasolina", 1.2)
        {'Gasóleo': [0.7, 0.8], 'Gasolina': [1.2]}
        """
        pass


    def mostra_resultado(dicio: dict) -> None:
        """Percorre o dicionário para produzir a listagem desejada.
        
        >>> mostra_resultado({'Gasóleo': [0.7]})
        Gasóleo: 0.7
        >>> mostra_resultado({'Gasóleo': [0.7, 0.8], 'Gasolina': [1.2]})
        Gasóleo: 0.75
        Gasolina: 1.2
        """
        pass


Submeta na tarefa C.











