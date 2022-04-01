import pandas as pd
import csv
urlList=[]
# url=[]
data = pd.read_csv("./testcodedata/ESPURL-220210.csv")

## see if data is duplicate
# esp_list = data.iloc[:, 0].tolist()
# print(len(set(mydata)))

# each save 30
for i in range(0,len(data)):
    esp_list = data.iloc[i*30:(i*30)+30, 5].tolist() # each save 30 , col = 5
    # print(len(esp_list))
    urlList.append(esp_list)

# # save all
# esp_list = data.iloc[:, 5].tolist() #translate all
# urlList.append(esp_list)


df = pd.Series(urlList).dropna()
df.to_csv('./testcodedata/ESPList.csv',index=False)
