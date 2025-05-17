# To'plamlar birlashmasi
a = {1, 2, 3}
b = {3, 4, 5}
birlashma = a | b
print("Birlashma:", birlashma)

# To'plamlarning kesishishi
kesishma = a & b
print("Kesishma:", kesishma)

# To'plamlarning farqi
farq = a - b
print("Farq:", farq)

# Pastki to'plamni tekshirish
print("a b ning pastki to'plamimi:", a <= b)

# Elementni tekshirish
element = 2
print("Element mavjudmi:", element in a)

# Uzunligi to'plam
print("To'plam uzunligi:", len(a))

# Ro'yxatni to'plamga aylantirish
lst = [1, 2, 2, 3, 4, 4]
setdan = set(lst)
print("Ro'yxatdan to'plam:", setdan)

# Elementni olib tashlash
a.discard(2)
print("Element olib tashlandi:", a)

# Toʻplamni tozalash
a.clear()
print("Tozalangan to'plam:", a)

# Set boʻsh ekanligini tekshiring
print("To'plam bo'shmi:", len(a) == 0)

# Simmetrik farq
a = {1, 2, 3}
b = {3, 4, 5}
simmetrik = a ^ b
print("Simmetrik farq:", simmetrik)

# Elementni qo'shish
a.add(6)
print("Element qo'shildi:", a)

# Pop elementi
popped = a.pop()
print("Pop qilingan element:", popped)
print("Qolgan to'plam:", a)

# Maksimalni topish
sonlar = {1, 5, 3, 9}
print("Maksimal:", max(sonlar))

# Minimalni topish
print("Minimal:", min(sonlar))

# Juft sonlarni filtrlash
juftlar = {x for x in sonlar if x % 2 == 0}
print("Juftlar:", juftlar)

# Toq sonlarni filtrlash
toqlar = {x for x in sonlar if x % 2 != 0}
print("Toqlar:", toqlar)

# Diapazon to'plamini yaratish
diapazon = set(range(1, 11))
print("Diapazon to'plami:", diapazon)

# Birlashtirish va takrorlash
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
birlashtir = set(lst1 + lst2)
print("Birlashtir va takrorlarni olib tashla:", birlashtir)

# Ajralgan to'plamlarni tekshiring
a = {1, 2}
b = {3, 4}
print("Ajralganmi:", a.isdisjoint(b))

# Ro'yxatdan nusxalarni olib tashlash
lst = [1, 2, 2, 3, 4, 4]
noyob_royxat = list(set(lst))
print("Noyob ro'yxat:", noyob_royxat)

# Noyob elementlarni hisoblang
print("Noyob elementlar soni:", len(set(lst)))

# Tasodifiy to'plamni yaratish
import random
tasodifiy = set(random.sample(range(1, 100), 5))
print("Tasodifiy to'plam:", tasodifiy)