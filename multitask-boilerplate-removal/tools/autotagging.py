from base64 import encode
import pandas as pd
import glob

for files in glob.glob("../testcodedata/preprocess/*.csv"):
    # print(files)
    data = pd.read_csv(files)
    label = data['label'] #get col 'label'

    # [print(label[i]) for i in range(len(label))]
    start,end = label[label==1].index
    
    for i in range(start,end):  #get start and end num with label=1
        data.at[i,"label"] = 1 # change 0 to 1

    data.to_csv(files,encoding='utf-8-sig',index = False)
        
    