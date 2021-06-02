python3 Cls_data_preprocess.py
python3 run_bert.py --do_data
python3 run_bert.py --do_train --save_best  --train_batch_size 32 --n_gpu 1 --epochs 10
python3 run_bert.py --do_test  --n_gpu 1 --eval_batch_size 16
