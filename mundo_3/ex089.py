boletim = []
while True:
    nome =  str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    boletim.append([nome, [nota1, nota2], media])
    while True:
        op = str(input('Você deseja cadastrar as notas de outro aluno? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        print('Opção inválida!', end=' ')
    if op == 'N':
        break
print('-='*30)
print(f'{"Nº":^4}{"NOME":^16}{"MÉDIA":^10}', )
print('-'*30)
for c in range(0, len(boletim)):
    print(f'{c:^4}{boletim[c][0]:^16}{boletim[c][2]:^10.1f}', )
print('-'*30)
while True:
    op = int(input('Mostrar as notas de qual aluno? [999 interromper] '))
    if op == 999:
        break
    elif 0 <= op < len(boletim):
        print(f'Notas de {boletim[op][0]} são {boletim[op][1]}')
    else:
        print('Opção inválida!', end=' ')
