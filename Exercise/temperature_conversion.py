# chuyen doi nhiet do Celsius(C) va Fahrenheit(F)
# cho user nhap gia tri va chon type nhiet do

choice = input("Ban muon nhap nhiet do theo kieu nao? Celsius or Fahrenheit: ").lower()

if choice == 'celsius':
    c = float(input("Nhap gia tri cua Celsius: "))
    f = (c * 9) / 5 + 32
    print(f"Nhiet do {c}°C = {f}°F")
elif choice == 'fahrenheit':
    f = float(input("Nhap gia tri cua Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"Nhiet do {f}°F = {c}°C")
else:
    print("Invalid choice")