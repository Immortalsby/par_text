from deep_translator import DeeplTranslator

def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

def deal_star(s):
    new = []
    for c in s:
        new.append(c)
    for i,v in enumerate(s):
        if v == '*':
            new[i+1] = new[i+1].upper()
    new = ['' if x == '*' else x for x in new]
    return ''.join(new)

def get_head(s):
    i = s.rfind('>')
    if i:
        return s[0:i+1]
    return ''

def guess_key(s):
    if is_contains_chinese(s):
        source, target = 'chinese', 'french'
    else:
        source, target = 'french', 'chinese'
    translated = DeeplTranslator(api_key="94001194-c302-dea6-9fda-02a577bb4b3f:fx",
source=source, target=target, use_free_api=True).translate(s, return_all=True)
    return translated

def matchcase(pre,word,suf):
    def replace(m):
        text = m.group()
        if text.isupper():
            return pre + word.upper() + suf
        elif text.islower():
            return pre + word.lower() + suf
        elif text[0].isupper():
            return pre +word.capitalize() + suf
        else:
            return pre + word + suf
    return replace
