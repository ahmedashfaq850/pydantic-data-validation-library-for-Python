from pydantic import BaseModel, field_validator, model_validator, computed_field # type: ignore


class User(BaseModel):
    username: str
    @field_validator('username')
    def username_must_not_contain_underscore(cls, v):
        if '_' in v:
            raise ValueError('Username must not contain underscores')
        return v
    

# If you want to apply the validation on the whole model
class SignUp(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode='before')
    def password_match(cls, values):
        if values['password'] != values['confirm_password']:
            raise ValueError('Passwords do not match')
        return values
    


# If want to add a new field from existing fields which means you are computing a new field
class Product(BaseModel):
    price: float
    quantity: int
    
    @computed_field
    @property
    def total_value(self) -> float:
        return self.price * self.quantity