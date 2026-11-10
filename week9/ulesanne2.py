new_task = input("Sisesta uus ülesanne: ")

with open("data/todo.txt", "a", encoding="utf-8") as f:
    f.write(new_task.strip() + "\n")

print("Ülesanne lisati faili.")