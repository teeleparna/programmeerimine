spent = int(input("Kui palju raha sa meie juures kulutasid? "))

if spent >= 5000:
    print("Platinum")
elif spent >= 1000:
    print("Gold")
elif spent >= 500:
    print("Silver")
elif spent >= 100:
    print("Bronze")
else:
    print("Regular customer")