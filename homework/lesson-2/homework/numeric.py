a=56.455557454534454
a=round(a,2)
print(a)
num1 = float(input("Birinchi raqamni kiriting: "))
num2 = float(input("Ikkinchi raqamni kiriting: "))
num3 = float(input("Uchinchi raqamni kiriting: "))

eng_katta = max(num1, num2, num3)
eng_kichik = min(num1, num2, num3)

print(f"Eng katta raqam: {eng_katta}")
print(f"Eng kichik raqam: {eng_kichik}")
kilometr = float(input("Kilometrni kiriting: "))

metr = kilometr*1000
santimetr = metr * 100

print(f"{kilometr} km = {metr} m")
print(f"{kilometr} km = {santimetr} cm")
num1 = int(input("Birinchi raqamni kiriting: "))
num2 = int(input("Ikkinchi raqamni kiriting: "))

butun_bolish = num1 // num2
qoldiq = num1 % num2

print(f"Butun bo‘lish natijasi: {butun_bolish}")
print(f"Qoldiq: {qoldiq}")
selsiy = float(input("Selsiy haroratini kiriting: "))

farenxeyt = (selsiy * 9/5) + 32

print(f"{selsiy}°C = {farenxeyt}°F")
raqam = int(input("Raqamni kiriting: "))

oxirgi_raqam = raqam % 10

print(f"Oxirgi raqam: {oxirgi_raqam}")
raqam1 = int(input("Birinchi raqamni kiriting: "))
raqam2 = int(input("Ikkinchi raqamni kiriting: "))

if raqam1 == raqam2:
    print("Raqamlar teng.")
else:
    print("Raqamlar teng emas.")
