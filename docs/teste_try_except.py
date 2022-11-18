""" Função fatorial - teste à instrução try-except  """

import sys

def fatorial_r(n):
    """Calculo do fatorial de um número.

    n! = n * (n-1)! para n > 1
    """

    assert type(n) is int, "n não é um inteiro: %r" % n
    assert n>0, "n não é maior que zero: %r" % n

    resultado = 1 # Elemento neutro da multiplicação 
    if (n>1):
        resultado = n * fatorial_r(n-1)
    
    return resultado

def test_try_except():
    """Exemplo de uso de try-except"""

    while True:
        try:
            x = int(input('Insira um número inteiro: '))
            z = fatorial_r(x)
            print('O fatorial de {} é {}'.format(x,z))

        except KeyboardInterrupt:
            print('\n Terminado.')
            sys.exit(0)

        except ValueError:
            print('Tente novamente.')

        except EOFError:
            print('\n Fim dos dados. Terminado.')
            sys.exit(0)

if __name__ == '__main__':
    test_try_except()

