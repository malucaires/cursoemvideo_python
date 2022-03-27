#Verificar formatação
tabela = ('Fortaleza', 'Athletico', 'Atlético', 'Bragantino', 'Bahia', 'Fluminense',
          'Palmeiras', 'Flamengo', 'Atlético', 'Corinthians', 'Ceará', 'Santos',
          'Cuiabá', 'Sport', 'São Paulo', 'Juventude', 'Internacional', 'Grêmio',
          'América', 'Chapecoense')
print('-='*20)
print(f'Lista de times: {tabela}')
print('-='*20)
print(f'Os primeiros cinco colocados são: {tabela[0:5]}', end='')
print('\n','-='*20)
print(f'Os últimos quatro colocados são: {tabela[-4:]}', end='')
print('\n','-='*20)
print(f'Os times em ordem alfabética são:{sorted(tabela)}')
print('-='*20)
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}º posição')
print('FIM')