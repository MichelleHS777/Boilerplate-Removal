category = ['功能', '品質', '無', '配件', '售後', '外觀', '價位', '音量']
cate2idx = {cate:idx for idx, cate in enumerate(category)}
idx2cate = {idx: cate for cate, idx in cate2idx.items()}
print(len(cate2idx))
print(idx2cate)
# import numpy as np
# import tensorflow as tf
# import pandas as pd

# file = './data/cleaneval/mix/mix_data/new_zh_0033.csv' # 'ce_6-level-33.csv' # new_zh_0033.csv

# if "ce" in file:
#     domain = 0 # cleaneval
# else:
#     domain = 1 # newdata
# domain = pd.Series([domain])
# # print('np of domain: ', np.array(domain), '\n')
# domain_out = tf.one_hot(np.array(domain), 2)
# # print('domain out:', type(domain_out))


# # df = pd.read_csv(file)
# # label = tf.one_hot(np.array(df['label']), 2)
# # print('label: \n', label)