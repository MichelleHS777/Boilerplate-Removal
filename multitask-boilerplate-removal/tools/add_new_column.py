import glob
import pandas as pd

files = glob.glob("./test/newdata_zh/*.csv")

for file in files:
    # print(file)
    df = pd.read_csv(file)    
    if "ce" in file:
        df.insert(len(df.columns), column='domain', value=['cleaneval']*len(df))
    else:
        df.insert(len(df.columns), column='domain', value=['newdata']*len(df))
    df.to_csv(file, encoding='utf-8-sig', index=False)
