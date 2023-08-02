from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum,
    Table,
    UniqueConstraint
)
from sqlalchemy.orm import relationship
from src.databases.setup import Base
import enum


class FieldType(enum.Enum):
    image_url = "image_url"
    text = "text"
    number = "number"
    decimal = "decimal"


# Association table
template_field_association = Table(
    "template_field_association",
    Base.metadata,
    Column("template_id", Integer, ForeignKey("form_templates.id")),
    Column("field_id", Integer, ForeignKey("form_fields.id")),
    UniqueConstraint("template_id", "field_id", name="uix_1")
)


class FormTemplate(Base):
    __tablename__ = "form_templates"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)

    fields = relationship(
        "FormField", secondary=template_field_association, back_populates="template")
    responses = relationship("FormResponse", back_populates="template")


class FormField(Base):
    __tablename__ = "form_fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    field_type = Column(Enum(FieldType), index=True)

    template = relationship(
        "FormTemplate", secondary=template_field_association, back_populates="fields")
    values = relationship("FormValue", back_populates="field")


class FormResponse(Base):
    __tablename__ = "form_responses"

    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("form_templates.id"))

    template = relationship("FormTemplate", back_populates="responses")
    values = relationship("FormValue", back_populates="response")


class FormValue(Base):
    __tablename__ = "form_values"

    id = Column(Integer, primary_key=True, index=True)
    response_id = Column(Integer, ForeignKey("form_responses.id"))
    field_id = Column(Integer, ForeignKey("form_fields.id"))
    value = Column(String)

    field = relationship("FormField", back_populates="values")
    response = relationship("FormResponse", back_populates="values")
