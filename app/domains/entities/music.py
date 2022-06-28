from pydantic import BaseModel
from typing import List, Optional
from domains.entities.file_name import MusicFile


class MusicOnset(MusicFile):
    Music_count_length: int  # UWW: 96  toshi: 90
    Music_half_count_length: int
    Music_quarter_count_length: int
    Offset: int  # UWW: 10  toshi: 140
    Duration: int  # UWW: 65  toshi: 60
    drum: List[int]
    vocal: List[int]
    melody: List[int]
    edit_command_lists: Optional[List[List[int]]]  # [[start, end, interval]]

