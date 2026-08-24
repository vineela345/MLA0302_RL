# 26) Develop a recommendation system for a streaming service to suggest movies based on user feedback, implemented as an MDP and trained using a Deep Deterministic Policy Gradient (DDPG) algorithm.

import random

n_movies = int(input("Enter number of movies: "))
user_rating = float(input("Enter user's rating (1-5): "))

preferences = [
    random.uniform(0, 1)
    for _ in range(n_movies)
]

recommended_movie = preferences.index(
    max(preferences)
)

reward = user_rating / 5

policy_update = reward * 0.1

preferences[recommended_movie] += policy_update

print("\n--- OUTPUT ---")
print(
    "Movie preferences:",
    [round(x, 2) for x in preferences]
)
print("Recommended movie:", recommended_movie + 1)
print("User rating:", user_rating)
print("Reward:", round(reward, 2))
print("Policy update:", round(policy_update, 3))
