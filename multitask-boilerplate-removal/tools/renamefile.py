## chage the path to the current file you want to change
import os

# rename
for file in os.listdir(os.getcwd()):
    file = file.replace('.csv','')
    os.rename(file+'.csv', 'new_zh_'+file+'.csv') 
    # start+=1

print('='*20+"Rename Success"+"="*20)
# 列出重命名的目錄
print("目錄為: %s" %os.listdir(os.getcwd())) #getcwd: 當前工作目錄
