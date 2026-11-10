with open("data/todo.txt", "r", encoding="utf-8") as f:
    tasks = [line.strip() for line in f.readlines()]

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")