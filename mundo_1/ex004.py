n=input('Digite algo: ')
print('O tipo primitivo dessa palavra é:',type(n))
print('Só tem espaços?',n.isspace())
print('É um número?',n.isnumeric())
print('É alfabético?',n.isalpha())
print('É alfanumérico?',n.isalnum())
print('Está em maiúsculo?',n.isupper())
print('Está em minúsculo?',n.islower())
print('Está capitalizada?',n.istitle())
