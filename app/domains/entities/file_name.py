from pydantic import BaseModel

class MusicFile(object):
    name: str
    vocal_name: str
    melody_name: str
    drum_name: str


class DanceFile(object):
    kinect: str
    right_hand: str
    right_foot: str
    left_hand: str
    left_foot: str