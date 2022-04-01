import glob
# from re import I
import numpy as np
from sklearn.model_selection import KFold
import shutil  #Python檔案複製相應模組
# import os


files = glob.glob("./newdata/cv5fold2/train/4/*.csv")
# print(len(files))
files = np.array(files)
kf = KFold(n_splits=5) #分割為多少個K子集
# print(kf.get_n_splits(files))
count = 0

train_dir='./newdata/cv5fold2/train/'
test_dir='./newdata/cv5fold2/test/'

train2_dir='./newdata/cv5fold2/train2/'
valid_dir='./newdata/cv5fold2/valid/'


# for i in range(5):
    # os.mkdir(valid_dir+str(i))
    # os.mkdir(train2_dir+str(i))
#     os.mkdir(train_dir+str(i))
#     os.mkdir(test_dir+str(i))

for train_index, test_index in kf.split(files):
    print("TRAIN:", len(train_index), "VALID:", len(test_index))
    file_train, file_test = files[train_index], files[test_index]
    for ftr in file_train :
        shutil.copy(ftr.replace('\\\\','\\'),train2_dir+str(4)) #count
    for fte in file_test :
        shutil.copy(fte.replace('\\\\','\\'),valid_dir+str(4)) #count
    break
    # count += 1
#     ## file = './newdata/output\\0009.csv'.replace('\\\\','\\')
# # print(count)
