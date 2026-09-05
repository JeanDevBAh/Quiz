#   /*******************************************************************************
#   Autor: Jean Carlos Lima Mascarenhas
#   Componente Curricular: MI Algoritmos 
#   Concluido em: 03/12/2024
#   Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#   trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#   apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#   de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#   do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#   ******************************************************************************************/

#Bibliotecas(Todas padrão do python):
import os
import random
import time
import textwrap#Essa biblioteca vai servir para facilitar a quebra de linha dos textos.

os.system('cls')#Limpa o terminal.

def jogo(): #Menu principal do jogo.
      while True:
            os.system('cls')
            print('-=-=-=-=AskMe-=-=-=-=\n')
            print('Selecione o modo:\n\n' #Informações do menu.
                  '1-Questões Fixas\n\n'
                  '2-Limite de Tempo\n\n'
                  '3-Tente não errar\n\n'
                  '4-Hall da fama\n\n'
                  '0-Exit\n')
            time.sleep(0.5)
            while True: #loop vai se repetir até o usuario dar um dos comandos de modo correto.
                  try:
                        seleção = int(input('Digite o número do modo: '))
                        break
                  except:
                        print('Invalido, tente novamente!')
                        time.sleep(2)
            if seleção == 1:#Modo de jogo 1
                  fixas(questions)
            elif seleção == 2:#Modo de jogo 2
                  Ltempo(questions, 306)
            elif seleção == 3: #Modo de jogo 3
                  Aterrar(questions)
            elif seleção == 0: #Encerrar o jogo
                  os.system('cls')
                  print('-=-=-=PROGRAMA ENCERRADO-=-=-=-')
                  break
            elif seleção == 4: #Hall da fama
                  hall_da_fama()
            else: #Solicitação de uma nova digitação em caso de erro.
                  print('Invalido, tente novamente!')
                  time.sleep(2)

def hall_da_fama(): #Menu para o acesso aos halls de cada modo de jogo.
      while True:
            os.system('cls')
            print('-=-=-=-=-=HALL DA FAMA=-=-=-=-=-\n\n'
                  '1-Fixas\n\n'
                  '2-Tempo\n\n' #Informações do menu
                  '3-Até errar\n\n'
                  '4-voltar\n')
            while True:
                  try:
                        n = int(input('Selecione o hall: '))
                        break
                  except:
                        print('Invalido, tente novamente.')
                        time.sleep(2)
            if n == 1: #Hall das Fixas
                  with open('Hallf.txt', 'r', encoding='utf-8')as file1:
                        c1 = file1.read() #Leitura e impressão do arquivo
                  print(f'\n{c1}')
                  for i in range (8, 0, -1): #Cronometro simulado com time sleep.
                        print(f'\r{i}...', end='')
                        time.sleep(1)
            elif n == 2: #Hall de Tempo
                  print('Pontuação equivalente ao tempo em segundos que cada jogador fez o modo\n')
                  with open('Hallt.txt', 'r', encoding='utf-8')as file2:
                        c2 = file2.read()
                  print(f'\n{c2}')
                  for i in range (8, 0, -1):
                        print(f'\r{i}...', end='')
                        time.sleep(1)
            elif n == 3: #Hall do Até Errar
                  with open('Halle.txt', 'r', encoding='utf-8')as file3:
                        c3 = file3.read()
                  print(f'\n{c3}')
                  for i in range (8, 0, -1):
                        print(f'\r{i}...', end='')
                        time.sleep(1)
            elif n == 4: #Volta para o menu Principal
                  break
            else: #Solicitação de uma nova digitação em caso de erro.
                  print('Invalido, tente novamente.')
                  time.sleep(2)

def fixas(questions): #Modo de jogo das fixas recebe a lista de questões como parametro.
      caracteres = 70
      pontos = 0  #Definições iniciais.
      ajudas = 3
      aux = 0
      os.system('cls')
      print('-=-=-=-=-=-=Questões fixas-=-=-=-=-=-=\n\n'
            'Neste modo você enfrentará 15 questões\n\n'
            'Acerte quantas puder para maiores pontuações!')
      for i in range (5, 0, -1): #Cronometro improvisado
            print(f'\r{i}...', end='')
            time.sleep(1) # Limpa o terminal
      os.system('cls')
      fix = 15 #numero de questões
      for i in range(fix): #loop do jogo.
            Qatual = random.choice(questions) #seleciona uma questão aleatoria.
            questions.remove(Qatual) #Remove a qeustão da lista para evitar repetição.
            t_quebrado = textwrap.fill(Qatual['questionText'], width=caracteres) #uso da biblioteca para quebrar a linha após o n de caracteres definido.
            print(f'{t_quebrado}\n')
            print(f'A) {Qatual['option1']}\n')  #Print da questão, dos pontos, das ajudas e atribuição das alternativas
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
            while True: #loop de verificação da resposta.
                  resp = input('Insira a alternativa: ').strip().upper()
                  if resp == 'A':
                        if A == Qatual['answer']: #Caso for certa
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres) #Explicação da questão.
                              print(texto_quebrado)
                              pontos += int(Qatual['value']) #Pontuação adicionada
                              break
                        else: #Caso for errado
                              print('\nErrado\n')
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
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              break
                  elif resp == '9': #Menu das ajudas.
                        while True:
                              if ajudas > 0: #Caso tenha ajuda disponivel.
                                    print('Ajudas:\n'
                                          '1-Dica\n' #Info do menu
                                          '2-Pular questão\n'
                                          '3-Eliminar alternativas\n'
                                          '4-Voltar')
                                    while True: #Entrada do usuario.
                                          try:
                                                ajd = int(input('Insira sua escolha: '))
                                                break
                                          except:
                                                print('\nDigite uma opção valida.\n')
                                    if ajd == 1: #Dicas
                                          dica = ''.join(Qatual['hint'])
                                          text_quebrado = textwrap.fill(dica, width=caracteres)
                                          print('\nDica: ')
                                          print(text_quebrado)
                                          print()
                                          ajudas -= 1 #Reduz as ajudas disponiveis.
                                          break
                                    elif ajd == 2: #Pula a questão quebrando o loop dela.
                                          ajudas -= 1
                                          break
                                    elif ajd == 3: #Sorteia alternativas erradas e elimina elas.
                                          os.system('cls')
                                          alternativas = [Qatual['option1'],Qatual['option2'],Qatual['option3'],Qatual['option4'],Qatual['option5']]
                                          t_quebrado = textwrap.fill(Qatual['questionText'], width=caracteres)
                                          print(f'{t_quebrado}\n')
                                          for i in range(3): #No maximo 3 erradas são eliminadas.
                                                alt_random = random.choice(alternativas)
                                                if alt_random != Qatual['answer']:
                                                      alternativas.remove(alt_random)
                                          for i in alternativas: #Printa a questão novamente sem as alternativas retiradas.
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
                                    elif ajd == 4: #Sai do menu de ajudas.
                                          break
                                    else:
                                          print('\nDigite uma opção valida.\n')
                             
                              if ajudas == 0: #Sem ajudas nada ocorre.
                                    print('Ajuda indisponivel')
                                    break
                        if ajd == 2: #Pula a questão quebrando o loop dela.
                              break 
                  else: #Redigitação em caso de erro.
                        print('\nDigite uma opção valida.\n')
            if pontos // 60 != aux and ajudas < 3: #Administração das ajudas que podem ser no maximo 3.
                  ajudas +=1
                  aux += 1
            for i in range (8, 0, -1): #Cronometro improvisado.
                  print(f'\r{i}...', end='')
                  time.sleep(1)
            os.system('cls')
      atualizar_ranking('Hallf.txt', pontos) #Ao fim do jogo é chamada essa função para verificar se o jogador entrará no rank, e atualiza-lo em caso de entrar.
      while True: #Entrada do usuario sobre querer reiniciar o modo de jogo.
            try:
                  rsp=int(input('Jogar novamente? 1-Sim | 2-Não: '))
                  if rsp == 1 or rsp == 2:
                        break
                  else:
                        print('Invalido, digite novamente.')
            except:
                  print('Invalido, digite novamente.')
      if rsp == 1:
            questions = regenerar() #restaura o banco de questões
            fixas(questions) #Roda a função novamente

def regenerar(): #Repetição do processo do programa principal para restaurar o banco de questões ao iniciar o jogo novamente.
      chaves=['category', 'value', 'questionPath', 'questionText', 'option1', 'option2', 'option3',
      'option4', 'option5', 'answer', 'explanation', 'hint']
      with open('Banco_de_Questões', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
      for key in chaves:
            conteudo = conteudo.replace(key, f"'{key}'")

      questions = eval(conteudo[12:])
      return questions #Retorna uma lista de questões nova.

def Ltempo(questions,tempo_limite): #Modo de jogo de tempo recebe a lista de questões e o tempo como parametro.
      caracteres = 70
      pontos = 0
      ajudas = 3 #Definições iniciais
      aux = 0
      start_time = time.time() #Tempo inicial  
      end_time = start_time + tempo_limite #tempo limite
      os.system('cls')
      print('-=-=-=-=-=-=Limite de Tempo-=-=-=-=-=-=\n\n'
            'Neste modo você enfrentará 15 questões com 5 minutos de limite de tempo!\n\n'
            'Acerte no melhor tempo para maiores pontuações!')
      for i in range (5, 0, -1):
            print(f'\r{i}...', end='')
            time.sleep(1)
      os.system('cls')
      fixas = 15 #numero de questões
      for i in range(fixas):#loop do jogo.  
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
            if time.time() > end_time: #Se o tempo esgotar o jogo encerra.
                  print("\nTempo esgotado! Fim do jogo.")
                  time.sleep(2)
                  break
            tempo_restante = int(end_time - time.time()) #Tempo restante será utilizado para informar ao usuario e sera parametro de sua possivel posição no rank.
            print(f"\nTempo restante: {tempo_restante} segundos")

            while True: # A partir daqui é a mesma logica aplicada no primeiro modo, tirando o fato de que a questão não passa para a proxima se o jogador errar.
                  resp = input('Insira a alternativa: ').strip().upper()
                  if resp == 'A':
                        if A == Qatual['answer']:
                              print('\nResposta Correta!\n')
                              texto_quebrado = textwrap.fill(Qatual['explanation'], width=caracteres)
                              print(texto_quebrado)
                              pontos += int(Qatual['value'])
                              break
                        else:
                              print('\nErrado\n') #Ao errar só uma mensagem será dada o jogador deve tentar até acertar a questão.
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
      RankTempo('Hallt.txt', 300-tempo_restante) #O hall da fama deste modo usa de uma logica contraria aos outros.
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

def Aterrar(questions): #Modo de jogo Até Errar recebe a lista de questões como parametro.
      caracteres = 70
      pontos = 0
      ajudas = 3 #Definições iniciais.
      aux = 0
      errado = False #Variavel auxiliar para encerrar o jogo em caso de erro.
      os.system('cls')
      print('-=-=-=-=-=-=Até Errar-=-=-=-=-=-=\n\n'
            'Neste modo você enfrentará todas as questões do jogo até errar!\n\n'
            'Boa sorte!')
      for i in range (5, 0, -1):
            print(f'\r{i}...', end='')
            time.sleep(1)
      os.system('cls')
      while questions: #loop do jogo é feito de forma que o jogo rode até acabarem todas as questões da lista.
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
            while True: #Mesma logica aplicada nos outros modos, tirando o fato do jogo encerrar em caso de erro.
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
                              errado = True #Variavel de erro alterada
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
                              errado = True #Variavel de erro alterada
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
                              errado = True #Variavel de erro alterada
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
                              errado = True #Variavel de erro alterada
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
                              errado = True #Variavel de erro alterada
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
            if errado == True: #Caso o jogador errar o modo se encerra.
                  break
            os.system('cls')
      atualizar_ranking('Halle.txt', pontos) #Hall da fama é atualizado se o jogador pontuar o suficiente.
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

def lerRank(caminho): #Função para ler o rank e fazer uma lista de dicionarios com as informações atuais dele.
    with open(caminho, "r") as arquivo:
        linhas = arquivo.readlines()
    ranking = []
    for linha in linhas:
        posicao, nome, pontuacao = linha.strip().split(':')
        ranking.append({"posicao": int(posicao), "nome": nome, "pontuacao": int(pontuacao)})
    return ranking

def salvarRank(caminho, ranking): #Função para salvar as alterações feitas no rank.
    with open(caminho, "w") as arquivo:
        for jogador in ranking:
            arquivo.write(f"{jogador['posicao']}: {jogador['nome']}: {jogador['pontuacao']}\n")

def atualizar_ranking(caminho, pontuacao): #Função que organiza os ranks.
    ranking = lerRank(caminho) #Leitura do rank.
    
    menor_pontuacao = min(ranking, key=lambda x: x["pontuacao"]) #identificação de quem vai sair.
    if pontuacao > menor_pontuacao["pontuacao"]:
        print(f"Você entrou no ranking! Substituindo {menor_pontuacao['nome']} com {menor_pontuacao['pontuacao']} pontos.")
        
        nome = input("Digite seu nome: ")
        ranking.append({"posicao": 0, "nome": nome, "pontuacao": pontuacao}) #As informações do novo jogador são coletadas.
        
        
        ranking = sorted(ranking, key=lambda x: x["pontuacao"], reverse=True) #Rank é feito de forma decrescente
        ranking = ranking[:10] #Os 10 primeiros permanecem 
        for i, jogador in enumerate(ranking, start=1):
            jogador["posicao"] = i #Ordenação das posições
        
        salvarRank(caminho, ranking) #Rank atualizado.
        print("Ranking atualizado com sucesso!")
    else:
        print("Sua pontuação não foi suficiente para entrar no ranking.")

def RankTempo(caminho, tempoSobrando): #Função que organiza o Rank do modo de tempo em especifico.
    ranking = lerRank(caminho)
    
    maiorTempo = max(ranking, key=lambda x: x["pontuacao"]) #identificação de quem vai sair.
    if tempoSobrando < maiorTempo["pontuacao"]:
       print(f"Você entrou no ranking! Substituindo {maiorTempo['nome']} com {maiorTempo['pontuacao']} segundos.")
        
       nome = input("Digite seu nome: ")
       ranking.append({"posicao": 0, "nome": nome, "pontuacao": tempoSobrando}) #As informações do novo jogador são coletadas.
        
       ranking = sorted(ranking, key=lambda x: x["pontuacao"]) #Rank é feito de forma crescente
       ranking = ranking[:10] #Os 10 primeiros permanecem 
       for i, jogador in enumerate(ranking, start=1):
            jogador["posicao"] = i #Ordenação das posições
        
       salvarRank(caminho, ranking) #Rank atualizado.
       print("Ranking atualizado com sucesso!")
    else:
        print("Sua pontuação não foi suficiente para entrar no ranking.")



#Programa principal
chaves=['category', 'value', 'questionPath', 'questionText', 'option1', 'option2', 'option3',
 'option4', 'option5', 'answer', 'explanation', 'hint']
with open('Banco_de_Questões.txt', 'r', encoding='utf-8') as arquivo: #Chamada do arquivo 
    conteudo = arquivo.read()
for key in chaves: #Subisituição das chaves no arquivo por chaves com aspas para serem reconhecidas quando trazidas para o programa.
      conteudo = conteudo.replace(key, f"'{key}'")

questions = eval(conteudo[12:]) #Transformação do arquivo de str para uma lista.

#Verificação para ver se o hall da fama existe, caso de não existir, ele é escrito em um modelo padronizado.
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

#Função para o menu do jogo.                 
jogo()






            
      














