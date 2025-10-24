from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field, validator, EmailStr
from enum import Enum
from typing import Optional, Annotated, Literal
import json
from fastapi.responses import JSONResponse


app = FastAPI()

def load_data():
      with open ('Dic.json','r') as f :
            data = json.load(f)
      return data
def save_data(data):
    with open('Dic.json', 'w') as f:
        json.dump(data, f, indent=2)

class patient(BaseModel):
      id: Annotated [str, Field(...,description="this is patient id field")]
      name: Optional[str] = Field(None, description="this is name field")
      age: Annotated[int , Field(..., description="age field")]
      gender: Annotated[Literal["male","female","other"], Field(...,description="'this is multiple choice field for gender selection")]

@app.post("/create")
def Add_patients(patient: patient):
    #load data
    data = load_data()
    #check if the paitent is in the database
    if patient.id in data:
          raise HTTPException(status_code=400,detail="Data is in the temp DB")
    # if not add the new paitent 
    data[patient.id]=patient.model_dump(exclude=['id'])

    save_data(data)


    return JSONResponse(status_code=200, content={'message':'your data is submitted'})