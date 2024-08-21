if __name__ == '__main__':
    arquivos = []
    for _ in range(int(input)):
        Name = input()
        score = int(input())
        arquivos.append((Name, score))
    mark = list(set(aleatorio[1] for aleatorio in arquivos))
    mark.sort()

    if len(mark) < 2:
        raise ValueError("Errado")
    else:
        segundo_no_ranking = mark[1]
        portifolio = [aleatorio[0] for aleatorio in arquivos if aleatorio[1] == segundo_no_ranking]
        portifolio.sort()
        for name in portifolio:
            print(name)
# Dados os nomes e notas de cada aluno em uma classe de alunos, armazene-os em uma lista aninhada e imprima o(s) nome(s) de qualquer aluno com a segunda nota mais baixa.
# Nota: Se houver vários alunos com a segunda nota mais baixa, ordene seus nomes em ordem alfabética e imprima cada nome em uma nova linha.
