from typing import List
from fastapi import Depends, FastAPI, APIRouter, HTTPException
from sqlalchemy.orm import Session
from stories import crud, models, schemas
from database.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Story)
def create_story(story: schemas.CreateStory, db: Session = Depends(get_db)):
    return crud.create_story(db=db, story=story)

@router.get("/{story_id}", response_model=schemas.Story)
def read_story(story_id: int, db: Session = Depends(get_db)):
    story = crud.get_story(db, story_id=story_id)
    if story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return story