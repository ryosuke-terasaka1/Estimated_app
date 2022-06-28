from domains.entities.music import MusicOnset
from usecases.analysis.music.onset import onset_timing
import librosa

def create_onset(music_onset: MusicOnset):

    # music_onset
    drums_onset = onset_timing("drum", "faded_drums.wav", 1.8)
    vocals_onset = onset_timing("vocal", "faded_vocals.wav", 2.2)
    melodys_onset = onset_timing("melody", "faded_melody.wav", 1.4)