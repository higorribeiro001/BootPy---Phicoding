import random

# atividade 1
print('-- Atividade 1 --')

nome = 'Higor'
sobrenome = 'Araujo'
idade = 20
ano_nascimento = 2023 - (idade + 1) # é que esse ano ainda farei 21 kk
maior_idade = idade >= 18
altura = 1.6

print('\n')
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_idade)
print('Altura em metros:', altura)

# atividade 2
par = int('0')
impar = int('1')

print('\n')
print('-- Atividade 2 --')
print('\n')

print('>>>>>> Jogo do ímpar/par <<<<<<\n')
while True:
    opcao = int(input('Opções: \n0 -> par \n1 -> ímpar \nOutro qualquer -> sair\n'))

    if opcao == impar:
        print('Você escolheu ímpar!\n')
    elif opcao == par:
        print('Você escolheu par!\n')
    else:
        print('Jogo Finalizado!')
        break

    num_user = int(input('Digite um número: '))
    num_pc = random.randint(0, 1000)
    print('A máquina escolheu: ', end=f'{num_pc}\n')

    if (num_user + num_pc) % 2 == opcao == par:
        print('Você venceu!')
    elif (num_user + num_pc) % 2 == opcao == impar:
        print('Você venceu!')
    else:
        print('Você perdeu!')


