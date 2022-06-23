from tokenize import String
from typing import List
from pydantic import BaseModel


class IdealDataCreate(BaseModel):
    Similarly_vocal: List[int]
    Similarly_melody: List[int]
    Similarly_drum: List[int]
    
    
class IdealData(IdealDataCreate):
    Concious_Part: List[String]
