mevalar=['olma', 'dars', 'uyga vazifa', 'mashgulot', 'darslik']
print(len(mevalar)) #ro'yxatdagi elementlar soni
numb=[1, 2, 3, 4, 5]
print(sum(numb)) #ro'yxatdagi elementlar yig'indisi
ptint(max(numb)) #ro'yxatdagi eng katta element
print(min(numb)) #ro'yxatdagi eng kichik element
mevalar = ['olma', 'dars', 'uyga vazifa', 'mashgulot', 'darslik']
element = 'olma'

if element in mevalar:
    print(f"{element} ro'yxatda mavjud")
else:
    print(f"{element} ro'yxatda yo'q")
    if mevalar:
        print("So'nggi element:", mevalar[-1])
    else:
        print("Ro'yxat bo'sh")

    # Dilim ro'yxati (dastlabki uchta element)
    dilim = mevalar[:3]
    print("Dilim ro'yxati:", dilim)

    # Teskari ro'yxat
    teskari = mevalar[::-1]
    print("Teskari ro'yxat:", teskari)

    # Ro'yxatni saralash
    saralangan = sorted(mevalar)
    print("Saralangan ro'yxat:", saralangan)

    # Dublikatlarni olib tashlash
    mevalar2 = ['olma', 'olma', 'dars', 'dars', 'uyga vazifa']
    noyob = list(set(mevalar2))
    print("Noyob elementlar:", noyob)

    # Elementni qo'yish
    mevalar.insert(2, 'banan')
    print("Element qo'shilgan:", mevalar)

    # Element indeksi
    indeks = mevalar.index('olma')
    print("'olma' indeksi:", indeks)

    # Bo'sh ro'yxatni tekshirish
    # bo'sh = [] # type: ignore
    # if not bo'sh:
        # print("Ro'yxat bo'sh")

    # Juft sonlarni hisoblash
    numb = [1, 2, 3, 4, 5]
    juft_sonlar = [x for x in numb if x % 2 == 0]
    print("Juft sonlar soni:", len(juft_sonlar))

    # Toq sonlarni hisoblash
    toq_sonlar = [x for x in numb if x % 2 != 0]
    print("Toq sonlar soni:", len(toq_sonlar))

    # Ro'yxatlarni birlashtirish
    a = [1, 2]
    b = [3, 4]
    birlashtirilgan = a + b
    print("Birlashtirilgan ro'yxat:", birlashtirilgan)

    # Sublistni topish
    sub = [2, 3]
    def sublist_bormi(royxat, sub):
        for i in range(len(royxat) - len(sub) + 1):
            if royxat[i:i+len(sub)] == sub:
                return True
        return False
    print("Sublist mavjud:", sublist_bormi(numb, sub))

    # Elementni almashtirish
    mevalar[mevalar.index('olma')] = 'nok'
    print("Element almashtirilgan:", mevalar)

    # Ikkinchi eng katta toping
    def ikkinchi_eng_katta(royxat):
        return sorted(set(royxat))[-2]
    print("Ikkinchi eng katta:", ikkinchi_eng_katta(numb))

    # Ikkinchi eng kichik elementni toping
    def ikkinchi_eng_kichik(royxat):
        return sorted(set(royxat))[1]
    print("Ikkinchi eng kichik:", ikkinchi_eng_kichik(numb))

    # Juft sonlarni filtrlash
    juftlar = [x for x in numb if x % 2 == 0]
    print("Juftlar:", juftlar)

    # Toq sonlarni filtrlash
    toqlar = [x for x in numb if x % 2 != 0]
    print("Toqlar:", toqlar)

    # Ro'yxat uzunligi
    print("Ro'yxat uzunligi:", len(mevalar))

    # Nusxasini yaratish
    nusxa = mevalar.copy()
    print("Nusxa:", nusxa)

    # O'rta elementni oling
    def orta_element(royxat):
        n = len(royxat)
        if n == 0:
            return None
        elif n % 2 == 1:
            return royxat[n//2]
        else:
            return royxat[n//2-1:n//2+1]
    print("O'rta element:", orta_element(numb))

    # Maksimal Sublistni topish
    sublist = [2, 3, 4]
    print("Sublist maksimal:", max(sublist))

    # Pastki ro'yxatning minimal qismini toping
    print("Sublist minimal:", min(sublist))

    # Elementni indeks bo'yicha olib tashlash
    ind = 2
    if ind < len(mevalar):
        del mevalar[ind]
    print("Indeks bo'yicha olib tashlandi:", mevalar)

    # Ro'yxatning tartiblanganligini tekshirish
    def tartiblanganmi(royxat):
        return royxat == sorted(royxat)
    print("Tartiblanganmi:", tartiblanganmi(numb))

    # Elementlarni takrorlash
    takror = [x for x in numb for _ in range(2)]
    print("Takrorlangan:", takror)

    # Birlashtirish va saralash
    birlashtir_sarala = sorted(a + b)
    print("Birlashtir va sarala:", birlashtir_sarala)

    # Barcha indekslarni toping
    element = 2
    indekslar = [i for i, x in enumerate(numb) if x == element]
    print("Barcha indekslar:", indekslar)

    # Ro'yxatni aylantirish (o'ngga siljitish)
    def aylantir(royxat, n=1):
        return royxat[-n:] + royxat[:-n]
    print("Aylantirilgan:", aylantir(numb, 2))

    # Diapazon ro'yxatini yaratish
    diapazon = list(range(1, 11))
    print("Diapazon:", diapazon)

    # Musbat sonlar yig'indisi
    musbat = [x for x in numb if x > 0]
    print("Musbat yig'indi:", sum(musbat))

    # Salbiy sonlar yig'indisi
    salbiy = [x for x in numb if x < 0]
    print("Salbiy yig'indi:", sum(salbiy))

    # Palindrome'ni tekshiring
    def palindrome(royxat):
        return royxat == royxat[::-1]
    print("Palindrome:", palindrome([1,2,3,2,1]))

    # Ichki ro'yxatni yaratish
    def ichki_royxat(royxat, n):
        return [royxat[i:i+n] for i in range(0, len(royxat), n)]
    print("Ichki ro'yxat:", ichki_royxat(numb, 2))

    # Noyob elementlarni tartibda oling
    def noyob_tartibda(royxat):
        res = []
        for x in royxat:
            if x not in res:
                res.append(x)
        return res
    print("Noyob tartibda:", noyob_tartibda([1,2,2,3,1,4]))
