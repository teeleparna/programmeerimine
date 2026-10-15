parool = "python123"

sisestus = input("Sisesta parool: ")

while sisestus != parool:
    print("Vale parool!")
    sisestus = input("Proovi uuesti: ")

print("Õige parool! Sisselogimine õnnestus.")