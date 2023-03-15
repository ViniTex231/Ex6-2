jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO')
    if resp == 'N':
        break
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
