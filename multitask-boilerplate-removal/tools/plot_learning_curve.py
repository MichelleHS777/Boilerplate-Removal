# Plotting
import matplotlib.pyplot as plt
import numpy as np

# save interation
train_losses=[]
val_losses=[]

# save epoch 
train_loss = []
val_loss = []

f = open('../result/220526/addDomain.txt', 'r')
for line in f.readlines():
    if "train loss" in line:
        # print('train')
        loss = float(line.strip('train loss:    '))
        train_losses.append(loss) # save loss in iteration
    elif "val loss" in line:
        # print('val')
        loss = float(line.strip('val loss:    ').replace('*',''))
        val_losses.append(loss) # save loss in iteration
    if "==========" in line:
        print("===Epoch====")
        print(np.mean(train_losses), np.mean(val_losses))
        train_loss.append(np.mean(train_losses)) # save loss in epoch 
        val_loss.append(np.mean(val_losses))
        train_losses=[] # Clear old iteration loss
        val_losses=[]

# Plot learning curve
loss = {'train_loss':train_loss, 'val_loss':val_loss} # create dictionary
plt.plot(loss['train_loss'])
plt.plot(loss['val_loss'])
plt.title("Model Loss")
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.legend(["Train", "Val"], loc='upper left')
plt.xlim([2, 20])
# plt.legend(["Train"], loc='upper left')
plt.savefig('../result/220526/addDomain.png')