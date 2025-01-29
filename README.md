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
