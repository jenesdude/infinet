import sys
import textfsm
from re import findall

template = "parse_status_OCT.template"
input_file = sys.argv[1]


def quote_strings(string):
    """Функция для заключения строк в кавычки, если они содержат буквы.
    Работает и в случае, если на вход дан плоский массив подобных строк."""
    if type(string) == list:
        quoted = []
        for e in string:
            if findall('[^0-9-.]', e):
                quoted.append('"' + e + '"')
            else:
                quoted.append(e)
        return quoted
    else:
        if findall('[^0-9-.]', string):
            return '"' + string + '"'
        else:
            return string


with open(template) as f, open(input_file) as input_file:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(input_file.read())[0]
    for i in range(len(header)):
        if type(result[i]) == list:
            print('{}: {}'.format(header[i].replace('_', ' '),
                                  ", ".join(quote_strings(result[i]))))
        else:
            print('{}: {}'.format(header[i].replace('_', ' '),
                                  quote_strings(result[i])))
