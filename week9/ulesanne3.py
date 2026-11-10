with open("data/todo.txt", "r", encoding="utf-8") as f:
    tasks = [line.strip() for line in f.readlines()]

tasks.sort(key=str.lower)

for task in tasks:
    print(task)