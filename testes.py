with open('Hallt.txt', 'r',encoding='utf-8') as file:
            cont = file.readlines()
rank = []
for l in cont:
        posicao, nome, pontuacao = l.strip().split(":")
        rank.append({"posicao": posicao, "nome": nome, "pontuacao": int(pontuacao)})
print(rank)
