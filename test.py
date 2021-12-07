import time

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


file = "upload/Macron20201212-FRCN.txt"
with open(file,'r',encoding='utf-8') as f_zh:
    datas = f_zh.read()
    datas = [x for x in datas.split('$') if x]
data_heads = []
data_fr = []
data_zh = []
for data in datas:
    data = '$' + data
    data = data.strip('\n')
    head = get_head(data)
    data_heads.append(head)
for i, data in enumerate(datas):
    data = '$' + data
    data = data.strip('\n')
    if '*' in data:
        data = deal_star(data)
    if 'ZH' in data_heads[i]:
        data = data.replace(' ','')
        data_zh.append(data.replace(data_heads[i], ''))
    else:
        data_fr.append(data.replace(data_heads[i], ''))
print(f"-------\n{data_zh[0:2]}-------\n")
print(f"-------\n{data_fr[0:2]}-------\n")
print(f"-------\n{data_heads[0:2]}-------\n")