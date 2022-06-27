from app.domains.entities.file_name import MusicFile, DanceFile
from app.domains.entities.music import MusicOnset
from app.domains.entities.ideal import IdealDataCreate

faded = MusicFile()
faded.music = "app/drivers/input/music/data/faded/faded.wav"
faded.drum = "app/drivers/input/music/data/faded/faded_drums.wav"
faded.melody = "app/drivers/input/music/data/faded/faded_melody.wav"
faded.vocal = "app/drivers/input/music/data/faded/faded_vocals.wav"

faded_onset = MusicOnset(faded)
faded_onset.Music_count_length = 90
faded_onset.Offset = 140
faded_onset.Duration = 60

# [start, length, interval]
faded_onset.edit_command_lists = [
    [0, 32, 8],
    [32, 4, 4],
    [36, MusicOnset.Music_half_count_length - 36, 8]
]

toshi_ideal_data = IdealDataCreate()
toshi_ideal_data.Csv_data = "app/drivers/input/move/ideal_data/csv_data/toshi_ideal_data.csv"
