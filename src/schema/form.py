from pydantic import BaseModel
from src.databases.models import FieldType
from typing import List


class FormFieldBase(BaseModel):
    name: str
    field_type: FieldType


class FormFieldCreate(FormFieldBase):
    pass


class FormField(FormFieldBase):
    id: int
    class Config:
        from_attributes = True


class FormTemplateBase(BaseModel):
    title: str
    fields: List[FormFieldCreate]


class FormTemplateCreate(FormTemplateBase):
    pass


class FormTemplate(FormTemplateBase):
    id: int

    class Config:
        from_attributes = True


class FormResponseBase(BaseModel):
    template_id: int


class FormResponseCreate(FormResponseBase):
    pass


class FormResponse(FormResponseBase):
    id: int

    class Config:
        from_attributes = True


class FormValueBase(BaseModel):
    response_id: int
    field_id: int
    value: str


class FormValueCreate(FormValueBase):
    pass


class FormValue(FormValueBase):
    id: int

    class Config:
        from_attributes = True
