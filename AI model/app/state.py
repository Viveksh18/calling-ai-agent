from typing import TypedDict, Optional, Literal
from pydantic import BaseModel, Field
from enum import Enum


class Caller_info(BaseModel):
    name: str
    relationship: str
    phone: str
    work: str

class Purpose(BaseModel):
    purpose_category: str
    main_purpose: str
    caller_request: str
    requested_action: str
    important_details: Optional[str] = None

class UrgencyLevel(str, Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Urgency(BaseModel):
    level: UrgencyLevel
    reason: str
    requires_immediate_attention: Literal["True","False"] = False

class Summary(BaseModel):
    summary: str

class CallState(TypedDict):
    conversation: list
    greeting: str
    caller_info: Caller_info
    purpose: Purpose
    urgency: Urgency
    summary: Summary

