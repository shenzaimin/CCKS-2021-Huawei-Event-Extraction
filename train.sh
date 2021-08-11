#!/bin/bash
# train for each event
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta_IF_1_1 --seed 2021 --device_num 1 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 10 --learning_rate 5e-5 --gradient_accumulation_steps 1 --type "IF" --train_or_predict 1
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta_SHF_1_1 --seed 2021 --device_num 1 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 10 --learning_rate 5e-5 --gradient_accumulation_steps 1 --type "SHF" --train_or_predict 1
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta_CD_1_1 --seed 2021 --device_num 1 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 10 --learning_rate 5e-5 --gradient_accumulation_steps 1 --type "CD" --train_or_predict 1
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta_Ch_1_1 --seed 2021 --device_num 1 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 10 --learning_rate 5e-5 --gradient_accumulation_steps 1 --type "Ch" --train_or_predict 1
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta_SF_1_1 --seed 2021 --device_num 1 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 10 --learning_rate 5e-5 --gradient_accumulation_steps 1 --type "SF" --train_or_predict 1
#python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta_EF_1_1 --seed 2021 --device_num 0 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 8 --learning_rate 5e-5 --gradient_accumulation_steps 1 --type "EF" --train_or_predict 1
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta_SM_1_1 --seed 2021 --device_num 1 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 10 --learning_rate 5e-5 --gradient_accumulation_steps 1 --type "SM" --train_or_predict 1
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta_Op_1_1 --seed 2021 --device_num 1 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 10 --learning_rate 5e-5 --gradient_accumulation_steps 1 --type "Op" --train_or_predict 1

# predict for test data
python3 train_roberta_model.py --dataset data --num_epochs 100 --model_folder saved_model_roberta --seed 2021 --device_num 1 --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 10 --learning_rate 1e-4 --gradient_accumulation_steps 1 --train_or_predict 2
