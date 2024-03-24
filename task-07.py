import random
from tabulate import tabulate

def monte_carlo_simulation(num_trials):
    counts = [0] * 13
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        counts[total] += 1
    probabilities = [(count / num_trials) * 100 for count in counts[2:]]
    return probabilities

num_trials = 1000000
probabilities = monte_carlo_simulation(num_trials)

table_data = []
for i, probability in enumerate(probabilities, start=2):
    table_data.append([i, f"{probability:.2f}% ({probability * num_trials // 100}/{num_trials})"])

table_headers = ["Сума", "Імовірність"]
table = tabulate(table_data, headers=table_headers, tablefmt="grid")
print(table)
