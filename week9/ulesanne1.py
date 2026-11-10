with open("data/todo.txt", "r", encoding="utf-8") as f:
    tasks = f.readlines()

for task in tasks:
    print(task.strip())