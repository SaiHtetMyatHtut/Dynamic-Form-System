from fastapi import FastAPI
# Development
from src.databases.setup import Base, engine
from src.routes import form_templates, form_fields, form_responses, form_values

app = FastAPI()
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
app.include_router(form_templates.router, prefix="/form-template", tags=["form-template"])
app.include_router(form_fields.router, prefix="/form-field", tags=["form-field"])
app.include_router(form_responses.router, prefix="/form-response", tags=["form-response"])
app.include_router(form_values.router, prefix="/form-value", tags=["form-value"])

@app.get("/")
def main():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)