from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List
from src.databases.setup import get_db
from src.databases.models import FormTemplate, FormField
from src.schema import form

router = APIRouter()


@router.get("/", response_model=List[form.FormTemplate])
def read_form_templates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    form_templates = db.query(FormTemplate).offset(skip).limit(limit).all()
    return form_templates


@router.post("/", response_model=form.FormTemplate)
def create_form_template(form_template: form.FormTemplateCreate, db: Session = Depends(get_db)):
    db_form = FormTemplate(
        title=form_template.title,
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    for field in form_template.fields:
        db_field = FormField(
            name=field.name,
            field_type=field.field_type
        )
        db.add(db_field)  
        db.commit()  
        db.refresh(db_field)
    
    
    return db_form
