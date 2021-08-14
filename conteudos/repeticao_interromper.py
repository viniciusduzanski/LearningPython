n = s = 0
while True:
    n = int(input('Digite um núemro: '))
    if n == 999:   # Se o usuário digitar 999 vai finalizar e não vai entrar na soma
        break   # Interrompe o while
    s += n
print(f'A soma vale {s}.')