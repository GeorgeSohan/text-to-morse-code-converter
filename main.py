
MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '. _ _ _ .',
    '!': '_ . _ . _ _',
    '/': '_ . . _ .',
    '(': '_ . _ _ .',
    ')': '_ . _ _ . _',
    '&': '. _ . . .',
    ':': '_ _ _ . . .',
    ';': '_ . _ . _ .',
    '=': '_ . . . _',
    '+': '. _ . _ .',
    '-': '_ . . . . _',
    '_': '. . _ _ . _',
    '"': '. _ . . _ .',
    '$': '. . . _ . . _',
    '@': '. _ _ . _ .',
}

text_to_convert = input('Morse Code Converter\nType text to convert to Morse Code!\n')
output_list = []


def converter():
    for letter in text_to_convert:
        letter = letter.upper()
        output_list.append(MORSE_CODE_DICT[letter])
    return output_list


result = ' '.join(converter())
print(f'The Morse Code of {text_to_convert} is {result}')
