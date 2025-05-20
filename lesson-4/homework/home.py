# Ikkita ro'yxatning faqat o'ziga xos (umumiy bo'lmagan) elementlarini qaytaruvchi funksiya

def oziga_xos_elementlar(list1, list2):
    natija = []
    list1_copy = list1.copy()
    list2_copy = list2.copy()
    # list1 dagi har bir elementni list2 da borligini tekshiramiz
    for el in list1:
        if el in list2_copy:
            list2_copy.remove(el)
        else:
            natija.append(el)
    # list2 dagi qolgan elementlarni natijaga qo'shamiz
    natija.extend(list2_copy)
    return natija

# Misollar
print(oziga_xos_elementlar([1, 1, 2], [2, 3, 4]))      # [1, 1, 3, 4]
print(oziga_xos_elementlar([1, 2, 3], [4, 5, 6]))      # [1, 2, 3, 4, 5, 6]
print(oziga_xos_elementlar([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]

n = 5
for i in range(1, n):
    print(i * i)

def ostki_chiziqcha_qosh(txt):
    unli = 'aeiou'
    natija = ''
    i = 0
    while i < len(txt):
        natija += txt[i]
        # Unli harf yoki oldingi harf ostki chiziqcha bo'lsa
        if (txt[i] in unli or (i > 0 and natija[-2] == '_')) and i < len(txt) - 1:
            natija += '_'
        i += 1
    return natija

# Misollar
print(ostki_chiziqcha_qosh("hello"))         # hel_lo
print(ostki_chiziqcha_qosh("assalom"))       # ass_alom
print(ostki_chiziqcha_qosh("abcabcdabcdeabcdefabcdefg"))  # abc_abcd_abcdeab_cdef_abcdefg

import random

def number_guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10
        print("1 dan 100 gacha son o'yladim. Topishga harakat qiling!")
        for _ in range(attempts):
            try:
                guess = int(input("Son kiriting: "))
            except ValueError:
                print("Faqat butun son kiriting!")
                continue
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("You guessed it right!")
                return
        print("You lost. Want to play again?")
        javob = input("Yana o'ynaysizmi? (Y/YES/y/yes/ok): ")
        if javob.lower() not in ['y', 'yes', 'ok']:
            break

# O'yinni boshlash uchun:
number_guessing_game()

# Oddiy parol tekshirgich
parol = input("Parol kiriting: ")
if len(parol) < 8:
    print("Parol juda qisqa")
elif not any(harf.isupper() for harf in parol):
    print("Parol katta harfdan iborat bo'lishi kerak")
else:
    print("Parol kuchli")

# 1 dan 100 gacha bo‘lgan barcha tub sonlarni chop etish
print("1 dan 100 gacha bo'lgan tub sonlar:")
for son in range(2, 101):
    tub = True
    for d in range(2, int(son ** 0.5) + 1):
        if son % d == 0:
            tub = False
            break
    if tub:
        print(son)

import random

def tosh_qogoz_qaychi():
    variantlar = ['rock', 'paper', 'scissors']
    user_score = 0
    comp_score = 0

    print("Tosh, qog'oz, qaychi o'yini! 5 ochkoga birinchi bo'lib g'alaba qozonadi.")
    while user_score < 5 and comp_score < 5:
        user = input("Tanlang (rock, paper, scissors): ").lower()
        if user not in variantlar:
            print("Noto'g'ri tanlov! Qayta urinib ko'ring.")
            continue
        comp = random.choice(variantlar)
        print(f"Kompyuter tanlovi: {comp}")

        if user == comp:
            print("Durrang!")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'scissors' and comp == 'paper') or \
             (user == 'paper' and comp == 'rock'):
            print("Siz yutdingiz!")
            user_score += 1
        else:
            print("Kompyuter yutdi!")
            comp_score += 1

        print(f"Hisob: Siz {user_score} - Kompyuter {comp_score}\n")

    if user_score == 5:
        print("Tabriklaymiz! Siz g'olib bo'ldingiz!")
    else:
        print("Kompyuter g'olib bo'ldi!")

# O'yinni boshlash uchun:

tosh_qogoz_qaychi()tosh_qogoz_qaychi()