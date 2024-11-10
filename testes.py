with open('questões.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

questions = eval(str(conteudo.split('=')[1]))
