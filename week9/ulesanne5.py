with open("data/todo.txt", "r", encoding="utf-8") as f:
    tasks = [line.strip() for line in f.readlines()]

tasks.sort(key=str.lower)

with open("data/todo_sorted.txt", "w", encoding="utf-8") as f:
    for number, task in enumerate(tasks, start=1):
        f.write(f"{number}. {task}\n")

print("Andmed salvestati faili data/todo_sorted.txt.")