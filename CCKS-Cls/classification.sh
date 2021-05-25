python3 Cls_data_preprocess.py
python3 run_bert.py --do_data
python3 run_bert.py --do_train --save_best  --train_batch_size 16 --n_gpu 0
python3 run_bert.py --do_test  --n_gpu 0
