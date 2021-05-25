# -*- coding: utf-8 -*-
# @Time     : 2021/5/22 14:46
# @Author   : 宁星星
# @Email    : shenzimin0@gmail.com
import json
import os


type_map = {
    "IndexFault": "IF",
    "SoftHardwareFault": "SHF",
    "CollectData": "CD",
    "Check": "Ch",
    "SettingFault": "SF",
    "ExternalFault": "EF",
    "SetMachine": "SM",
    "Operate": "Op"
}

type_map_inv = {v: k for k, v in type_map.items()}

def original_2_train(original_dir_1, target_dir_1, original_dir_2, target_dir_2):
    in_file_1 = open(original_dir_1, 'r', encoding='utf8')
    out_file_1 = open(target_dir_1, 'w', encoding='utf8')
    wrong = 0
    for line in in_file_1:
        line = line.strip()
        line = json.loads(line)
        new_line = dict()
        new_line["id"] = line["doc_id"]
        new_line["content"] = line["text"]
        words_original = line['text']
        new_line["events"] = []
        for event in line["event_list"]:
            trigger = event["trigger"]
            arguments = event["argument"]
            new_event = dict()
            type = type_map[trigger[0]]
            new_event["type"] = type
            mentions = []
            for argument in arguments:
                mention = dict()
                mention["word"] = argument[2]
                entity = argument[2]
                start_span = argument[1]
                end_span = argument[1] + len(argument[2])

                # check有多少标错的实体
                if entity != words_original[start_span:end_span]:
                    # check left
                    slide_dist = 0
                    while entity != words_original[start_span:end_span] and slide_dist < 70 and start_span >= 0 and end_span >= 0:
                        start_span -= 1
                        end_span -= 1
                        slide_dist += 1
                    if entity != words_original[start_span:end_span]:
                        # check right
                        slide_dist = 0
                        start_span = argument[1]
                        end_span = argument[1] + len(argument[2])
                        while entity != words_original[
                                        start_span:end_span] and slide_dist < 70 and start_span >= 0 and end_span >= 0:
                            start_span += 1
                            end_span += 1
                            slide_dist += 1
                        if entity != words_original[start_span:end_span]:
                            start_span = argument[1]
                            end_span = argument[1] + len(argument[2])
                            if entity not in words_original:
                                print(
                                    f'{line["doc_id"]}-[WRONG]-{words_original[start_span:end_span]}-[right]-{mention["word"]}-{start_span}')
                                wrong += 1

                        else:
                            mention["span"] = [start_span, end_span]
                            mention["role"] = argument[0]
                            mentions.append(mention)
                            print(f'slide distance: {slide_dist}')
                    else:
                        mention["span"] = [start_span, end_span]
                        mention["role"] = argument[0]
                        mentions.append(mention)
                        print(f'slide distance: {slide_dist}')

                else:
                    mention["span"] = [start_span, end_span]
                    mention["role"] = argument[0]
                    mentions.append(mention)
            # 加上trigger实体
            mention = dict()
            mention["word"] = trigger[2]
            start = trigger[1]
            end = trigger[1] + len(trigger[2])
            mention["span"] = [start, end]
            mention["role"] = "trigger"
            mentions.append(mention)
            new_event["mentions"] = mentions
            new_line["events"].append(new_event)
        json_obj = json.dumps(new_line, ensure_ascii=False)
        out_file_1.write(json_obj+'\n')

    in_file_2 = open(original_dir_2, 'r', encoding='utf8')
    out_file_2 = open(target_dir_2, 'w', encoding='utf8')
    for line in in_file_2:
        line = line.strip()
        line = json.loads(line)
        new_line = dict()
        new_line["id"] = line["doc_id"]
        new_line["content"] = line["text"]
        json_obj = json.dumps(new_line, ensure_ascii=False)
        out_file_2.write(json_obj + '\n')
    print(f'WRONG NUM: {wrong}')

def valid_2_submit(original, target):
    in_file_1 = open(original, 'r', encoding='utf8')
    out_file_1 = open(target, 'w', encoding='utf8')
    for line in in_file_1:
        line = line.strip()
        line = json.loads(line)
        new_line = dict()
        new_line["doc_id"] = line["id"]
        new_line["event_list"] = []
        for event in line["events"]:
            trigger_type = type_map_inv[event["type"]]
            new_event = {"trigger": [trigger_type, 0, ""], "argument": []}  # TODO 这里对于没找到的trigger可以用训练集出现的列表来匹配

            for mention in event["mentions"]:
                word = mention["word"]
                start = mention["span"][0]
                role = mention["role"]

                if role == "trigger":
                    argument_new = [trigger_type, start, word]
                    new_event["trigger"] = argument_new
                else:
                    argument_new = [role, start, word]
                    new_event["argument"].append(argument_new)
            new_line["event_list"].append(new_event)
        json_obj = json.dumps(new_line, ensure_ascii=False)
        out_file_1.write(json_obj + '\n')


if __name__ == '__main__':
    # train_original_dir = '../data/train/train.json'
    # valid_original_dir = '../data/dev/valid.json'
    #
    # train_fix_dir = '../data/train_fix/train.json'
    # valid_fix_dir = '../data/dev_fix/valid.json'
    # # os.mkdir('../data/train_fix')
    # # os.mkdir('../data/dev_fix')
    # original_2_train(train_original_dir, train_fix_dir, valid_original_dir, valid_fix_dir)
    submit_origin_dir = '../result.txt'
    submit_fix_dir = '../result_fix.txt'
    valid_2_submit(submit_origin_dir, submit_fix_dir)