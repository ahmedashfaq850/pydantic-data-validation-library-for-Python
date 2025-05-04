from pydantic import BaseModel #type: ignore
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str

class User(BaseModel):
    id: int
    name: str
    address: Address
    

# Self Referencing or Forward Referencing in Pydantic
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None  
    

# Rebuild the model to resolve forward references
Comment.model_rebuild()