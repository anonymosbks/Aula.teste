class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

print(restaurante_praca.nome)

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

categoria = Restaurante.categoria

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(restaurante_pizza.categoria == 'Fast Food')

restaurante_pizza.ativo = True

print(restaurante_praca.nome, restaurante_praca.categoria)
print(restaurante_pizza.nome, restaurante_pizza.categoria)