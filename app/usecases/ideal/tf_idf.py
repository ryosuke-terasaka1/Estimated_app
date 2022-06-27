from app.domains.entities.ideal import IdealData
from app.domains.entities.music import MusicOnset

def one_dimension_tfidf(vocal, melody, drum, start, length, interval):
    v_sum = sum(vocal)
    m_sum = sum(melody)
    d_sum = sum(drum)
    tf_idf_result = []
    end = start + length
    for i in range(start, end, interval):
        v_measure = sum(vocal[i:i + interval])
        v_tfidf = v_measure / v_sum

        m_measure = sum(melody[i:i + interval])
        m_tfidf = m_measure / m_sum

        d_measure = sum(drum[i:i + interval])
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


def ideal_tf_idf_func(dancer: IdealData, onset: MusicOnset):
    ans = []
    for edit_command in onset.edit_command_lists:
        start, length, interval = edit_command[0], edit_command[1], edit_command[2]
        ans += one_dimension_tfidf(dancer.Similarly_vocal, dancer.Similarly_melody, dancer.Similarly_drum, start, length, interval)
    #     ans += one_dimension_tfidf(vocal, melody, drum, 0, 32, 8)
    #     ans += one_dimension_tfidf(vocal, melody, drum, 32, 4, 4)
    if dancer.Csv_data == "app/drivers/input/move/ideal_data/csv_data/uww2021_ideal_data.csv":
        ans = ans[:-3]


    return ans