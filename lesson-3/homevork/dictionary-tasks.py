# Misol uchun lug'atlar
d = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5}

# Qiymatni olish
kalit = 'b'
print("Qiymat:", d.get(kalit, "Topilmadi"))

# Check Key
print("Kalit mavjudmi:", kalit in d)

# Kalitlarni hisoblash
print("Kalitlar soni:", len(d))

# Hamma kalitlarni olish
print("Kalitlar:", list(d.keys()))

# Hamma qiymatlarni olish
print("Qiymatlar:", list(d.values()))

# Lug'atlarni birlashtirish
birlashtirilgan = {**d, **d2}
print("Birlashtirilgan:", birlashtirilgan)

# Kalitni olib tashlash
d.pop('a', None)
print("Kalit olib tashlandi:", d)

# Yangi boʻsh lugʻatni yaratish
yangi = dict()
print("Bo'sh lug'at:", yangi)

# Lugʻatning boʻsh ekanligini tekshirish
print("Bo'shmi:", len(yangi) == 0)

# Kalit-qiymat juftligini olish
kalit = 'b'
if kalit in d:
    print("Juftlik:", (kalit, d[kalit]))
else:
    print("Kalit topilmadi")

# Qiymatni yangilash
d['b'] = 10
print("Yangilangan qiymat:", d)

# Qiymat hodisalarini hisoblash
qiymat = 10
print("Qiymat hodisalari:", list(d.values()).count(qiymat))

# Lug'atni teskari aylantirish
teskari = {v: k for k, v in d.items()}
print("Teskari lug'at:", teskari)

# Qiymatli kalitlarni toping
qiymat = 10
kalitlar = [k for k, v in d.items() if v == qiymat]
print("Qiymatli kalitlar:", kalitlar)

# Ro'yxatlardan lug'at yaratish
kalitlar = ['x', 'y', 'z']
qiymatlar = [7, 8, 9]
yangi_dict = dict(zip(kalitlar, qiymatlar))
print("Ro'yxatlardan lug'at:", yangi_dict)

# Ichki lug'atlarni tekshirish
d3 = {'a': {'x': 1}, 'b': 2}
print("Ichki lug'atlar bormi:", any(isinstance(v, dict) for v in d3.values()))

# Ichki qiymatni olish
print("Ichki qiymat:", d3['a'].get('x') if isinstance(d3['a'], dict) else None)

# Andoza lugʻatni yaratish
from collections import defaultdict
andoza = defaultdict(lambda: 0)
andoza['a'] = 5
print("Andoza lug'at:", dict(andoza))
print("Yo'q kalit uchun:", andoza['b'])

# Noyob qiymatlarni hisoblang
print("Noyob qiymatlar soni:", len(set(d.values())))

# Lugʻatni kalitlar boʻyicha saralash
saralangan_k = dict(sorted(d.items()))
print("Kalitlar bo'yicha saralash:", saralangan_k)

# Lugʻatni qiymat boʻyicha saralash
saralangan_v = dict(sorted(d.items(), key=lambda x: x[1]))
print("Qiymat bo'yicha saralash:", saralangan_v)

# Qiymat bo'yicha filtrlash (masalan, qiymati 5 dan katta)
filtr = {k: v for k, v in d.items() if v > 5}
print("Qiymat bo'yicha filtr:", filtr)

# Umumiy kalitlarni tekshirish
d4 = {'b': 10, 'f': 6}
print("Umumiy kalitlar bormi:", bool(set(d) & set(d4)))

# Kalit-qiymat juftligidan lug'at yaratish
juftliklar = [('m', 1), ('n', 2)]
juftlik_dict = dict(juftliklar)
print("Juftliklardan lug'at:", juftlik_dict)

# Birinchi kalit-qiymat juftligini olish
if d:
    birinchi = next(iter(d.items()))
    print("Birinchi juftlik:", birinchi)
else:
    print("Lug'at bo'sh")