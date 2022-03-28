expr = str(input('Digite a expressão matemática: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simb)
            break
if len(pilha) == 0:
    print('A expressão está válida')
else:
    print('A expressão não está válida')
