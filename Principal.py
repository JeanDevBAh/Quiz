import os
import random
import time
import textwrap
os.system('cls')

def jogo():
      while True:
            os.system('cls')
            print('-=-=-=-=AskMe-=-=-=-=\n')
            print('Selecione o modo de jogo:\n\n'
                  '1-Questões Fixas\n\n'
                  '2-Limite de Tempo\n\n'
                  '3-Tente não errar\n\n'
                  '0-Fechar o jogo\n')
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
            else:
                  print('Invalido, tente novamente!')
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
            for i in range (10, 0, -1):
                  print(f'\r{i}...', end='')
                  time.sleep(1)
            os.system('cls')

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
            for i in range (10, 0, -1):
                  print(f'\r{i}...', end='')
                  time.sleep(1)
            if errado == True:
                  break
            os.system('cls')




#Programa principal
chaves=['category', 'value', 'questionPath', 'questionText', 'option1', 'option2', 'option3', 'option4', 'option5', 'answer', 'explanation', 'hint']
with open('questões.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
for key in chaves:
      conteudo = conteudo.replace(key, f"'{key}'")

questions = eval(conteudo.split('=')[1])

jogo()






            
      














