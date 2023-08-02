from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List
from src.databases.setup import get_db
from src.databases.models import FormField
from src.schema import form

router = APIRouter()


@router.get("/", response_model=List[form.FormField])
def read_form_fields(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    form_fields = db.query(FormField).offset(skip).limit(limit).all()
    return form_fields


@router.post("/", response_model=form.FormField)
def create_form_field(form_field: Annotated[str, Depends(form.FormFieldCreate)], db: Session = Depends(get_db)):
    field = FormField(
        template_id=form_field.template_id,
        name=form_field.name,
        field_type=form_field.field_type
    )
    db.add(field)
    db.commit()
    db.refresh(field)
    return field

# Add more routes as needed for updating and deleting form fields
