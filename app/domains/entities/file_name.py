from pydantic import BaseModel

class MusicFile(BaseModel):
    music: str
    vocal: str
    melody: str
    drum: str


class DanceFile(BaseModel):
    kinect: str
    right_hand: str
    right_foot: str
    left_hand: str
    left_foot: str