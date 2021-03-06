accents = [
   ["'a", "á"], ['"a', "ä"], ["^a", "â"], ["`a", "à"],
   ["'e", "é"], ['"e', "ë"], ["^e", "ê"], ["`e", "è"],
   ["'i", "í"], ['"i', "ï"], ["^i", "î"], ["`i", "ì"],
   ["'o", "ó"], ['"o', "ö"], ["^o", "ô"], ["`o", "ò"],
   ["'u", "ú"], ['"u', "ü"], ["^u", "û"], ["`u", "ù"],
   ["cc", "ç"], ['ug', 'ğ'], ['"U', "Ü"], ['"u', "ü"],
   ["vZ", "Ž"], ['vc', 'č'], ['Ho', "ő"], ['O', "Ø"],
   ['o', "ø"], ['l', 'ł'], ["'n", "ń"], ['v{s}', 'š'],
   ['v{S}', 'Š'], ['L', 'Ł'], ['&', '&amp;'], ["'c", "ć"],
   ['v{c}', 'č'],
   ['~n', 'ñ']
]

def xml_string(text):
    text = text.replace("``", u"“")
    text = text.replace("''", u"”")

    for tex, utf8 in accents:
        # utf8 = utf8.decode('utf-8')
        text = text.replace('{\\%s}' % tex, utf8)          # {\"a}
        # text = text.replace('\\%s' % tex, utf8)            # \"a
        try:
            text = text.replace('\\%s{%s}' % tuple(tex), utf8) # \"{a}
        except TypeError:
            pass
        # sometimes words are but in brackets in bibtex to make it {CapiTaliZed} correctly
    # text = text.replace('{', '').replace('}', '')
    return text