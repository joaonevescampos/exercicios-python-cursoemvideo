nome = input('Qual seu nome completo?')
print('Seu nome em maiúsculo é: {}.'.format(nome.upper()))
print('Seu nome em minúsculo é: {}.'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome.replace(' ',''))))
nome.replace('',' ')
pnome = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(pnome[0])))