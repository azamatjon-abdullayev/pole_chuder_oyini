q = 's'
w = 'a'
e = 'l'
r = 'o'
t = 'm'

y = 'salom'

print('Salom pole chudes oyiniga hush kelibsiz')
kiritish = input('tahminiy harf yoki siz oylagan sozni kiriting = ')


def togri_javoblar():
    royhat = []
    if kiritish == q:
        kiritish.join(royhat)
    if kiritish == w:
        kiritish.join(royhat)
    if kiritish == e:
        kiritish.join(royhat)
    if kiritish == r:
        kiritish.join(royhat)
    if kiritish == t:
        kiritish.join(royhat)
        print(royhat)


while kiritish != 0:
    if kiritish == q:
        print('siz kiritgan s harfi sozda mavjud')
        print('topgan harflaringizni korish uchun 1ni kiriting')
        if kiritish == 1:
            togri_javoblar()

        kiritish = input('kiriting = ')
    elif kiritish == w:
        print('siz kiritgan a harfi sozda mavjud')
        print('topgan harflaringizni korish uchun 1ni kiriting')

        togri_javoblar()
        print(z)
        z = q + w
        kiritish = input('kiriting = ')
    elif kiritish == e:
        print('siz kiritgan l harfi sozda mavjud')
        print('topgan harflaringizni korish uchun 1ni kiriting')

        togri_javoblar()
        x = q + w + e
        kiritish = input('kiriting = ')
    elif kiritish == r:
        print('siz kiritgan o harfi sozda mavjud')
        print('topgan harflaringizni korish uchun 1ni kiriting')

        togri_javoblar()
        c = q + w + e + r
        kiritish = input('kiriting = ')
    elif kiritish == t:
        v = q + w + e + r + t
        print('Tabriklayman harflarni togri topdingiz javob esa ' + v + ' sozi edi')
        print('endi esa salom sozini kiriting')
        kiritish = input('kiriting = ')
    elif kiritish == y:
        print('siz yutdingiz')
    else:
        print('Siz kiritgan harf yoki soz mavjud emas')
        kiritish = input('kiriting = ')
