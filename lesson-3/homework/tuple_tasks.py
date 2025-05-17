# Misol uchun tuple
t = (1, 2, 3, 2, 4, 2, 5)

# Hodisalarni soni
element = 2
print("Hodisalar soni:", t.count(element))

# Max element
print("Max element:", max(t))

# Min element
print("Min element:", min(t))

# Elementni tekshirish
print("Element mavjudmi:", element in t)

# Birinchi element
if t:
    print("Birinchi element:", t[0])
else:
    print("Tuple bo'sh")

# So'nggi element
if t:
    print("So'nggi element:", t[-1])
else:
    print("Tuple bo'sh")

# Tuple uzunligi
print("Tuple uzunligi:", len(t))

# Slice tuple (dastlabki uchta element)
slice_tuple = t[:3]
print("Slice tuple:", slice_tuple)

# Birgalikda tuples
t2 = (6, 7)
birgalikda = t + t2
print("Birgalikda tuple:", birgalikda)

# Tuple boʻsh ekanligini tekshirish
print("Tuple bo'shmi:", len(t) == 0)

# Elementning barcha indekslari
indekslar = [i for i, x in enumerate(t) if x == element]
print("Barcha indekslar:", indekslar)

# Ikkinchi eng katta toping
def ikkinchi_eng_katta(t):
    return sorted(set(t))[-2]
print("Ikkinchi eng katta:", ikkinchi_eng_katta(t))

# Ikkinchi eng kichik toping
def ikkinchi_eng_kichik(t):
    return sorted(set(t))[1]
print("Ikkinchi eng kichik:", ikkinchi_eng_kichik(t))

# Bitta element tuple yaratish
yangi_tuple = (42,)
print("Bitta element tuple:", yangi_tuple)

# Ro'yxatni tuplega aylantirish
lst = [1, 2, 3]
tuplega = tuple(lst)
print("Ro'yxatdan tuple:", tuplega)

# Tuple tartiblanganligini tekshirish
print("Tartiblanganmi:", t == tuple(sorted(t)))

# Subtuple maksimal qismini topish
subtuple = (2, 3, 4)
print("Subtuple maksimal:", max(subtuple))

# Subtuplening minimal qismini toping
print("Subtuple minimal:", min(subtuple))

# Elementni qiymati bo'yicha olib tashlash
def olib_tashlash(t, el):
    lst = list(t)
    if el in lst:
        lst.remove(el)
    return tuple(lst)
print("Qiymati bo'yicha olib tashlandi:", olib_tashlash(t, 2))

# Ichki tuple yaratish
def ichki_tuple(t, n):
    return tuple(t[i:i+n] for i in range(0, len(t), n))
print("Ichki tuple:", ichki_tuple(t, 2))

# Elementlarni takrorlash
def takrorla(t, n):
    return tuple(x for x in t for _ in range(n))
print("Takrorlangan:", takrorla(t, 2))

# Range tuple yaratish
range_tuple = tuple(range(1, 11))
print("Range tuple:", range_tuple)

# Teskari tuple
teskari = t[::-1]
print("Teskari tuple:", teskari)

# Palindrome'ni tekshiring
def palindrome(t):
    return t == t[::-1]
print("Palindrome:", palindrome((1,2,3,2,1)))

# Noyob elementlarni oling
def noyob_tuple(t):
    res = []
    for x in t:
        if x not in res:
            res.append(x)
    return tuple(res)
print("Noyob tuple:", noyob_tuple((1,2,2,3,1,4)))