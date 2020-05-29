from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from stories import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Story)
def create_story(story: schemas.StoryCreate, db: Session = Depends(get_db)):
    return crud.create_story(db=db, story=story)

@router.get("/{story_id}", response_model=schemas.Story)
def read_story(story_id: int, db: Session = Depends(get_db)):
    story = crud.get_story(db, story_id=story_id)
    if story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return story

@router.get("/{story_id}/symptoms", response_model=List[schemas.Symptom])
def read_story_symptoms(story_id: int, db: Session = Depends(get_db)):
    return crud.get_story_symptoms(db, story_id=story_id)
