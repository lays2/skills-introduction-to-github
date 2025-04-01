import gym
import numpy as np

# Criar o ambiente
env = gym.make("CartPole-v1")

# Número de episódios para simulação
num_episodes = 10

for episode in range(num_episodes):
    observation = env.reset()  # Reinicia o ambiente
    total_reward = 0
    done = False
    
    while not done:
        env.render()  # Mostra a simulação na tela
        
        # Escolhe uma ação aleatória
        action = env.action_space.sample()
        
        # Executa a ação e coleta as informações retornadas
        observation, reward, done, info = env.step(action)
        total_reward += reward
        
        if done:
            print(f"Fim do Episódio {episode + 1} - Pontuação Total: {total_reward}")
            break

env.close()  # Fecha o ambiente


