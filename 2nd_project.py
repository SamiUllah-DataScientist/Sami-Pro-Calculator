day_no = int(input("💡 Hint: 1 = Monday ... 7 = Sunday\n\nEnter the DAY Number: "))

match day_no:
    case 1:
        print(f"Monday -> Day {day_no} of 7 · Work Mode 💪")
    case 2:
        print(f"Tuesday -> Day {day_no} of 7 · Grind Mode 🔥")
    case 3:
        print(f"Wednesday -> Day {day_no} of 7 · Mid-Week ⚡")
    case 4:
        print(f"Thursday -> Day {day_no} of 7 · Almost There 🎯")
    case 5:
        print(f"Friday -> Day {day_no} of 7 · Blessed Day 🤲")
    case 6:
        print(f"Saturday -> Day {day_no} of 7 · Chill Mode 😎")
    case 7:
        print(f"Monday -> Day {day_no} of 7 · Reset Day 🔄")
    case _:
        print(f"Invalid Number! Sirf 1 se 7 ke darmiyan number likho yara 😅")
