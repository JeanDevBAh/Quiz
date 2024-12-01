
chaves=['category', 'value', 'questionPath', 'questionText', 'option1', 'option2', 'option3',
 'option4', 'option5', 'answer', 'explanation', 'hint']
with open('questões.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
for key in chaves:
      conteudo = conteudo.replace(key, f"'{key}'")
questions = eval(conteudo[12:])
print(questions)