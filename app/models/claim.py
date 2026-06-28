from pydantic import BaseModel
from typing import Optional


class ClaimSummary(BaseModel):
    patient_name: Optional[str] = None
    hospital_name: Optional[str] = None
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    claim_amount: Optional[str] = None
    admission_date: Optional[str] = None
    discharge_date: Optional[str] = None
    summary: str