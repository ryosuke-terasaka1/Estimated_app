from typing import List, Optional
from pydantic import BaseModel
import pandas as pd


class IdealDataCreate(BaseModel):
    Csv_name: str
    Csv_data: pd.DataFrame
    Similarly_vocal: List[int]
    Similarly_melody: List[int]
    Similarly_drum: List[int]
    
    
class IdealData(IdealDataCreate):
    Accuracy_Part: List[str]
    Rule_base_Concious_Part: List[str]
    Tf_idf_Concious_Part: List[str]

