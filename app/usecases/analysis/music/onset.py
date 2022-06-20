def onset_timing(file_name, music_part, threshold):

    mpl.rcParams['axes.xmargin'] = 0
    mpl.rcParams['axes.ymargin'] = 0

    y, sr = librosa.load(music_part, sr=16000, mono=True, offset=offset, duration=duration)  # 演奏時間

    o_env = librosa.onset.onset_strength(y, sr=sr)**threshold  #基準値を設定 
    times = librosa.times_like(o_env, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

    onset_time = np.round(times[onset_frames],decimals=2)

    half_timing = []
    quarter_timing = []
    for _ in range(music_half_count_length):
        half_timing.append(0)
    for _ in range(music_quarter_count_length):
        quarter_timing.append(0)

#     timing 
#     peak_time = []
    for i in onset_time:
        for j in range(1, len(half_count_list)-1):
            if half_count_list[j] <= i < half_count_list[j+1]:
#                 if timing[j] == 1:
#                     continue
#                 else:
                half_timing[j] = 1
#             else:
#                 timing.insert(j, 0)
#     print(timing)
    return half_timing