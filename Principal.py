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
                  for i in range (5, 0, -1):
                        print(f'\r{i}...', end='')
                        time.sleep(1)
            elif n == 2:
                  with open('Hallt.txt', 'r', encoding='utf-8')as file2:
                        c2 = file2.read()
                  print(f'\n{c2}')
                  for i in range (5, 0, -1):
                        print(f'\r{i}...', end='')
                        time.sleep(1)
            elif n == 3:
                  with open('Halle.txt', 'r', encoding='utf-8')as file3:
                        c3 = file3.read()
                  print(f'\n{c3}')
                  for i in range (5, 0, -1):
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
      fix = 2
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
      with open('Hallt.txt', 'r',encoding='utf-8') as file:
            cont = file.readlines()
      rank = []
      for l in cont:
            posicao, nome, pontuacao = l.strip().split(":")
            rank.append({"posicao": posicao, "nome": nome, "pontuacao": int(pontuacao)})
      rank1 = rank[0]
      rank2 = rank[1]
      rank3 = rank[2]   
      if pontos > rank1['pontuacao'] and rank1['pontuacao'] == 0:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank1['pontuacao'] = pontos
            rank1['nome'] = input('Digite seu nome: ') 
      elif pontos > rank1['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank1['pontuacao'], rank2['pontuacao'], rank3['pontuacao'] = pontos , rank1['pontuacao'], rank2['pontuacao']
            rank1['nome'], rank2['nome'], rank3['nome'] = input('Digite seu nome: ') , rank1['nome'], rank2['nome']
      elif pontos > rank2['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank2['pontuacao'], rank3['pontuacao'] = pontos , rank2['pontuacao']
            rank2['nome'], rank3['nome'] = input('Digite seu nome: ') , rank2['nome']
      elif pontos > rank3['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank3['pontuacao'] = pontos
            rank3['nome'] = input('Digite seu nome: ') 
      with open('Hallf.txt', 'w',encoding='utf-8') as file:
            for p in rank:
                  file.write(f'{p['posicao']}: {p['nome']}: {p['pontuacao']} pontos\n')
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
      with open('questões.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
      for key in chaves:
            conteudo = conteudo.replace(key, f"'{key}'")

      questions = eval(conteudo.split('=')[1])
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
      with open('Halle.txt', 'r',encoding='utf-8') as file:
            cont = file.readlines()
      rank = []
      for l in cont:
            posicao, nome, pontuacao = l.strip().split(":")
            rank.append({"posicao": posicao, "nome": nome, "pontuacao": int(pontuacao)})
      rank1 = rank[0]
      rank2 = rank[1]
      rank3 = rank[2]   
      rank1['pontuacao'] = 999999999999
      rank2['pontuacao'] = 999999999999
      rank3['pontuacao'] = 999999999999
      if tempo_restante < rank1['pontuacao'] and rank1['pontuacao'] == 999999999999:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank1['pontuacao'] = tempo_restante
            rank1['nome'] = input('Digite seu nome: ') 
      elif tempo_restante < rank1['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank1['pontuacao'], rank2['pontuacao'], rank3['pontuacao'] = tempo_restante , rank1['pontuacao'], rank2['pontuacao']
            rank1['nome'], rank2['nome'], rank3['nome'] = input('Digite seu nome: ') , rank1['nome'], rank2['nome']
      elif tempo_restante < rank2['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank2['pontuacao'], rank3['pontuacao'] = tempo_restante , rank2['pontuacao']
            rank2['nome'], rank3['nome'] = input('Digite seu nome: ') , rank2['nome']
      elif tempo_restante < rank3['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank3['pontuacao'] = tempo_restante
            rank3['nome'] = input('Digite seu nome: ') 
      with open('Halle.txt', 'w',encoding='utf-8') as file:
            for p in rank:
                  if p['pontuacao'] == 999999999999:
                        p['pontuacao'] == 0
                  file.write(f'{p['posicao']}: {p['nome']}: {p['pontuacao']}s\n')
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
      fixas = 15
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
      with open('Halle.txt', 'r',encoding='utf-8') as file:
            cont = file.readlines()
      rank = []
      for l in cont:
            posicao, nome, pontuacao = l.strip().split(":")
            rank.append({"posicao": posicao, "nome": nome, "pontuacao": int(pontuacao)})
      rank1 = rank[0]
      rank2 = rank[1]
      rank3 = rank[2]   
      if pontos > rank1['pontuacao'] and rank1['pontuacao'] == 0:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank1['pontuacao'] = pontos
            rank1['nome'] = input('Digite seu nome: ') 
      elif pontos > rank1['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank1['pontuacao'], rank2['pontuacao'], rank3['pontuacao'] = pontos , rank1['pontuacao'], rank2['pontuacao']
            rank1['nome'], rank2['nome'], rank3['nome'] = input('Digite seu nome: ') , rank1['nome'], rank2['nome']
      elif pontos > rank2['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank2['pontuacao'], rank3['pontuacao'] = pontos , rank2['pontuacao']
            rank2['nome'], rank3['nome'] = input('Digite seu nome: ') , rank2['nome']
      elif pontos > rank3['pontuacao']:
            print('Parabens você entrou para o hall da fama!\n\n')
            rank3['pontuacao'] = pontos
            rank3['nome'] = input('Digite seu nome: ') 
      with open('Halle.txt', 'w',encoding='utf-8') as file:
            for p in rank:
                  file.write(f'{p['posicao']}: {p['nome']}: {p['pontuacao']} pontos\n')
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

#Programa principal
chaves=['category', 'value', 'questionPath', 'questionText', 'option1', 'option2', 'option3',
 'option4', 'option5', 'answer', 'explanation', 'hint']
with open('questões.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
for key in chaves:
      conteudo = conteudo.replace(key, f"'{key}'")

questions = eval(conteudo.split('=')[1])

if not os.path.exists('Hallf.txt'):
      with open('Hallf.txt', 'w', encoding='utf-8')as file1:
            for i in range(3):
                  file1.write(f'{i+1}º: ###: 0\n')
if not os.path.exists('Hallt.txt'):
      with open('Hallt.txt', 'w', encoding='utf-8')as file2:
            for i in range(3):
                  file2.write(f'{i+1}º: ###: 0\n')
if not os.path.exists('Halle.txt'):
      with open('Halle.txt', 'w', encoding='utf-8')as file3:
            for i in range(3):
                  file3.write(f'{i+1}º: ###: 0\n')
jogo()






            
      














