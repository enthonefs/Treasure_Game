# TicTacToeEnv

Este projeto implementa um ambiente de Jogo da Velha (Tic-Tac-Toe) utilizando o `gym` do OpenAI. É uma simulação onde dois computadores jogam um contra o outro.

## Estrutura do Código

- `TicTacToeEnv`: Classe principal que herda de `gym.Env` e define o ambiente do Jogo da Velha.
  - `__init__()`: Inicializa o ambiente, espaços de ação e observação.
  - `reset()`: Reinicia o jogo.
  - `step(action)`: Executa uma ação no ambiente e retorna o novo estado, a recompensa, se o jogo terminou, e informações adicionais.
  - `render(mode='human')`: Renderiza o tabuleiro do jogo.
  - `check_winner()`: Verifica se há um vencedor no jogo.
  - `computer_move()`: Calcula um movimento válido para o computador.

## Funcionalidades

- **Create**: Reinicia o jogo com o método `reset()`.
- **Read**: Exibe o estado atual do tabuleiro com o método `render()`.
- **Update**: Executa uma ação com o método `step(action)`.
- **Delete**: Reseta o tabuleiro com o método `reset()`.

## Como Utilizar

1. Inicialize o ambiente:
   ```python
   env = TicTacToeEnv()
   obs = env.reset()
Simule um jogo entre dois computadores:

python
while True:
    action = env.computer_move()
    obs, reward, done, _ = env.step(action)
    env.render()
    if done:
        if reward == 1:
            print(f"Jogador {'X' if env.current_player == 1 else 'O'} venceu!")
        elif reward == 0:
            print("O jogo terminou em empate!")
        break
Exemplo de Execução
Ao executar o código, você verá uma simulação de um jogo entre dois computadores, com a seguinte saída:

Iniciando simulação de Jogo da Velha com dois computadores.
Tabuleiro inicial:
. . .
. . .
. . .

Jogador X escolheu a posição 0.
X . .
. . .
. . .
...
Dependências
gym

numpy

Para instalar as dependências, execute:

bash
pip install gym numpy
Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
