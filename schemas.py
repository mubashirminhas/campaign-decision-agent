
from pydantic import BaseModel
from typing import List

class CampaignInput(BaseModel):
    campaign_id: str
    budget: float
    clicks: int
    conversions: int

class CampaignResponse(BaseModel):
    campaign_id: str
    cpc: float
    conversion_rate: float
    action: str
