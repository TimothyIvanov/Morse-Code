m_e = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '---...': ':',
    '.----.': '\'',
    '-....-': '-',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-..-.': '\"',
    '-...-': '=',
    '...-.': 'Understood',
    '........': 'Error',
    '.-.-.': '+',
    '.-...': 'Wait',
    '...-.-': 'End of work',
    '-.-.-': 'Starting signal',
    '.--.-.': '@',
    '/': ' '}

e_m = {y:x for (x, y) in m_e.items()}

def main():
    while True:
        version = str(input('Enter 1 for Morse to English. Enter 2 for English to Morse.'))
        if version == '1':
            morse_to_english(m_e)
        elif version == '2':
            english_to_morse(e_m)
        else:
            print('Invalid input. Try again.')
            continue

def morse_to_english(morse_eng):
    final = []
    temp = []
    morse_code = morse_input_vldt() + ' '
    for n in morse_code:
        if n != ' ':
            temp.append(n)
        else:
            if len(temp) > 0:
                temp = ''.join(temp)
                final.append(morse_eng[temp])
                temp = []
            else:
                continue
    print(''.join(final))
    
def english_to_morse(eng_morse):
    eng_list = []
    eng_text = str(input('Enter English text here:'))
    space = 0
    for i in eng_text.upper():
        if i == ' ':
            space = True
        elif space and i != ' ':
            eng_list.append('/')
            eng_list.append(eng_morse[i])
            space = 0
        else: 
            eng_list.append(eng_morse[i])
    print(' '.join(eng_list))

def morse_input_vldt():
    valid = '.-/ '
    while True:
        morse_input = str(input('Enter Morse code here, using \'.\' as short, and \'-\' as long:'))
        for i in morse_input:
            if i not in valid:
                print('Invalid input. Try again.')
                break
        return morse_input

main()