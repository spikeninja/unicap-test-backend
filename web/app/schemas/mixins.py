from datetime import datetime
from pydantic import BaseModel


class DateTimeMixin(BaseModel):
    created_at: datetime
    updated_at: datetime
