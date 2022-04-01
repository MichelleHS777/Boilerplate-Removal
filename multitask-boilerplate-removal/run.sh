#! /usr/bin/Python


python main.py --train --train_folder="./newdata/cv5fold2/train/3/" --val_folder="./newdata/cv5fold2/valid/3/" > ./newdata/cv5fold2/result/eventgo_trainvali3.log

python main.py --test_folder="./newdata/cv5fold2/test/3/" > ./newdata/cv5fold2/result/eventgo_test3.log


python main.py --train --train_folder="./newdata/cv5fold2/train/4/" --val_folder="./newdata/cv5fold2/valid/4/" > ./newdata/cv5fold2/result/eventgo_trainvali4.log

python main.py --test_folder="./newdata/cv5fold2/test/4/" > ./newdata/cv5fold2/result/eventgo_test4.log