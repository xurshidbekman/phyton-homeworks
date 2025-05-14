ism = input("Ismingizni kiriting: ")
t_yil = int(input("Tug‘ilgan yilingizni kiriting: "))

yosh = 2025 - t_yil  # Hozirgi yilni hisobga olib
print(f"Salom, {ism}! Siz {yosh} yoshdasiz.")
txt = "LMaasleitbtui"
avtomobil_nomi = "".join(sorted(txt))
print(f"Avtomobil nomi: {avtomobil_nomi}")
matn = input("Matnni kiriting: ")

print(f"Matn uzunligi: {len(matn)}")
print(f"Katta harflar: {matn.upper()}")
print(f"Kichik harflar: {matn.lower()}")
satr = input("Satrni kiriting: ")

if satr == satr[::-1]:
    print("Bu palindrom!")
else:
    print("Bu palindrom emas.")
satr = input("Satrni kiriting: ")
unlilar = "aeiouAEIOU"
undoshlar = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

unli_soni = sum(1 for harf in satr if harf in unlilar)
undosh_soni = sum(1 for harf in satr if harf in undoshlar)

print(f"Unlilar soni: {unli_soni}")
print(f"Undoshlar soni: {undosh_soni}")
satr1 = input("Birinchi satrni kiriting: ")
satr2 = input("Ikkinchi satrni kiriting: ")

if satr2 in satr1:
    print("Ikkinchi satr birinchida mavjud.")
else:
    print("Ikkinchi satr birinchida mavjud emas.")
jumla = input("Jumlani kiriting: ")
eski_soz = input("Almashtiriladigan so‘zni kiriting: ")
yangi_soz = input("Yangi so‘zni kiriting: ")

yangi_jumla = jumla.replace(eski_soz, yangi_soz)
print(f"Natija: {yangi_jumla}")
satr = input("Satrni kiriting: ")

print(f"Birinchi harf: {satr[0]}")
print(f"Oxirgi harf: {satr[-1]}")
satr = input("Satrni kiriting: ")

print(f"Teskari satr: {satr[::-1]}")
jumla = input("Jumlani kiriting: ")

sozlar_soni = len(jumla.split())
print(f"So‘zlar soni: {sozlar_soni}")
satr = input("Satrni kiriting: ")

if any(harf.isdigit() for harf in satr):
    print("Satrda raqamlar mavjud.")
else:
    print("Satrda raqamlar yo‘q.")
sozlar = input("So‘zlarni vergul bilan kiriting: ").split(", ")
belgi = input("Ajratish uchun belgi kiriting: ")