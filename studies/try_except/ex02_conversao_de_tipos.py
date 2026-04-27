"""Conversão de Tipos: Peça para o usuário digitar uma lista de números separados por vírgula.
Tente converter cada elemento para int.
Se houver algo que não seja número, informe qual elemento falhou e pule para o próximo."""

lista = str(input('digite uma lista de numeros separados por virgula:   '))

lista_filtrada = lista.split(',')
numeros_convertidos = []

for elemento in lista_filtrada:
    try:
        num_convertido = int(elemento)
    except ValueError:
        print(f'o elemento digitado: {elemento} não pode ser convertido para inteiro')
    else:
        numeros_convertidos.append(num_convertido)

print(f'lista: {lista}')
print(f'lista filtrada: {lista_filtrada}')
print(f'numeros convertidos:    {numeros_convertidos}')

