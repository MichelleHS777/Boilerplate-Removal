urls=[]
for i in range(1,4):
    f = open('./Output/TXT/page-000'+str(i)+'.txt', 'r',encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        # print(line)
        if(bool(line.find('http'))):
            # print(line[line.find('http'):line.find('.com/')])
            urls.append(line[line.find('http'):line.find('.com/')])
            break
print(urls)
