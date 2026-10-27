"""#Criação de variáveis
nome = 'Kauan'
idade = 18

#Abordagem simples
print('Meu nome é: ', nome, 'e tenho: ', idade, 'anos.')

#Abordagem com f-string
print(f'Meu nome é: {nome} e tenho: {idade} anos.')

#Abordagem com .format()
print('Meu nome é: {} e tenho: {} anos.'.format(nome, idade))

#Abordagem da % (formatação de strings antiga - python 2)
print('Meu nome é: %s e tenho: %i anos,'% (nome, idade)) """

"""print('S', 'E', 'N', 'A', 'C', sep='\n')"""

#print('S', 'E', 'N', 'A', 'C', sep='\n')

#Imprimir valor de pi arredondado
"""pi = 3.14159

#Abordagem de f-string
print(f'\nO valor arredondado de pi é: {pi:.2f}\n')

#Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}\n'.format(pi))

#Abordagem da função round()
print('O valor arredondado de pi é: ', round(pi,2))"""

"""from math import pi 

print(pi)
print(round(pi, 2))"""

#Questão_1 
"""numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')"""

#Questão_2
"""idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Criança')
elif idade <= 18:
    print('Adolescente')
elif idade >= 100:
    print('Na cova')
elif idade >= 60:
    print('Veio')
else:
    print('Adulto')"""

#Question_3
"""usuario = input('Digite o nome de úsuario: ')
senha = input('Digite a senha: ')

if usuario == 'Kauan' and senha == '1721':
    print('Login realizado com sucesso!')
else: 
    print('Usuário ou senha incorreta.')"""

#Question_4
"""x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

if x > 0  and y > 0:
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quadrante')
elif x < 0 and y < 0:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadranete')
else:
    print('O ponto está localizado no eixo ou na origem')"""

#Teste_2
# Definindo uma tupla de coodernadas Geográficas
"""coodernadas_GPS = (40.7128, -74.0060)

# Exibindo as coodernadas
print('Coodernadas GPS:')
print('Latitude:', coodernadas_GPS[0])
print('Longitude:', coodernadas_GPS[1])"""

#Teste_3
"""numero = -1
for _ in range(3): #Supondo um número máximo de tentativas = 3
    numero = int(input('Digite um número positivo: '))
    if numero >= 0:
        break
print('Você Digitou: ', numero)

num = -1
while num <= 0:
    num = int(input('Digite um número positivo: '))
print('Você Digitou: ', num)"""













