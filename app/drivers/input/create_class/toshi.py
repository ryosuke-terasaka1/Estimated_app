import pandas as pd

from domains.entities.file_name import MusicFile, DanceFile
from domains.entities.music import MusicOnset
from domains.entities.ideal import IdealDataCreate
from drivers.input.move.ideal_data.condition_similarly import get_ideal_data

faded = MusicFile()


faded_onset = MusicOnset()
faded_onset.music = "drivers/input/music/data/faded/faded.wav"
faded_onset.drum = "drivers/input/music/data/faded/faded_drums.wav"
faded_onset.melody = "drivers/input/music/data/faded/faded_melody.wav"
faded_onset.vocal = "drivers/input/music/data/faded/faded_vocals.wav"

faded_onset.Music_count_length = 90
faded_onset.Music_half_count_length = 180
faded_onset.Music_quarter_count_length = 360
faded_onset.Offset = 140
faded_onset.Duration = 60

# [start, length, interval]
faded_onset.edit_command_lists = [
    [0, 32, 8],
    [32, 4, 4],
    [36, faded_onset.Music_half_count_length - 36, 8]
]

toshi_ideal_data = IdealDataCreate()
toshi_ideal_data.Csv_name = "drivers/input/move/ideal_data/csv_data/toshi_ideal_data.csv"
toshi_ideal_data.Csv_data = pd.read_csv(toshi_ideal_data.Csv_name, skiprows=[0,1], header=None, usecols=[9, 10, 11], encoding="cp932")
toshi_ideal_data = get_ideal_data(toshi_ideal_data)

