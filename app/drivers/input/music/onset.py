from app.domains.entities.file_name import MusicFile

def create_onset(MusicFile):
    y, sr = librosa.load("faded.wav")
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    half_count = float(30/tempo)
    quarter_count = float(15/tempo)
    half_count_list = []
    quarter_count_list = []
    for i in range(music_half_count_length):
        half_count_list.append(i * half_count)

    for l in range(music_quarter_count_length):
        quarter_count_list.append(l * quarter_count)


    # music_onset
    drums_onset = onset_timing("drum", "faded_drums.wav", 1.8)
    vocals_onset = onset_timing("vocal", "faded_vocals.wav", 2.2)
    melodys_onset = onset_timing("melody", "faded_melody.wav", 1.4)