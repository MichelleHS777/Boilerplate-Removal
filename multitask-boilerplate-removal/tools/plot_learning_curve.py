# Plotting
import matplotlib.pyplot as plt
import numpy as np

train_losses=[]
val_losses=[]
train_loss = []
val_loss = []

f = open('../result/220520/AllLoss+alpha025.txt', 'r')
for line in f.readlines():
    if "train loss" in line:
        # print('train')
        tr_loss = float(line.strip('train loss:    '))
        train_losses.append(tr_loss)
    elif "val loss" in line:
        # print('val')
        v_loss = float(line.strip('val loss:    ').replace('*',''))
        val_losses.append(v_loss)
    if "==========" in line:
        print("===Epoch====")
        print(np.mean(train_losses), np.mean(val_losses))
        train_loss.append(np.mean(train_losses))
        val_loss.append(np.mean(val_losses))
        train_losses=[]
        val_losses=[]

loss = {'train_loss':train_loss, 'val_loss':val_loss}
plt.plot(loss['train_loss'])
plt.plot(loss['val_loss'])
plt.title("Model Loss")
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.legend(["Train", "Val"], loc='upper left')
plt.xlim([2, 20])
# plt.legend(["Train"], loc='upper left')
plt.savefig('../result/220520/AllLoss+alpha025.png')