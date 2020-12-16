total = 0
for i in range(7):
    dailyTemp = float(input("What is the temperature like today?\n : "))
    total += dailyTemp
    if i < 6:
        print("Noted, please come back tomorrow.\n\n")

average = total / 7
print(f"The average temperature this week was {average} degrees")
