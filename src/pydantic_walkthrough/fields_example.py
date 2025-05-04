from pydantic import BaseModel, Field #type: ignore
from typing import Dict, List, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]
    


class Blog(BaseModel):
    title: str
    content: str
    image: Optional[str] = None
    
    

# Usage of Field

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50, description="The name of the employee")
    department: Optional[str] = 'General'
    salary: float = Field(..., ge = 10000 , le = 200000, description="The salary of the employee")