#leia o nome de uma cidade e diga se começa com Santo
cid=str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
