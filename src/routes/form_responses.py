from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List
from src.databases.setup import get_db
from src.databases.models import FormResponse
from src.schema import form

router = APIRouter()


@router.get("/", response_model=List[form.FormResponse])
def read_form_responses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    form_responses = db.query(FormResponse).offset(skip).limit(limit).all()
    return form_responses


@router.post("/", response_model=form.FormResponse)
def create_form_response(form_response: Annotated[str, Depends(form.FormResponseCreate)], db: Session = Depends(get_db)):
    response = FormResponse(template_id=form_response.template_id)
    db.add(response)
    db.commit()
    db.refresh(response)
    return response

# Add more routes as needed for updating and deleting form responses
