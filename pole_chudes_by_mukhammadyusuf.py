from console.utils import clear

openLetters = []
gameFinished = False # <- bu asosiy - GLOBAL


def show_open_letters():
    print(get_answer_mask_letters())


def get_answer_mask_letters(): # <- yana bir SOHA
    global gameFinished  ## SHU nima qiladi?
    result = ''
    for letter in word:
        if letter in openLetters:
            result += letter
        else:
            result += '*'
    gameFinished = '*' not in result
    print('Exit function')
    return result


def open_letter(letter: str):
    openLetters.append(letter)
    show_open_letters()


if __name__ == '__main__':
    word = str(input("O'yin uchun so'zni kiriting (boshlovchi): "))
    print()

    print('\r')
    clear()

    while not gameFinished:
        users_letter = str(input('Xarfni kiriting: '))

        if users_letter == 'exit':
            print('Xayr')
            break

        if len(users_letter) != 1:
            print('XARF DEDIK, SO\'Z emas!')
            continue  ## BU nima qiladi? Nega `return` emas?

        if users_letter in openLetters:
            print('Bu xarf ochilgan! Esar')
            continue  ## BU nima qiladi? Nega `return` emas?
        open_letter(users_letter)
