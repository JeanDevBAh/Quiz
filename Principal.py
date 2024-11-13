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
      os.system('cls')
      print('-=-=-=-=-=-=Questões fixas-=-=-=-=-=-=\n\n'
            'Neste modo você enfrentará um número fixo de questões(atualmente 6)\n\n'
            'Acerte quantas puder para maiores pontuações!')
      for i in range (8, 0, -1):
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
            print(f'                                                                PONTOS:{pontos}\n')
            while True:
                  resp = input('Digite a alternativa correta: ').strip().upper()
                  if resp == 'A':
                        if A == Qatual['answer']:
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
                  else:
                        print('\nDigite uma opção valida.\n')
            
            for i in range (10, 0, -1):
                  print(f'\r{i}...', end='')
                  time.sleep(1)
            os.system('cls')







#Programa principal
chaves=['category', 'value', 'questionPath', 'questionText', 'option1', 'option2', 'option3', 'option4', 'option5', 'answer', 'explanation', 'hint']
with open('questões.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
for key in chaves:
      conteudo = conteudo.replace(key, f"'{key}'")

questions = eval(conteudo.split('=')[1])

jogo()






            
      














