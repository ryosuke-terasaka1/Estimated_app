from typing import List
import itertools

part_list = ['ボーカル', 'メロディ', 'ドラム']
num_list = [0, 1]
key_list = []
value_list = {}
rule_num_list = [0, 1, 2]
to_int_dic = {'ボーカル': 3, 'メロディ': 2, 'ドラム': 1, 'None': 0}
accuracy_list = [2,2,2,2,2,2,2,1,1,1,1,1,1,1,3,3,3,3,3,3,3]

for i, j, k in itertools.product(num_list, num_list, num_list):
    value_list[(i, j, k)] = ""
    key_list.append((i, j, k))

def create_rule(vocal: List(int), melody: List(int), drum: List(int)) -> List(str):
    max_accuracy = [0, 0, 0]
    max_list = [[], [], []]
    rule_length_list = [(0, 168, 8)]

    for a,b,c,d,e,f,g,h in itertools.product(part_list, part_list, part_list, part_list, part_list, part_list, part_list, part_list):
        for priority_rank in itertools.permutations(part_list, 3):
            part_result = []
            tmp_result = []
            score = 0
            rule_list = [a,b,c,d,e,f,g,h]
            for i in range(len(rule_list)):
                value_list[key_list[i]] = rule_list[i]
            for vo, me, dr in zip(vocal, melody, drum):
                part_result.append(value_list[(vo, me, dr)])
            
            for start, length, interval in rule_length_list:
                end = start + length
                for i in range(start, end, interval):
                    v_measure = part_result[i:i+interval].count('ボーカル')
                    
                    m_measure = part_result[i:i+interval].count('メロディ')
                    
                    d_measure = part_result[i:i+interval].count('ドラム')
                    
                    max_num = max(v_measure, m_measure, d_measure)
                    
                    rule_base_list = []
                    
                    if max_num == 0:
                        rule_base_list.append('None')
                    
                    else:   
                        if m_measure == max_num:
                            rule_base_list.append('メロディ')
                        if v_measure == max_num:
                            rule_base_list.append('ボーカル')
                        if d_measure == max_num:
                            rule_base_list.append('ドラム')

                    if len(rule_base_list) >= 2:
                        if priority_rank[0] in rule_base_list:
                            rule_base_list = priority_rank[0]
                        elif priority_rank[1] in rule_base_list:
                            rule_base_list = priority_rank[1]
                        elif priority_rank[2] in rule_base_list:
                            rule_base_list = priority_rank[2]

                    tmp_result.append(to_int_dic[rule_base_list[0]])
            for tmp, acc in zip(tmp_result, accuracy_list):
                if tmp == acc: score += 1

            tmp_accuracy = (score / len(tmp_accuracy)) * 100
            for i in range(len(max_accuracy)):
                if tmp_accuracy > max_accuracy[i]:
                    max_accuracy[i] = tmp_accuracy
                    max_list[i] = [value_list, priority_rank]
                    break

    return max_list, max_accuracy
            
                    

                    
                        

                        
        
            

        





