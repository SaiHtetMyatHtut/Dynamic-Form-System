from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.databases.setup import get_db
from src.databases.models import FormValue
from src.schema import form

router = APIRouter()

@router.get("/", response_model=List[form.FormValue])
def read_form_values(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    form_values = db.query(FormValue).offset(skip).limit(limit).all()
    return form_values

@router.post("/", response_model=form.FormValue)
def create_form_value(form_value: form.FormValueCreate, db: Session = Depends(get_db)):
    value = FormValue(
        response_id=form_value.response_id,
        field_id=form_value.field_id,
        value=form_value.value
    )
    db.add(value)
    db.commit()
    db.refresh(value)
    return value

# Add more routes as needed for updating and deleting form values
