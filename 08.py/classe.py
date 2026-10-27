class Musica:
    nome = ''
    artista = ''
    duracao = int

musica_rock = Musica()
musica_rock.nome = 'Sweet Child O Mine'
musica_rock.artista = 'Guns N Roses'
musica_rock.duracao = 5.56
musica_pop = Musica()
musica_pop.nome = 'Chicago'
musica_pop.artista = 'Michael Jackson'
musica_pop.duracao = 4.05
musica_rap = Musica()
musica_rap.nome = 'Vida Loka'
musica_rap.artista = 'Racionais MCs'
musica_rap.duracao = 5.03

musicas = [musica_rock, musica_pop, musica_rap]

print(vars(musica_rock))
print(vars(musica_pop))
print(vars(musica_rap))