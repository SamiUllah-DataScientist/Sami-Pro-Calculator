# =======================================================
# 🧮 PROJECT: SAMI PRO CALCULATOR (Day 6 Ultimate)
# =======================================================

print("=========================================")
print("   🌟 WELCOME TO SAMI PRO CALCULATOR 🌟   ")
print("=========================================")
print("               📌 MENU 📌                ")
print("  [ + ] Addition      [ - ] Subtraction  ")
print("  [ * ] Multi         [ / ] Division     ")
print("  [ % ] Modulus       [ **] Power        ")
print("  [// ] Floor Division (The Pro Twist! 🔥)")
print("=========================================")

# Short Variable Names
n1 = float(input("Enter First Number: "))
op = input("Enter Operator (+, -, *, /, %, **, //): ")
n2 = float(input("Enter Second Number: "))

print("=========================================")

# Operations Logic with Pro Emojis ⚡
if op == "+":
    print(f"➕ Addition: {n1} + {n2} = {n1 + n2} 🎉")

elif op == "-":
    print(f"➖ Subtraction: {n1} - {n2} = {n1 - n2} ✨")

elif op == "*":
    print(f"✖️ Multiplication: {n1} * {n2} = {n1 * n2} 🔥")

elif op == "/":
    if n2 == 0:
        print("❌ Error: Zero (0) se divide nahi ho sakta yara! 😮")
    else:
        print(f"➗ Division: {n1} / {n2} = {n1 / n2} 🎯")

elif op == "%":
    print(f"🛡️ Remainder (Modulus): {n1} % {n2} = {n1 % n2} 💎")

elif op == "**":
    print(f"🚀 Power (Exponent): {n1} raised to {n2} = {n1 ** n2} 💥")

elif op == "//":
    if n2 == 0:
        print("❌ Error: Zero (0) se floor division nahi ho sakti yara! 😮")
    else:
        print(f"⚖️ Floor Division: {n1} // {n2} = {n1 // n2} 📈")

else:
    print("⚠️ Invalid Operator! Sahi operator dalo yara (+, -, *, /, %, **, //)")

print("=========================================")\

