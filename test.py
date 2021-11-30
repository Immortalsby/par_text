import time

fr = "upload/3aube_FR_para_utf8.txt"
zh = "upload/3aube_CN_para_utf8.txt"
zh_datas = ''
fr_datas = ''
with open(zh,'r',encoding='utf-8') as f_zh:
    zh_data = f_zh.read()
    zh_data = zh_data.split('#')
with open(fr,'r',encoding='utf-8') as f_fr:
    fr_data = f_fr.read()
    fr_data = fr_data.split('#')
for zh_datas,fr_datas in zip(zh_data,fr_data):
    print(f"-------\n{zh_datas}{fr_datas}-------\n")
    time.sleep(.5)