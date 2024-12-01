import os
import random
import time
import textwrap
os.system('cls')

def jogo():
      while True:
            os.system('cls')
            print('-=-=-=-=AskMe-=-=-=-=\n')
            print('Selecione o modo:\n\n'
                  '1-Questões Fixas\n\n'
                  '2-Limite de Tempo\n\n'
                  '3-Tente não errar\n\n'
                  '4-Hall da fama\n\n'
                  '0-Exit\n')
            time.sleep(0.5)
            while True:
                  try:
                        seleção = int(input('Digite o número do modo: '))
                        break
                  except:
                        print('Invalido, tente novamente!')
                        time.sleep(2)
            if seleção == 1:
                  fixas(questions)
            elif seleção == 2:
                  Ltempo(questions, 306)
            elif seleção == 3: 
                  Aterrar(questions)
            elif seleção == 0:
                  os.system('cls')
                  print('-=-=-=PROGRAMA ENCERRADO-=-=-=-')
                  break
            elif seleção == 4:
                  hall_da_fama()
            else:
                  print('Invalido, tente novamente!')
                  time.sleep(2)

def hall_da_fama():
      while True:
            os.system('cls')
            print('-=-=-=-=-=HALL DA FAMA=-=-=-=-=-\n\n'
                  '1-Fixas\n\n'
                  '2-Tempo\n\n'
                  '3-Até errar\n\n'
                  '4-voltar\n')
            while True:
                  try:
                        n = int(input('Selecione o hall: '))
                        break
                  except:
                        print('Invalido, tente novamente.')
                        time.sleep(2)
            if n == 1:
                  with open('Hallf.txt', 'r', encoding='utf-8')as file1:
                        c1 = file1.read()
                  print(f'\n{c1}')
                  for i in range (8, 0, -1):
                        print(f'\r{i}...', end='')
                        time.sleep(1)
            elif n == 2:
                  with open('Hallt.txt', 'r', encoding='utf-8')as file2:
                        c2 = file2.read()
                  print(f'\n{c2}')
                  for i in range (8, 0, -1):
                        print(f'\r{i}...', end='')
                        time.sleep(1)
            elif n == 3:
                  with open('Halle.txt', 'r', encoding='utf-8')as file3:
                        c3 = file3.read()
                  print(f'\n{c3}')
                  for i in range (8, 0, -1):
                        print(f'\r{i}...', end='')
                        time.sleep(1)
            elif n == 4:
                  break
            else:
                  print('Invalido, tente novamente.')
                  time.sleep(2)

def fixas(questions): 
      caracteres = 70
      pontos = 0
      ajudas = 3
      aux = 0
      os.system('cls')
      print('-=-=-=-=-=-=Questões fixas-=-=-=-=-=-=\n\n'
            'Neste modo você enfrentará 15 questões\n\n'
            'Acerte quantas puder para maiores pontuações!')
      for i in range (5, 0, -1):
            print(f'\r{i}...', end='')
            time.sleep(1)
      os.system('cls')
      fix = 15
      for i in range(fix):
            Qatual = random.choice(questions)
            questions.remove(Qatual)
            t_quebrado = textwrap.fill(Qatual['questionText'], width=caracteres)
            print(f'{t_quebrado}\n')
            print(f'A) {Qatual['option1']}\n')
            A = Qatual['option1']
            print(f'B) {Qatual['option2']}\n')
            B = Qatual['option2']
            print(f'C) {Qatual['option3']}\n')
            C = Qatual['option3']
            print(f'D) {Qatual['option4']}\n')
            D = Qatual['option4']
            print(f'E) {Qatual['option5']}\n')
            E = Qatual['option5']
            print('9-Ajuda')
            print(f'                                                                PONTOS:{pontos}\n'
                  f'                                                                AJUDAS:{ajudas}')
            while True:
                  resp = input('Insira a alternativa: ').strip().upper()
                  if resp == 'A':
                        if A == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == 'B':
                        if B == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == 'C':
                        if C == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == 'D':
                        if D == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == 'E':
                        if E == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == '9':
                        while True:
                              if ajudas > 0:
                                    print('Ajudas:\n'
                                          '1-Dica\n'
                                          '2-Pular questão\n'
                                          '3-Eliminar alternativas\n'
                                          '4-Voltar')
                                    while True:
                                          try:
                                                ajd = int(input('Insira sua escolha: '))
                                                break
                                          except:
                                                print('\nDigite uma opção valida.\n')
                                    if ajd == 1:
                                          dica = ''.join(Qatual['hint'])
                                          text_quebrado = textwrap.fill(dica, width=caracteres)
                                          print('\nDica: ')
                                          print(text_quebrado)
                                          print()
                                          ajudas -= 1
                                          break
                                    elif ajd == 2:
                                          ajudas -= 1
                                          break
                                    elif ajd == 3:
                                          os.system('cls')
                                          alternativas = [Qatual['option1'],Qatual['option2'],Qatual['option3'],Qatual['option4'],Qatual['option5']]
                                          t_quebrado = textwrap.fill(Qatual['questionText'], width=caracteres)
                                          print(f'{t_quebrado}\n')
                                          for i in range(3):
                                                alt_random = random.choice(alternativas)
                                                if alt_random != Qatual['answer']:
                                                      alternativas.remove(alt_random)
                                          for i in alternativas:
                                                if i == A:
                                                      print(f'A){i}\n')
                                                elif i == B:
                                                      print(f'B){i}\n')
                                                elif i == C:
                                                      print(f'C){i}\n')
                                                elif i == D:
                                                      print(f'D){i}\n')
                                                elif i == E:
                                                      print(f'E){i}\n')
                                          print('9-Ajuda')
                                          print(f'                                                                PONTOS:{pontos}\n'
                                                f'                                                                AJUDAS:{ajudas}')
                                          ajudas -= 1
                                          break
                                    elif ajd == 4:
                                          break
                                    else:
                                          print('\nDigite uma opção valida.\n')
                             
                              if ajudas == 0:
                                    print('Ajuda indisponivel')
                                    break
                        if ajd == 2:
                              break 
                  else:
                        print('\nDigite uma opção valida.\n')
            if pontos // 60 != aux and ajudas < 3:
                  ajudas +=1
                  aux += 1
            for i in range (8, 0, -1):
                  print(f'\r{i}...', end='')
                  time.sleep(1)
            os.system('cls')
      atualizar_ranking('Hallf.txt', pontos)
      while True:
            try:
                  rsp=int(input('Jogar novamente? 1-Sim | 2-Não: '))
                  if rsp == 1 or rsp ==2:
                        break
                  else:
                        print('Invalido, digite novamente.')
            except:
                  print('Invalido, digite novamente.')
      if rsp == 1:
            questions = regenerar()
            fixas(questions)

def regenerar():
      chaves=['category', 'value', 'questionPath', 'questionText', 'option1', 'option2', 'option3',
      'option4', 'option5', 'answer', 'explanation', 'hint']
      with open('Banco_de_Questões', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
      for key in chaves:
            conteudo = conteudo.replace(key, f"'{key}'")

      questions = eval(conteudo[12:])
      return questions

def Ltempo(questions,tempo_limite):
      caracteres = 70
      pontos = 0
      ajudas = 3
      aux = 0
      start_time = time.time()
      end_time = start_time + tempo_limite
      os.system('cls')
      print('-=-=-=-=-=-=Limite de Tempo-=-=-=-=-=-=\n\n'
            'Neste modo você enfrentará 15 questões com 5 minutos de limite de tempo!\n\n'
            'Acerte no melhor tempo para maiores pontuações!')
      for i in range (5, 0, -1):
            print(f'\r{i}...', end='')
            time.sleep(1)
      os.system('cls')
      fixas = 15
      for i in range(fixas):
            Qatual = random.choice(questions)
            questions.remove(Qatual)
            t_quebrado = textwrap.fill(Qatual['questionText'], width=caracteres)
            print(f'{t_quebrado}\n')
            print(f'A) {Qatual['option1']}\n')
            A = Qatual['option1']
            print(f'B) {Qatual['option2']}\n')
            B = Qatual['option2']
            print(f'C) {Qatual['option3']}\n')
            C = Qatual['option3']
            print(f'D) {Qatual['option4']}\n')
            D = Qatual['option4']
            print(f'E) {Qatual['option5']}\n')
            E = Qatual['option5']
            print('9-Ajuda')
            print(f'                                                                PONTOS:{pontos}\n'
                  f'                                                                AJUDAS:{ajudas}')
            if time.time() > end_time:
                  print("\nTempo esgotado! Fim do jogo.")
                  time.sleep(2)
                  break
            tempo_restante = int(end_time - time.time())
            print(f"\nTempo restante: {tempo_restante} segundos")

            while True:
                  resp = input('Insira a alternativa: ').strip().upper()
                  if resp == 'A':
                        if A == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                  elif resp == 'B':
                        if B == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                  elif resp == 'C':
                        if C == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                  elif resp == 'D':
                        if D == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                  elif resp == 'E':
                        if E == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                  elif resp == '9':
                        while True:
                              if ajudas > 0:
                                    print('Ajudas:\n'
                                          '1-Dica\n'
                                          '2-Pular questão\n'
                                          '3-Eliminar alternativas\n'
                                          '4-Voltar')
                                    while True:
                                          try:
                                                ajd = int(input('Insira sua escolha: '))
                                                break
                                          except:
                                                print('\nDigite uma opção valida.\n')
                                    if ajd == 1:
                                          dica = ''.join(Qatual['hint'])
                                          text_quebrado = textwrap.fill(dica, width=caracteres)
                                          print('\nDica: ')
                                          print(text_quebrado)
                                          print()
                                          ajudas -= 1
                                          break
                                    elif ajd == 2:
                                          ajudas -= 1
                                          break
                                    elif ajd == 3:
                                          os.system('cls')
                                          alternativas = [Qatual['option1'],Qatual['option2'],Qatual['option3'],Qatual['option4'],Qatual['option5']]
                                          t_quebrado = textwrap.fill(Qatual['questionText'], width=caracteres)
                                          print(f'{t_quebrado}\n')
                                          for i in range(3):
                                                alt_random = random.choice(alternativas)
                                                if alt_random != Qatual['answer']:
                                                      alternativas.remove(alt_random)
                                          for i in alternativas:
                                                if i == A:
                                                      print(f'A){i}\n')
                                                elif i == B:
                                                      print(f'B){i}\n')
                                                elif i == C:
                                                      print(f'C){i}\n')
                                                elif i == D:
                                                      print(f'D){i}\n')
                                                elif i == E:
                                                      print(f'E){i}\n')
                                          print('9-Ajuda')
                                          print(f'                                                                PONTOS:{pontos}\n'
                                                f'                                                                AJUDAS:{ajudas}')
                                          ajudas -= 1
                                          break
                                    elif ajd == 4:
                                          break
                                    else:
                                          print('\nDigite uma opção valida.\n')
                             
                              if ajudas == 0:
                                    print('Ajuda indisponivel')
                                    break
                        if ajd == 2:
                              break 
                  else:
                        print('\nDigite uma opção valida.\n')
            if pontos // 60 != aux and ajudas < 3:
                  ajudas +=1
                  aux += 1
            for i in range (5, 0, -1):
                  print(f'\r{i}...', end='')
                  time.sleep(1)
            os.system('cls')
      RankTempo('Hallt.txt', tempo_restante)
      while True:
            try:
                  rsp=int(input('Jogar novamente? 1-Sim | 2-Não: '))
                  if rsp == 1 or rsp ==2:
                        break
                  else:
                        print('Invalido, digite novamente.')
            except:
                  print('Invalido, digite novamente.')
      if rsp == 1:
            questions = regenerar()
            Ltempo(questions)

def Aterrar(questions):
      caracteres = 70
      pontos = 0
      ajudas = 3
      aux = 0
      errado = False
      os.system('cls')
      print('-=-=-=-=-=-=Até Errar-=-=-=-=-=-=\n\n'
            'Neste modo você enfrentará todas as questões do jogo até errar!\n\n'
            'Boa sorte!')
      for i in range (5, 0, -1):
            print(f'\r{i}...', end='')
            time.sleep(1)
      os.system('cls')
      while questions:
            Qatual = random.choice(questions)
            questions.remove(Qatual)
            t_quebrado = textwrap.fill(Qatual['questionText'], width=caracteres)
            print(f'{t_quebrado}\n')
            print(f'A) {Qatual['option1']}\n')
            A = Qatual['option1']
            print(f'B) {Qatual['option2']}\n')
            B = Qatual['option2']
            print(f'C) {Qatual['option3']}\n')
            C = Qatual['option3']
            print(f'D) {Qatual['option4']}\n')
            D = Qatual['option4']
            print(f'E) {Qatual['option5']}\n')
            E = Qatual['option5']
            print('9-Ajuda')
            print(f'                                                                PONTOS:{pontos}\n'
                  f'                                                                AJUDAS:{ajudas}')
            while True:
                  resp = input('Insira a alternativa: ').strip().upper()
                  if resp == 'A':
                        if A == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == 'B':
                        if B == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == 'C':
                        if C == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == 'D':
                        if D == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == 'E':
                        if E == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n')
                              errado = True
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == '9':
                        while True:
                              if ajudas > 0:
                                    print('Ajudas:\n'
                                          '1-Dica\n'
                                          '2-Pular questão\n'
                                          '3-Eliminar alternativas\n'
                                          '4-Voltar')
                                    while True:
                                          try:
                                                ajd = int(input('Insira sua escolha: '))
                                                break
                                          except:
                                                print('\nDigite uma opção valida.\n')
                                    if ajd == 1:
                                          dica = ''.join(Qatual['hint'])
                                          text_quebrado = textwrap.fill(dica, width=caracteres)
                                          print('\nDica: ')
                                          print(text_quebrado)
                                          print()
                                          ajudas -= 1
                                          break
                                    elif ajd == 2:
                                          ajudas -= 1
                                          break
                                    elif ajd == 3:
                                          os.system('cls')
                                          alternativas = [Qatual['option1'],Qatual['option2'],Qatual['option3'],Qatual['option4'],Qatual['option5']]
                                          t_quebrado = textwrap.fill(Qatual['questionText'], width=caracteres)
                                          print(f'{t_quebrado}\n')
                                          for i in range(3):
                                                alt_random = random.choice(alternativas)
                                                if alt_random != Qatual['answer']:
                                                      alternativas.remove(alt_random)
                                          for i in alternativas:
                                                if i == A:
                                                      print(f'A){i}\n')
                                                elif i == B:
                                                      print(f'B){i}\n')
                                                elif i == C:
                                                      print(f'C){i}\n')
                                                elif i == D:
                                                      print(f'D){i}\n')
                                                elif i == E:
                                                      print(f'E){i}\n')
                                          print('9-Ajuda')
                                          print(f'                                                                PONTOS:{pontos}\n'
                                                f'                                                                AJUDAS:{ajudas}')
                                          ajudas -= 1
                                          break
                                    elif ajd == 4:
                                          break
                                    else:
                                          print('\nDigite uma opção valida.\n')
                             
                              if ajudas == 0:
                                    print('Ajuda indisponivel')
                                    break
                        if ajd == 2:
                              break 
                  else:
                        print('\nDigite uma opção valida.\n')
            if pontos // 60 != aux and ajudas < 3:
                  ajudas +=1
                  aux += 1
            for i in range (8, 0, -1):
                  print(f'\r{i}...', end='')
                  time.sleep(0.8)
            if errado == True:
                  break
            os.system('cls')
      atualizar_ranking('Halle.txt', pontos)
      while True:
            try:
                  rsp=int(input('Jogar novamente? 1-Sim | 2-Não: '))
                  if rsp == 1 or rsp ==2:
                        break
                  else:
                        print('Invalido, digite novamente.')
            except:
                  print('Invalido, digite novamente.')
      if rsp == 1:
            questions = regenerar()
            Aterrar(questions)

def lerRank(caminho):
    with open(caminho, "r") as arquivo:
        linhas = arquivo.readlines()
    ranking = []
    for linha in linhas:
        posicao, nome, pontuacao = linha.strip().split(":")
        ranking.append({"posicao": int(posicao), "nome": nome, "pontuacao": int(pontuacao)})
    return ranking

def salvarRank(caminho, ranking):
    with open(caminho, "w") as arquivo:
        for jogador in ranking:
            arquivo.write(f"{jogador['posicao']}: {jogador['nome']}: {jogador['pontuacao']}\n")

def atualizar_ranking(caminho, pontuacao):
    ranking = lerRank(caminho)
    
    menor_pontuacao = min(ranking, key=lambda x: x["pontuacao"])
    if pontuacao > menor_pontuacao["pontuacao"]:
        print(f"Você entrou no ranking! Substituindo {menor_pontuacao['nome']} com {menor_pontuacao['pontuacao']} pontos.")
        
        nome = input("Digite seu nome: ")
        ranking.append({"posicao": 0, "nome": nome, "pontuacao": pontuacao})
        
        
        ranking = sorted(ranking, key=lambda x: x["pontuacao"], reverse=True)
        ranking = ranking[:10]
        for i, jogador in enumerate(ranking, start=1):
            jogador["posicao"] = i
        
        salvarRank(caminho, ranking)
        print("Ranking atualizado com sucesso!")
    else:
        print("Sua pontuação não foi suficiente para entrar no ranking.")

def RankTempo(caminho, tempoSobrando):
    ranking = lerRank(caminho)
    
    maiorTempo = max(ranking, key=lambda x: x["pontuacao"])
    if tempoSobrando < maiorTempo["pontuacao"]:
       print(f"Você entrou no ranking! Substituindo {maiorTempo['nome']} com {maiorTempo['pontuacao']} segundos.")
        
       nome = input("Digite seu nome: ")
       ranking.append({"posicao": 0, "nome": nome, "pontuacao": tempoSobrando})
        
       ranking = sorted(ranking, key=lambda x: x["pontuacao"])
       ranking = ranking[:10]
       for i, jogador in enumerate(ranking, start=1):
            jogador["posicao"] = i
        
       salvarRank(caminho, ranking)
       print("Ranking atualizado com sucesso!")
    else:
        print("Sua pontuação não foi suficiente para entrar no ranking.")

#Programa principal
chaves=['category', 'value', 'questionPath', 'questionText', 'option1', 'option2', 'option3',
 'option4', 'option5', 'answer', 'explanation', 'hint']
with open('Banco_de_Questões.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
for key in chaves:
      conteudo = conteudo.replace(key, f"'{key}'")

questions = eval(conteudo[12:])

if not os.path.exists('Hallf.txt'):
      with open('Hallf.txt', 'w', encoding='utf-8')as file1:
            for i in range(10):
                  file1.write(f'{i+1}: ###: 0\n')
if not os.path.exists('Hallt.txt'):
      with open('Hallt.txt', 'w', encoding='utf-8')as file2:
            for i in range(10):
                  file2.write(f'{i+1}: ###: 999\n')
if not os.path.exists('Halle.txt'):
      with open('Halle.txt', 'w', encoding='utf-8')as file3:
            for i in range(10):
                  file3.write(f'{i+1}: ###: 0\n')
jogo()






            
      














