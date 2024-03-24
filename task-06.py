def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорійність/вартість у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = {}
    total_cost = 0
    total_calories = 0

    for item, properties in sorted_items:
        if total_cost + properties['cost'] <= budget:
            selected_items[item] = properties
            total_cost += properties['cost']
            total_calories += properties['calories']

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            cost = items[list(items.keys())[i - 1]]['cost']
            calories = items[list(items.keys())[i - 1]]['calories']
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    # Відновлення вибраних страв
    selected_items = {}
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items[list(items.keys())[i - 1]] = items[list(items.keys())[i - 1]]
            j -= items[list(items.keys())[i - 1]]['cost']
        i -= 1

    return selected_items, dp[n][budget]

# Задання страв та бюджету
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

# Виклик функцій
greedy_selected_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
dynamic_selected_items, dynamic_total_calories = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print("Вибрані елементи:", greedy_selected_items)
print("Загальна вартість:", greedy_total_cost)
print("Загальна кількість калорій:", greedy_total_calories)

print("\nДинамічне програмування:")
print("Вибрані елементи:", dynamic_selected_items)
print("Загальна кількість калорій:", dynamic_total_calories)
