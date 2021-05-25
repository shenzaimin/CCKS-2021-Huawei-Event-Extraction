# -*- coding: utf-8 -*-
# @Time     : 2021/5/22 11:08
# @Author   : 宁星星
# @Email    : shenzimin0@gmail.com
import os
import json
import copy


fix_file_dir = '../data/train/train_fix.json'
# os.mkdir('../data/train_fix')

wrong = 0
file = '../data/train/train.json'
print("Reading file: " + file)
in_file = open(file, 'r', encoding='utf-8')
out_file = open(fix_file_dir, 'w+', encoding='utf-8')
for line in in_file:
    line = line.strip()
    line = json.loads(line)
    words_original = line['text']
    idx_original = line['doc_id']
    new_event_list = copy.deepcopy(line['event_list'])
    for mention in line['event_list']:
        start_span = mention['start']
        end_span = mention['end'] + 1
        role = mention['type']
        entity = mention['entity']
        # check有多少标错的实体
        if entity != words_original[start_span:end_span]:
            # check left
            slide_dist = 0
            while entity != words_original[start_span:end_span] and slide_dist < 70:
                start_span -= 1
                end_span -= 1
                slide_dist += 1
            if entity != words_original[start_span:end_span]:
                # check right
                slide_dist = 0
                start_span = mention['start']
                end_span = mention['end'] + 1
                while entity != words_original[
                                     start_span:end_span] and slide_dist < 70:
                    start_span += 1
                    end_span += 1
                    slide_dist += 1
                if entity != words_original[start_span:end_span]:
                    start_span = mention['start']
                    end_span = mention['end'] + 1
                    print(
                        f'{idx_original}-[WRONG]-{words_original[start_span:end_span]}-[right]-{mention["entity"]}-{start_span}')
                    wrong += 1
                    new_attributes.remove(mention)
                    new_mention = {'start': start_span, 'type': mention['type'],
                                   'end': end_span - 1, 'entity': words_original[start_span:end_span]}
                    new_attributes.append(new_mention)
                else:
                    new_attributes.remove(mention)
                    new_mention = {'start': start_span, 'type': mention['type'],
                                   'end': end_span - 1, 'entity': mention['entity']}
                    new_attributes.append(new_mention)
                    print(f'slide distance: {slide_dist}')
            else:
                new_attributes.remove(mention)
                new_mention = {'start': start_span, 'type': mention['type'],
                               'end': end_span - 1, 'entity': mention['entity']}
                new_attributes.append(new_mention)
                print(f'slide distance: {slide_dist}')
    line['attributes'] = new_attributes
    json_obj = json.dumps(line, ensure_ascii=False)
    out_file.write(json_obj+'\n')
