'''# Projeto para o desenvolvimento da atividade 10, do curso Proz de Introdução à programação, pelo aluno Lucas da Silva Gonçalves.
# Project for activity 10, of the course Proz of Introducing Programming by Lucas da Silva Gonçalves.

A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente!
Dessa vez, eles precisam que você atualize o array de produtos. 
Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. 
Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. 
Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

Como desafio, adicione dois novos produtos da sua escolha à lista.'''

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
print(lista_produtos)

lista_produtos[1], lista_produtos[4] = "rímel", "cremes hidratantes"
lista_produtos.pop()

print(lista_produtos)