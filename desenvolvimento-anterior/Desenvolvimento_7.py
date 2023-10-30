'''
# Projeto para o desenvolvimento da atividade 7, do curso Proz de Introdução à programação, pelo aluno Lucas da Silva Gonçalves.
# Project for activity 7, of the course Proz of Introducing Programming by Lucas da Silva Gonçalves.

Declare dois arrays, cada um com um mínimo de cinco elementos, e imprima eles no terminal usando o comando print().
O primeiro array deve conter os produtos de uma loja da sua escolha (loja de comida, materiais de construção, música,
etc). O segundo array deve conter os anos de nascimento de familiares e amigos seus.
Lembre-se de usar nomes descritivos para nomear cada variável, e de usar o tipo de dado apropriado para cada 
lista (strings, booleanos, números inteiros, floats).
'''

produtos_loja = ['banana', 'maçã', 'limão', 'cereja', 'uva']
print(produtos_loja)

for i in range(len(produtos_loja)):
    print(produtos_loja[i])


ano_nascimento = [1962, 1963, 1994, 2004, 2010]
print(ano_nascimento)

for i in range(len(ano_nascimento)):
    print(ano_nascimento[i])

