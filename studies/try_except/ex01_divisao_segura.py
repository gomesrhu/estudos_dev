"""Divisão Segura: Crie um programa que peça dois números e realize a divisão.
Trate o erro de divisão por zero (ZeroDivisionError) e entrada de dados inválida (ValueError)."""

#fiz um laço while para que o usuário seja forçado a inserir um número válido e também que não seja um zero no denominador
#caso retire o laço o programa funcionará normalmente, resta apenas tirar o "ok=True" do bloco else e trocar por um print com a exibição do resultado/produto
#OBS.: não sei se é boa prática fazer tanta coisa dentro de um único try como eu fiz, mas a princípio minha solução resolve o enunciado
ok = False

while not ok:

    try:
        n1 = str(input('Digite o numerador: '))
        n1 = float(n1)
        n2 = str(input('Digite o denominador: '))
        n2 = float(n2)
        produto = n1/n2
    except ValueError:
        print('algum dos números digitados não é válido')
    except ZeroDivisionError:
        print('Erro: DIVISÃO POR ZERO não permitida com números reais')
    else:
        ok = True
        #print(f'{n1}/{n2}={(n1/n2):.2f}')


if produto:
    print(f'{n1}/{n2}={produto:.2f}')



