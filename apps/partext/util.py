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