import librosa
import librosa.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from domains.entities.music import MusicOnset




def onset_timing(music_onset: MusicOnset, music_part, threshold):
    y, sr = librosa.load(music_onset.name)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    half_count = float(30/tempo)
    quarter_count = float(15/tempo)
    half_count_list = []
    quarter_count_list = []
    for i in range(music_onset.Music_half_count_length):
        half_count_list.append(i * half_count)
        
    for l in range(music_onset.Music_quarter_count_length):
        quarter_count_list.append(l * quarter_count)
    mpl.rcParams['axes.ymargin'] = 0

    y, sr = librosa.load(music_part, sr=16000, mono=True, offset=music_onset.Offset, duration=music_onset.Duration)  # 演奏時間

    o_env = librosa.onset.onset_strength(y, sr=sr)**threshold  #基準値を設定 
    times = librosa.times_like(o_env, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

    onset_time = np.round(times[onset_frames],decimals=2)

    half_timing = []
    quarter_timing = []
    for _ in range(music_onset.Music_half_count_length):
        half_timing.append(0)
    for _ in range(music_onset.Music_quarter_count_length):
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