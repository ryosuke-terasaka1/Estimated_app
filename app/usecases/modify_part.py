def enlarge_sentence(sentence: list, length: int) -> list:
    sentence_list = []
    for i in sentence:
        for _ in range(length):
            sentence_list.append(i)
    return sentence_list

def similarly_score(motion, music):
    plus_point = 1
    minus_point = 0
    score_list = []
    for i in range(len(motion)):
        if motion[i]==1 and music[i]==1:
            score_list.append(plus_point)
        elif motion[i]==0 and music[i]==0:
            score_list.append(0)
        elif motion[i] != music[i]:
            score_list.append(0)
    return score_list

def similary_press_score(motion, music, length):
    score_sentence = similarly_score(motion, music)
    score_sum = 0
    press_score_list = []
    for i in range(len(score_sentence)):
        score_sum += score_sentence[i]
        if i % length == length-1:
            press_score_list.append(score_sum)
            score_sum = 0
    return press_score_list

def estimated_concious_of_music_part(vocals, melody, drums):
#     vocals.insert(0,"ボーカル")
#     melody.insert(0, "メロディ")
#     drums.insert(0, "ドラム")
    estimated_concious_of_music_part = []
    for i in range(len(vocals)):
        max_score_part = []
        max_score = max(vocals[i], melody[i], drums[i])
#         print(max_score)
        if max_score == 0:
            max_score_part.append("なし")
            max_score += 1
        if max_score == vocals[i]:
            max_score_part.append("ボーカル")
        if max_score == melody[i]:
            max_score_part.append("メロディ")
        if max_score == drums[i]:
            max_score_part.append("ドラム")
        estimated_concious_of_music_part.append(max_score_part)
    return estimated_concious_of_music_part

def estimated_accuracy(estimated_concious_of_music_part,concious_of_music_part):
    count_accuracy_part = 0
    for i in range(len(estimated_concious_of_music_part)):
        if len(set(concious_of_music_part[i]) & set(estimated_concious_of_music_part[i]))>0:
            count_accuracy_part += 1
    estimated_accuracy = float(count_accuracy_part* 100 // len(concious_of_music_part) )
    return estimated_accuracy


def make_concious_part(length, dimension):
    concious_part = []
    if dimension == "one":
        vocal = 'ボーカル'
        melody = 'メロディ'
        drum = 'ドラム'
    
    if dimension == "two":
        vocal = ['ボーカル']
        melody = ['メロディ']
        drum = ['ドラム']

    for _ in range(length):
        concious_part.append(melody)
    for _ in range(length):
        concious_part.append(drum)
    for _ in range(length):
        concious_part.append(vocal)
        
    return concious_part


def delete_break_list(part_list):
#     print(part_list[184:])
    copy_part_list = part_list.copy()
    del copy_part_list[184:]
#     print(part_list[120:128])
    del copy_part_list[120:128]
#     print(part_list[56:64])
    del copy_part_list[56:64]
    return copy_part_list

# def delete_break_list(part_list):
# #     print(part_list[184:])
#     copy_part_list = part_list.copy()
#     del copy_part_list[368:]
# #     print(part_list[120:128])
#     del copy_part_list[240:256]
# #     print(part_list[56:64])
#     del copy_part_list[112:128]
#     return copy_part_list


def arrange_list(estimated_concious_of_music_part,concious_of_music_part):
    count_accuracy_part = 0
    for i in range(len(estimated_concious_of_music_part)):
        if len(set(concious_of_music_part[i]) & set(estimated_concious_of_music_part[i]))>0:
            estimated_concious_of_music_part[i] = concious_of_music_part[i]
    return estimated_concious_of_music_part


def part_to_value(estimated_concious_of_music_part,concious_of_music_part):
    part_list = arrange_list(estimated_concious_of_music_part,concious_of_music_part)
    value_list = []
    for i in part_list:
        if i == ['メロディ']:
            value_list.append(1)
        elif i == ['ドラム']:
            value_list.append(2)
        elif i == ['ボーカル']:
            value_list.append(3)
        else:
            value_list.append(0)
    return value_list


def one_dimension_tfidf(vocal, melody, drum, start, length, interval):

    v_sum = sum(vocal)
    m_sum = sum(melody)
    d_sum = sum(drum)
    tf_idf_result = [] 
    end = start + length
    for i in range(start, end, interval):
        v_measure = sum(vocal[i:i+interval])
        v_tfidf = v_measure / v_sum
        
        m_measure = sum(melody[i:i+interval])
        m_tfidf = m_measure / m_sum
        
        d_measure = sum(drum[i:i+interval])
        d_tfidf = d_measure / d_sum
        
        max_num = max(v_tfidf, m_tfidf, d_tfidf)
        
        tf_idf_list = []
        
        if max_num == 0:
            tf_idf_list.append('None')
        
        else:   
            if v_tfidf == max_num:
                tf_idf_list.append('ボーカル')
            if m_tfidf == max_num:
                tf_idf_list.append('メロディ')
            if d_tfidf == max_num:
                tf_idf_list.append('ドラム')

        tf_idf_result.append(tf_idf_list)
#         print(tf_idf_result)
    
    return tf_idf_result
    

def one_dimension_part_to_value(vocal, melody, drum):
    ans=[]
#     ans += one_dimension_tfidf(vocal, melody, drum, 0, 32, 8)
#     ans += one_dimension_tfidf(vocal, melody, drum, 32, 4, 4)
    ans += one_dimension_tfidf(vocal, melody, drum, 0, music_half_count_length, 8)
    ans = ans[:-3]
    
#     ans += one_dimension_tfidf(vocal, melody, drum, 0, 32, 8)
#     ans += one_dimension_tfidf(vocal, melody, drum, 32, 4, 4)
#     ans += one_dimension_tfidf(vocal, melody, drum, 36, music_half_count_length-36, 8)
    return ans


def body_concious_score(alf,arf,alh,arh,klf,krf,klh,krh):
    body_score = []
    for i in range(len(alf)):
        body_score.append(sum([alf[i],arf[i],alh[i],arh[i],klf[i],krf[i],klh[i],krh[i]]))
    return body_score 


def body_concious_part(alf,arf,alh,arh,klf,krf,klh,krh):
    body_concious_part_list = []
    
    for i in range(len(alf)):
        partlist = []
        max_score_part = []
        
        partlist += [alf[i],arf[i],alh[i],arh[i],klf[i],krf[i],klh[i],krh[i]]
        print(partlist)
        count_vocal = partlist.count("ボーカル")
        count_drum = partlist.count("ドラム")        
        count_melody = partlist.count("メロディ")
        count_None = partlist.count("なし")
        
        max_score = max(count_vocal, count_drum, count_melody, count_None)
#         print(max_score)
        if max_score == count_vocal:
            max_score_part.append("ボーカル")
        if max_score == count_melody:
            max_score_part.append("メロディ")
        if max_score == count_drum:
            max_score_part.append("ドラム")
        if max_score == count_None and len(max_score_part) == 0:
            max_score_part.append("なし")
        body_concious_part_list.append(max_score_part)  
    return body_concious_part_list


# def sum_four_counts(partname_list):
#     i = 0
#     body_concious_partname_list = []
#     while i < (len(partname_list)-7):
#             partlist = []
#             max_score_part = []
#             for j in range(8):
#                 partlist.append(partname_list[i + j])
# #             print(partlist)
#             count_vocal = partlist.count(["ボーカル"])
#             count_drum = partlist.count(["ドラム"])        
#             count_melody = partlist.count(["メロディ"])
# #             count_None = partlist.count(["なし"])
# #             print(count_vocal)
#             max_score = max(count_vocal, count_drum, count_melody)
#     #         print(max_score)
#             if max_score == 0:
#                 max_score_part.append("なし")
#             if max_score == count_vocal:
#                 max_score_part.append("ボーカル")
#             if max_score == count_melody:
#                 max_score_part.append("メロディ")
#             if max_score == count_drum:
#                 max_score_part.append("ドラム")
# #             if max_score == count_None and len(max_score_part) == 0:
# #                 max_score_part.append("なし")
#             body_concious_partname_list.append(max_score_part)  
            
#             i += 8
  
#     return body_concious_partname_list

# def sum_four_counts(partname_list):
#     i = 0
#     body_concious_partname_list = []
#     while i < (len(partname_list)-7):
#             partlist = []
#             max_score_part = []
#             for j in range(8):
#                 partlist.append(partname_list[i + j])
# #             print(partlist)
#             count_vocal = partlist.count(["ボーカル"])
#             count_drum = partlist.count(["ドラム"])        
#             count_melody = partlist.count(["メロディ"])
# #             count_None = partlist.count(["なし"])
# #             print(count_vocal)
#             max_score = max(count_vocal, count_drum, count_melody)
#             if max_score == 0:
#                 max_score_part.append("なし")
#             elif max_score == count_melody:
#                 max_score_part.append("メロディ")
# #                 if count_melody == count_vocal or count_melody == drum:
#             elif max_score == count_vocal:
#                 max_score_part.append("ボーカル")
#             elif max_score == count_drum:
#                 max_score_part.append("ドラム")
# #             if max_score == count_None and len(max_score_part) == 0:
# #                 max_score_part.append("なし")
#             body_concious_partname_list.append(max_score_part)  
            
#             i += 8
  
#     return body_concious_partname_list

def sum_four_counts(partname_list):
    i = 0
    body_concious_partname_list = []
    while i < (len(partname_list)-7):
            partlist = []
            max_score_part = []
            for j in range(8):
                partlist.append(partname_list[i + j])
                
            count_vocal = partlist.count(["ボーカル"])
            count_drum = partlist.count(["ドラム"])        
            count_melody = partlist.count(["メロディ"])

            max_score = max(count_vocal, count_drum, count_melody)
            if count_melody >= 2:
                max_score_part.append("メロディ")
            elif count_drum >= 2:
                max_score_part.append("ドラム")
            elif count_vocal >= 2:
                max_score_part.append("ボーカル")
            elif max_score == 0:
                max_score_part.append("なし")
            elif max_score == count_melody:
                max_score_part.append("メロディ")
#                 if count_melody == count_vocal or count_melody == drum:
            elif max_score == count_vocal:
                max_score_part.append("ボーカル")
            elif max_score == count_drum:
                max_score_part.append("ドラム")
#             if max_score == count_None and len(max_score_part) == 0:
#                 max_score_part.append("なし")
            body_concious_partname_list.append(max_score_part)  
            
            i += 8
  
    return body_concious_partname_list


def to_int(parts: list):
    int_list = []
    for part in parts:
        if part == ['ボーカル']:
            int_list.append(3)
        elif part == ['メロディ']:
            int_list.append(2)
        elif part == ['ドラム']:
            int_list.append(1)
        elif part == ['None']:
            int_list.append(0)

    return int_list




