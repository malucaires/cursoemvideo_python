#Digite a largura e altura e determine a área e qtde de tinta para pintar (1L equivale a 2m²)
alt=float(input('Digite a altura da parede: '))
lar=float(input('Digite a largura da parede: '))
area=alt*lar
print('Sua parede tem a dimensão de {:.2f}x{:.2f}, área de {:.2f}m² e a quantidade de tinta é {:.2f}L.'.format(alt,lar,area,area/2))