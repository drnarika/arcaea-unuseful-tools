import json

#TODO:添加616排序 可能？
path_slst = input('输入songlist文件夹')
path_slst = path_slst + '\songlist'

remotedl_yesorno = str(input('输入1设置remote_dl为True，其他则反之'))
if remotedl_yesorno == '1':
    key = True
else:
    key = False
slst = open(path_slst,'r',encoding='utf-8')
try:
    slst_text = slst.read()
    slst_json = json.loads(slst_text)
    slst.close()
except Exception as e:
    print('读取失败或slst不合法',e)
    exit(1)
for s in range(0,len(slst_json['songs'])):
    slst_json['songs'][s]['remote_dl'] = key

slst_comp = json.dumps(slst_json, indent=2,ensure_ascii=False)
slst = open(path_slst,'w',encoding='UTF-8')
slst.write(slst_comp)
print('Done.')