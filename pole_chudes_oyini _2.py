q = 's'
w = 'a'
e = 'l'
r = 'o'
t = 'm'
y = 'salom'

print('Salom pole chudes oyiniga hush kelibsiz,')
print('oyinga kirish uchun ha sozini kiriting')
p = input('Kiriting = ')
if p == 'yoq':
    print('Mayli sog bolasiz')
else:
    print("Olg'a bo'masa")
    kiritish = input('kiriting = ')
    print('hohlasangiz tahminiy sozingizni kiriting')


while kiritish !=0:
    if kiritish == q:
        print('siz kiritgan s harfi sozda mavjud')
        print('hohlasangiz tahminiy sozingizni kiriting')
        kiritish = input('kiriting = ')
    elif kiritish == w:
        print('siz kiritgan a harfi sozda mavjud')
        print('hohlasangiz tahminiy sozingizni kiriting')
        z = q + w
        kiritish = input('kiriting = ')
    elif kiritish == e:
        print('siz kiritgan l harfi sozda mavjud')
        print('hohlasangiz tahminiy sozingizni kiriting')
        x = q+w+e
        kiritish = input('kiriting = ')
    elif kiritish == r:
        print('siz kiritgan o harfi sozda mavjud')
        print('hohlasangiz tahminiy sozingizni kiriting')
        c = q+w+e+r
        kiritish = input('kiriting = ')
    elif kiritish == t:
        v = q + w + e + r + t
        l = v
        print('Tabriklayman harflarni togri topdingiz javob esa '+ v +' sozi edi')
        print('endi esa salom sozini kiriting')
        kiritish = input('kiriting = ')
    elif kiritish == y:
        print('siz yutdingiz')


    else:
        print('mavjud emas')
        kiritish = input('kiriting = ')



