from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    preferencies: List[str]
    job_list: List[str]

