"""
Содержит реализацию таких функций:
    1. Шифрование методом цезаря
    2. Частотный анализ
    3. Дешифровка, средствами частотного анализа
    4. Определение, шифрован текст или нет
"""

ALPHABET_LEN = 26

ALPHABET_UPPER = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z')  # len(alphabet) = 26

ALPHABET_LOWER = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z')

ORIGINAL_FREQUENCY = {'a': 8.17,
                      'b': 1.49,
                      'c': 2.78,
                      'd': 4.25,
                      'e': 12.7,
                      'f': 2.23,
                      'g': 2.02,
                      'h': 6.09,
                      'i': 6.97,
                      'j': 0.15,
                      'k': 0.77,
                      'l': 4.03,
                      'm': 2.41,
                      'n': 6.75,
                      'o': 7.51,
                      'p': 1.93,
                      'q': 0.1,
                      'r': 5.99,
                      's': 6.33,
                      't': 9.06,
                      'u': 2.76,
                      'v': 0.98,
                      'w': 2.36,
                      'x': 0.15,
                      'y': 1.97,
                      'z': 0.05,
                      }


def shifr(input_text, rot):
    """
    Шифрует текст методом цезаря.

    :param input_text: исходный текст
    :param rot: сдвиг
    :return: зашифрованный текст
    """
    output_text = ""

    for char in input_text:
        upper_f = False
        index_char = None

        if char in ALPHABET_LOWER:
            index_char = ALPHABET_LOWER.index(char)
        elif char in ALPHABET_UPPER:
            index_char = ALPHABET_UPPER.index(char)
            upper_f = True

        if index_char is None:
            output_text = output_text + char
            continue
        elif index_char + rot >= ALPHABET_LEN:
            index_char = index_char + rot - ALPHABET_LEN
        else:
            index_char = index_char + rot

        if upper_f:
            output_text = output_text + ALPHABET_UPPER[index_char]
        else:
            output_text = output_text + ALPHABET_LOWER[index_char]

    return output_text


def freq_analysis(input_text):
    """

    Подсчитывает частоту повторений букв в тексте

    :param input_text: анализируемый текст
    :return: dict{'буква': частота повторений}
    """

    input_text.swapcase()  # переводит строку в нижний регистр
    frequency_letter = {'a': 0,
                        'b': 0,
                        'c': 0,
                        'd': 0,
                        'e': 0,
                        'f': 0,
                        'g': 0,
                        'h': 0,
                        'i': 0,
                        'j': 0,
                        'k': 0,
                        'l': 0,
                        'm': 0,
                        'n': 0,
                        'o': 0,
                        'p': 0,
                        'q': 0,
                        'r': 0,
                        's': 0,
                        't': 0,
                        'u': 0,
                        'v': 0,
                        'w': 0,
                        'x': 0,
                        'y': 0,
                        'z': 0,
                        }
    for char in ALPHABET_LOWER:
        frequency_letter[char] = input_text.count(char) / len(input_text) * 100
    return frequency_letter


def freq_decrypt(crypt_text):
    """
    Алгоритм подбора шифра.
    Перебираем все варианты смещения. И определяем насколько частотная
    характеристика текста соответствует обычному тексту.
    Выводим самый близкий результат

    Метод не всегда работает с короткими сообщениями,
    в которых частотные характеристики могут сильно
    отличатся от характеристик естественного языка.

    :param crypt_text: зашифрованный текст
    :return: dict{'Rot': N,
                'freq_diff': k}

    """
    nearly_rotation = {'rot': 0,
                       'freq_diff': 0}
    i = 0
    while i < ALPHABET_LEN:
        difference = 0

        decrypt_text = shifr(crypt_text, i)
        frequency_decrypt = freq_analysis(decrypt_text)

        for symbol in ORIGINAL_FREQUENCY:
            difference = difference + ORIGINAL_FREQUENCY[symbol] * frequency_decrypt[symbol]

        if nearly_rotation['freq_diff'] == 0:
            nearly_rotation['freq_diff'] = difference
            nearly_rotation['rot'] = ALPHABET_LEN - i
        elif nearly_rotation['freq_diff'] < difference:
            nearly_rotation['freq_diff'] = difference
            nearly_rotation['rot'] = ALPHABET_LEN - i

        i += 1

    return nearly_rotation

def info_decrypt(input_text):
    """
    Определяет зашифрован ли текст, и если да, создает словарь для вывода на страницу

    :param input_text:
    :return: Словарь со сдвигом и дешифрованным текстом
    """
    decrypt_key = freq_decrypt(input_text)
    out_text = {'header': "",
                'decrypt_text': ""}
    if decrypt_key['rot'] < 26:
        out_text['header'] = "Предположительный сдвиг: " + str(decrypt_key['rot'])
        out_text['decrypt_text'] = shifr(input_text, 26 - decrypt_key['rot'])

    return out_text