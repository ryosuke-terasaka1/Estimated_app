from typing import Optional
from pydantic import BaseModel
import pandas as pd

from pydantic import BaseModel
from typing import Optional, List

class DancerBase(object):
    name: Optional[str]
    data: pd.DataFrame
    start_timing: int


class DancerAccel(DancerBase):
    data: pd.DataFrame
    start_timing: int
    right_hand: List[int]
    left_hand: List[int]
    right_foot: List[int]
    left_foot: List[int]

class DancerKinect(DancerBase):
    right_elbow: List[int]
    left_elbow: List[int]
    right_knee: List[int]
    left_knee: List[int]

class DancerSimilarlyCreate(DancerAccel,DancerKinect):
    pass

class DancerSimilarly(DancerSimilarlyCreate):
    rulebase_concious_part: List[int]
    tfidf_concious_part: List[int]
