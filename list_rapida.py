if __name__ == '__main__':
    list = []
    n = int(input())
    for _ in range(n):
        command, *args = input().split
        if command == "print":
            print(list)
        else:
            getattr(list, command)(*map(int, args))
'''
Considere uma lista (). Você pode executar os seguintes comandos: list = []

insert i e: Insira o número inteiro na posição .
print: Imprima a lista.
remove e: Exclua a primeira ocorrência de inteiro .
append e: Insira um número inteiro no final da lista. 
sort: Classifique a lista.
pop: Retire o último elemento da lista.
reverse: Inverta a lista.
Inicialize sua lista e leia o valor de seguido por linhas de comandos onde cada comando será dos tipos listados acima. Itere por cada comando em ordem e execute a operação correspondente em sua lista. 

'''