# def tf_idf(music_onset, body_music_part):
#     all_one_count = sum(music_onset)
#     tf_list = []
#     one_count = 0
#     tf_idf = []
#     body_music_list = []
#     body_music_lists = []
#     result = []
#     i = 0
#     while i < len(music_onset)-1:
#         onset_small_list = []
#         for j in range(2):
#             onset_small_list.append(music_onset[i + j])
#             body_music_list.append(body_music_part[i + j])
#         tf = float(sum(onset_small_list) / 2)
#         part_sum = float(sum(body_music_list) / 2)
#         if tf > 0:
#             one_count += 1
#         tf_list.append(tf)
#         body_music_lists.append(part_sum)
#         i += 2
#     idf = math.log(float(len(tf_list) / one_count)) + 1
#     print(idf)
#     [tf_idf.append(tf_value*idf) for tf_value in tf_list]
    
#     for n in range(len(tf_idf)):
#         result.append(float(tf_idf[n] * body_music_lists[n]))
    
#     return result

def tf_idf(body_part_melodys, body_part_drums, body_part_vocals):
    melody_idf = sum(body_part_melodys)
    drum_idf = sum(body_part_drums)
    vocal_idf = sum(body_part_vocals)
    tfidf_part = []
    
    i = 0
    while i < (len(body_part_melodys)-7):
        tf = 0
        melody_tf = 0
        drum_tf = 0
        vocal_tf = 0
        max_score_part = []
        for j in range(8):
            melody_tf += body_part_melodys[i + j]
            drum_tf += body_part_drums[i + j]
            vocal_tf += body_part_vocals[i + j]

        melody_tfidf = float(melody_tf / melody_idf)
        drum_tfidf = float(drum_tf / drum_idf)
        vocal_tfidf = float(vocal_tf / vocal_idf)

        max_score = max(melody_tfidf, drum_tfidf, vocal_tfidf)
#             print(max_score)
        if max_score == 0:
            max_score_part.append("なし")
        elif max_score == vocal_tfidf:
            max_score_part.append("ボーカル")
        elif max_score == melody_tfidf:
            max_score_part.append("メロディ")
        elif max_score == drum_tfidf:
            max_score_part.append("ドラム")
        
        tfidf_part.append(max_score_part)
        i += 8
        
    return tfidf_part
    
    
    


def tf_idf_four_counts(partvalue_list, length):
    i = 0
    four_counts_partvalue_list = []
    while i < (len(partvalue_list)-length+1):
            partlist = []
            sum_score = 0
            for j in range(length):
                sum_score += partvalue_list[i + j]
            four_counts_partvalue_list.append(sum_score)
            i += length
  
    return four_counts_partvalue_lis