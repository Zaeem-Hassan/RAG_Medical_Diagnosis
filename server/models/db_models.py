from pydantic import BaseModel,Field
from typing import Optional , List
import time
from datetime import datetime

class UserOut(BaseModel):
    username : str
    role : str

class ReportMeta(BaseModel):
    doc_id : str
    filename : str
    uploader : str
    uploaded_at : str

class DiagnosisRecord(BaseModel):
    doc_id : str
    requester : str
    question : str
    answer : str
    sources : Optional[list] = []
    timestamp : float = Field(default_factory=lambda: time.time())