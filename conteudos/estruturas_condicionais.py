nome = str(input('Qual é seu nome? '))
if nome == 'Vinícius':
    print('Que nome bonito!')
elif nome == 'Juscilei' or nome == 'Reinaldo' or nome == 'Leonilda':
    print('Seu nome não é muito comum!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
