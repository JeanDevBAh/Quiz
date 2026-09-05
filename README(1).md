# ❓ AskMe — Jogo de Perguntas e Respostas em Python

Este script em **Python** implementa um jogo de perguntas e respostas (quiz) interativo via terminal, com múltiplos modos de jogo, sistema de ajudas, pontuação e hall da fama persistente em arquivos de texto. O projeto foi desenvolvido como atividade prática para o componente curricular **MI-Algoritmos**.

---

## 👤 Autoria

* **Autor:** Jean Carlos Lima Mascarenhas
* **Componente Curricular:** MI Algoritmos
* **Concluído em:** 03/12/2024

> Trabalho declarado como de elaboração individual, sem uso de trechos de código de terceiros não devidamente citados.

---

## 🚀 Funcionalidades

* **Menu Principal Interativo:** navegação por opções numéricas para escolher o modo de jogo ou consultar o hall da fama.
* **Três Modos de Jogo:**
    * **1 — Questões Fixas:** o jogador enfrenta **15 questões** sorteadas do banco, acumulando pontos a cada acerto.
    * **2 — Limite de Tempo:** o jogador tenta responder o maior número de questões dentro de um **tempo limite** (padrão de 306 segundos), sem avançar de questão até acertar.
    * **3 — Tente não errar (Até Errar):** o jogador enfrenta questões até **errar uma vez**, quando o jogo é encerrado.
* **Sistema de Ajudas (limite de 3 por partida):**
    * **Dica** sobre a questão atual.
    * **Pular questão** sem penalidade de erro.
    * **Eliminar alternativas** erradas, sorteando até 3 opções incorretas para remover da tela.
    * Ajudas extras são recuperadas a cada 60 pontos acumulados, até o limite de 3.
* **Banco de Questões Dinâmico:** as questões são carregadas de um arquivo externo (`Banco_de_Questões.txt`) e convertidas em uma lista de dicionários em tempo de execução.
* **Sistema de Pontuação:** cada questão possui um valor próprio (`value`), somado à pontuação do jogador a cada acerto.
* **Hall da Fama Persistente:** rankings dos 10 melhores jogadores são salvos em arquivos `.txt` separados por modo de jogo (`Hallf.txt`, `Hallt.txt`, `Halle.txt`), criados automaticamente caso não existam.
* **Sistema de Reinício:** ao final de cada partida, o jogador pode escolher jogar novamente, regenerando o banco de questões.

---

## 💻 Pré-requisitos e Dependências

O projeto utiliza **apenas bibliotecas nativas do Python**, não sendo necessária a instalação de pacotes externos:

* `os`
* `random`
* `time`
* `textwrap`

Basta ter o **Python 3** instalado para executar o script.

> ⚠️ **Atenção:** o script utiliza o comando `os.system('cls')` para limpar o terminal, que é específico do **Windows**. Em sistemas Linux/macOS, será necessário substituir por `os.system('clear')` para que a limpeza de tela funcione corretamente.

---

## 📁 Arquivos Necessários

Para o jogo funcionar corretamente, o arquivo abaixo deve estar na mesma pasta do script:

* **`Banco_de_Questões.txt`** — arquivo contendo a lista de questões, com os campos: `category`, `value`, `questionPath`, `questionText`, `option1` a `option5`, `answer`, `explanation` e `hint`.

Os arquivos de ranking (`Hallf.txt`, `Hallt.txt`, `Halle.txt`) são **gerados automaticamente** na primeira execução, caso ainda não existam.

---

## ▶️ Como Executar

Após garantir que o arquivo `Banco_de_Questões.txt` está presente na pasta do projeto, execute:

```bash
python askme.py
```

> Substitua `askme.py` pelo nome real do arquivo do script, caso seja diferente.

---

## 🎮 Como Jogar

1. No menu principal, escolha o modo de jogo digitando o número correspondente (`1`, `2`, `3`) ou consulte o **Hall da Fama** (`4`).
2. A cada questão exibida, digite a letra da alternativa desejada (`A`, `B`, `C`, `D` ou `E`).
3. Digite `9` a qualquer momento para acessar o **menu de ajudas**, caso ainda tenha ajudas disponíveis.
4. Ao final da partida, se sua pontuação for suficiente, você poderá inserir seu nome para entrar no Hall da Fama.
5. Escolha se deseja jogar novamente (`1`) ou encerrar (`2`).
6. No menu principal, digite `0` para sair do programa.

---

## 🏆 Hall da Fama

Cada modo de jogo possui seu próprio ranking, com lógicas de ordenação diferentes:

| Modo | Arquivo | Critério de Ranking |
|------|---------|----------------------|
| Questões Fixas | `Hallf.txt` | Maior pontuação primeiro |
| Limite de Tempo | `Hallt.txt` | Menor tempo restante primeiro |
| Até Errar | `Halle.txt` | Maior pontuação primeiro |

Apenas os **10 melhores** de cada modo permanecem salvos.

---

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como atividade prática do componente curricular **MI-Algoritmos**, com o objetivo de aplicar conceitos de lógica de programação, manipulação de arquivos, estruturas de dados (listas e dicionários), controle de fluxo, tratamento de exceções e organização de menus interativos em Python.

---

## 📜 Licença

Este projeto é de uso educacional e livre para estudo, salvo indicação em contrário do autor.
