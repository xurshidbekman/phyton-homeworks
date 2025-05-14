username = input("Foydalanuvchi nomini kiriting: ")
password = input("Maxfiy so‘zni kiriting: ")

if username and password:
    print("Foydalanuvchi nomi va maxfiy so‘z to‘g‘ri kiritildi.")
else:
    print("Iltimos, foydalanuvchi nomi va maxfiy so‘zni to‘liq kiriting.")
num1 = float(input("Birinchi sonni kiriting: "))
num2 = float(input("Ikkinchi sonni kiriting: "))

if num1 == num2:
    print("Sonlar teng.")
else:
    print("Sonlar teng emas.")
num = int(input("Raqamni kiriting: "))

if num > 0 and num % 2 == 0:
    print("Raqam musbat va juft.")
else:
    print("Raqam musbat emas yoki juft emas.")
num1 = float(input("Birinchi raqamni kiriting: "))
num2 = float(input("Ikkinchi raqamni kiriting: "))
num3 = float(input("Uchinchi raqamni kiriting: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    print("Barcha raqamlar har xil.")
else:
    print("Ba'zi raqamlar bir-biriga teng.")
satr1 = input("Birinchi satrni kiriting: ")
satr2 = input("Ikkinchi satrni kiriting: ")

if len(satr1) == len(satr2):
    print("Satrlar uzunligi bir xil.")
else:
    print("Satrlar uzunligi farq qiladi.")
num = int(input("Raqamni kiriting: "))

if num % 3 == 0 and num % 5 == 0:
    print("Raqam 3 va 5 ga bo‘linadi.")
else:
    print("Raqam 3 va 5 ga bo‘linmaydi.")
num1 = float(input("Birinchi sonni kiriting: "))
num2 = float(input("Ikkinchi sonni kiriting: "))

if num1 + num2 > 50.8:
    print("Yig‘indi 50.8 dan katta.")
else:
    print("Yig‘indi 50.8 dan kichik yoki teng.")
num = int(input("Raqamni kiriting: "))

if 10 <= num <= 20:
    print("Raqam 10 dan 20 gacha.")
else:
    print("Raqam 10 dan 20 gacha emas.")
num = int(input("Raqamni kiriting: "))