import gym
from gym import spaces
import numpy as np 

class TicTacToeEnv(gym.Env):
    def __init__(self):
        super(TicTacToeEnv, self).__init__()
        
        
        self.action_space = spaces.Discrete(9)
        

        self.observation_space = spaces.Box(low=-1, high=1, shape=(9,), dtype=np.int32)
        
        
        self.reset()
    
    def reset(self):
        
        self.board = np.zeros(9, dtype=np.int32)
        self.current_player = 1 
        self.done = False
        return self.board.copy()
    
    def step(self, action):
        
        if self.done:
            raise ValueError("Jogo já terminou. Reinicie o ambiente.")
         
        
        self.board[action] = self.current_player
        
       
        winner = self.check_winner()
        if winner != 0:
            self.done = True
            reward = 1 if winner == self.current_player else -1
        elif 0 not in self.board: 
            self.done = True
            reward = 0
        else:
            reward = 0
            self.current_player *= -1 
        
        return self.board.copy(), reward, self.done, {}
    
    def render(self, mode='human'):
        board_symbols = self.board.reshape(3, 3)
        symbols = {1: 'X', -1: 'O', 0: '.'}
        rendered_board = '\n'.join(' '.join(symbols[cell] for cell in row) for row in board_symbols)
        print(rendered_board)
        print()
    
    def check_winner(self):
        board = self.board.reshape(3, 3)
        
        for i in range(3):
            if abs(board[i, :].sum()) == 3:
                return board[i, 0]
            if abs(board[:, i].sum()) == 3:
                return board[0, i]
        if abs(board.trace()) == 3:
            return board[0, 0]
        if abs(np.fliplr(board).trace()) == 3:
            return board[0, 2]
        return 0

    def computer_move(self):
       
        valid_actions = [i for i in range(9) if self.board[i] == 0]
        action = np.random.choice(valid_actions)
        return action


if __name__ == "__main__":
    env = TicTacToeEnv()
    obs = env.reset()
    
    print("Iniciando simulação de Jogo da Velha com dois computadores.")
    print("Tabuleiro inicial:")
    env.render()
    
    while True:
        action = env.computer_move()  
        print(f"Jogador {'X' if env.current_player == 1 else 'O'} escolheu a posição {action}.")
        
        obs, reward, done, _ = env.step(action)
        env.render()
        
        if done:
            if reward == 1:
                print(f"Jogador {'X' if env.current_player == 1 else 'O'} venceu!")
            elif reward == 0:
                print("O jogo terminou em empate!")
            break
