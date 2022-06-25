body_part_melodys = body_concious_score(accel_leftfoot_melodys,
                               accel_rightfoot_melodys,
                               accel_lefthand_melodys,
                               accel_righthand_melodys,
                               kinect_leftfoot_melodys,
                               kinect_rightfoot_melodys,
                               kinect_lefthand_melodys,
                               kinect_righthand_melodys)

body_part_drums = body_concious_score(accel_leftfoot_drums,
                               accel_rightfoot_drums,
                               accel_lefthand_drums,
                               accel_righthand_drums,
                               kinect_leftfoot_drums,
                               kinect_rightfoot_drums,
                               kinect_lefthand_drums,
                               kinect_righthand_drums)

body_part_vocals = body_concious_score(accel_leftfoot_vocals,
                               accel_rightfoot_vocals,
                               accel_lefthand_vocals,
                               accel_righthand_vocals,
                               kinect_leftfoot_vocals,
                               kinect_rightfoot_vocals,
                               kinect_lefthand_vocals,
                               kinect_righthand_vocals)


body_part_melodys = ideal_vocals
body_part_drums = ideal_melodys
body_part_vocals = ideal_drums


# del_melodys_onset = delete_break_list(melodys_onset)
# del_drums_onset = delete_break_list(drums_onset)
# del_vocals_onset = delete_break_list(vocals_onset)

# del_body_part_melodys = delete_break_list(body_part_melodys)
# del_body_part_drums = delete_break_list(body_part_drums)
# del_body_part_vocals = delete_break_list(body_part_vocals)

# print(sum(del_body_part_drums))

# body_melody_tf_idf = tf_idf(del_melodys_onset,del_body_part_melodys)
# body_drum_tf_idf = tf_idf(del_drums_onset,del_body_part_drums)
# body_vocal_tf_idf = tf_idf(del_vocals_onset,del_body_part_vocals)

# four_counts_body_melody_tf_idf = tf_idf_four_counts(body_melody_tf_idf, 4)
# four_counts_body_drum_tf_idf = tf_idf_four_counts(body_drum_tf_idf, 4)
# four_counts_body_vocal_tf_idf = tf_idf_four_counts(body_vocal_tf_idf, 4)

# body_tf_idf = estimated_concious_of_music_part(four_counts_body_vocal_tf_idf, four_counts_body_melody_tf_idf, four_counts_body_drum_tf_idf)

body_tf_idf = tf_idf(body_part_melodys, body_part_drums, body_part_vocals)
# body_tf_idf = tf_idf(del_body_part_melodys, del_body_part_drums, del_body_part_vocals)
print(body_tf_idf)

tf_idf_concious_part = toshi_accuracy_data
# tf_idf_concious_part = make_concious_part(7, "two")
value_tf_idf_concious_part = part_to_value(tf_idf_concious_part,tf_idf_concious_part)
enl_value_tf_idf_concious_part = enlarge_sentence(value_tf_idf_concious_part,100)
value_tfidf_body_part = part_to_value(body_tf_idf,tf_idf_concious_part)
enl_value_tfidf_body_part = enlarge_sentence(value_tfidf_body_part,100)
# estimated_accuracy(body_tf_idf,tf_idf_concious_part)
# print(value_tfidf_body_part)



toshi_tf_idf = one_dimension_part_to_value(ideal_vocals, ideal_melodys, ideal_drums)
int_toshi_tf_idf = to_int(toshi_tf_idf)