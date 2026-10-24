from altair import Projection
from pandas import option_context
from pydantic import BaseModel
from typing import  List, Optional

class Developer(BaseModel):
    name: str
    experience: Optional[int] = None

class Project(BaseModel):
    title: str
    decription: Optional[str] = None
    languages: Optional[str] = []
    lead_developer: Developer