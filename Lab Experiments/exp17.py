import gymnasium as gym
import pandas as pd
import numpy as np
import random

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam


data = pd.read_excel("/Users/vinnu/Documents/Experiment_17_MountainCar_Dataset.xlsx")


env = gym.make("MountainCar-v0")
model = Sequential()

model.add(Input(shape=(2,)))
model.add(Dense(24, activation="relu"))
model.add(Dense(24, activation="relu"))
model.add(Dense(3, activation="linear"))

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss="mse"
)

gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01

episodes = 20

for episode in range(episodes):

    state, info = env.reset()
    state = np.reshape(state, (1, 2))

    total_reward = 0
    done = False

    while not done:

        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(model.predict(state, verbose=0)[0])

        next_state, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated

        next_state = np.reshape(next_state, (1, 2))

        target = reward

        if not done:
            target = reward + gamma * np.max(model.predict(next_state, verbose=0)[0])

        target_f = model.predict(state, verbose=0)
        target_f[0][action] = target

        model.fit(state, target_f, epochs=1, verbose=0)

        state = next_state
        total_reward += reward

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    print("Episode:", episode + 1, "Reward:", total_reward)

env.close()

print("\nTraining Completed Successfully")
