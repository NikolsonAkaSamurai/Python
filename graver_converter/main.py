file = open('num2.txt')
# file = open(r'C:\Users\Николай\Desktop\уп\ДЕТАЛЬ1\num9.nc', encoding='utf-8')

def read_file():
    list_of_lines = file.readlines()
    return list_of_lines

def probeg():
    for row in file:
        for letter in file:
            if letter == 'X':
                let = letter
                return let

def check_words():
    list_of_words = []
    buf = ""
    for char in str:
        if char == ' ' or char == '%':
            list_of_words += [buf]
            buf = ""
        buf += char
    return list_of_words

list_text = []

for string in file:

    last_letter = ''
    list_of_letters = []
    str_letters ="XYZGSFM"
    for char in str_letters:
        list_of_letters += [char]

    for char in string:

        for i in range(len(list_of_letters)):
            if char == list_of_letters[i]:
                last_letter = list_of_letters[i]
        if char != ' ':
            list_text += [char]

        if char == 'X' or char == 'Y':
            list_text += ['[']
            list_text += ['[']
        if char == ' ' and last_letter == 'X':
            list_text += "*#6]+#24] "
        if char == ' ' and last_letter == 'Y':
            list_text += "*#6]+#25]"

temp = ""

for char in list_text:
    temp += char

print(temp)