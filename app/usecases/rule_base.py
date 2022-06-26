def rule_base(melody, drum, vocal):
    concious_part = []
    for i in range(len(melody)):
#         print(melody[i], drum[i], vocal[i])
        if (melody[i], drum[i], vocal[i]) == (0,0,0):
            concious_part.append("なし")
        elif (melody[i], drum[i], vocal[i]) == (0,1,0):
            concious_part.append("ドラム")
        elif (melody[i], drum[i], vocal[i]) == (0,0,1) or (melody[i], drum[i], vocal[i]) == (0,1,1):
            concious_part.append("ボーカル")
        else:
            concious_part.append("メロディ")

    return concious_part


def one_dimension_rulebase(vocal, melody, drum):
    rule_base_ans = []
    for v, m, d in zip(vocal, melody, drum):
        if m:
            rule_base_ans.append('メロディ')
        elif v:
            rule_base_ans.append('ボーカル')
            
        elif d:
            rule_base_ans.append('ドラム')
            

            
        else:
            rule_base_ans.append('None')
            
    return rule_base_ans

def one_dimension_rulebase_sum(vocal, melody, drum, start, length, interval):
    rule_base_ans = one_dimension_rulebase(vocal, melody, drum)
    rule_base_result = [] 
    end = start + length
    for i in range(start, end, interval):
        v_measure = rule_base_ans[i:i+interval].count('ボーカル')
        
        m_measure = rule_base_ans[i:i+interval].count('メロディ')
        
        d_measure = rule_base_ans[i:i+interval].count('ドラム')
        
        max_num = max(v_measure, m_measure, d_measure)
        
        rule_base_list = []
        
        if max_num == 0:
            rule_base_list.append('None')
        
        else:   
            if m_measure == max_num:
                rule_base_list.append('メロディ')
            elif v_measure == max_num:
                rule_base_list.append('ボーカル')
            elif d_measure == max_num:
                rule_base_list.append('ドラム')

                
#         else:   
#             if v_measure == max_num:
#                 rule_base_list.append('ボーカル')
#             elif d_measure == max_num:
#                 rule_base_list.append('ドラム')
#             elif m_measure == max_num:
#                 rule_base_list.append('メロディ')


        rule_base_result.append(rule_base_list)
#         print(tf_idf_result)
    
    return rule_base_result
    
    
def toshi_rulebase_func(vocal, melody, drum):    
    ans=[]
#     ans += one_dimension_rulebase_sum(vocal, melody, drum, 0, 32, 8)
#     ans += one_dimension_rulebase_sum(vocal, melody, drum, 32, 4, 4)
    ans += one_dimension_rulebase_sum(vocal, melody, drum, 0, music_half_count_length, 8)
    ans = ans[:-3]
    
    
#     ans += one_dimension_rulebase_sum(vocal, melody, drum, 0, 32, 8)
#     ans += one_dimension_rulebase_sum(vocal, melody, drum, 32, 4, 4)
#     ans += one_dimension_rulebase_sum(vocal, melody, drum, 36, music_half_count_length-36, 8)
    return ans
