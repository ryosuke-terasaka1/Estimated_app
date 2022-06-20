from pydantic import BaseModel
from typing import List

class Music(BaseModel):
    name: str

class MusicOnset(Music):
    drum: List[int]
    vocal: List[int]
    melody: List[int]
