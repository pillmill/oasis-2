from typing import List

from pydantic import BaseModel
from typing import List
from . import models
from enum import Enum

class Sex(str, Enum):
    female = "female"
    male = "male"
    other = "other"

class MedicalSituation(str, Enum):
    sick = "sick"
    not_sick = "not_sick"
    recovered = "recovered"

class TestSituation(str, Enum):
    positive = "positive"
    negative = "negative"
    not_tested = "not_tested"

class CreateStory(BaseModel):
    age: int
    sex: Sex
    ethnicity: str
    country_of_origin: str
    profession: str
    medical_problems: List[str] = []
    sick: MedicalSituation
    tested: TestSituation

class Story(CreateStory):
    id: int
    class Config:
        orm_mode: True

    @staticmethod
    def from_module(db_story: models.Story):
        return Story(
            id=db_story.id, 
            age=db_story.age, 
            sex=db_story.sex, 
            ethnicity=db_story.ethnicity, 
            country_of_origin=db_story.country_of_origin, 
            profession=db_story.profession, 
            medical_problems=db_story.medical_problems, 
            sick=db_story.sick, 
            tested=db_story.tested
            )