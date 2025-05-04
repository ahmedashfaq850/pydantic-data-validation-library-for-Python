from pydantic import BaseModel  # type: ignore


class Product(BaseModel):
    name: str
    price: float
    quantity: int
    isFeatured: bool = False
    tags: list[str] = []
    description: str | None = None
    

# consume this validation
def validate_product(product: dict) -> Product:
    return Product(**product)

# Example usage
product = {
    "name": "Laptop",
    "price": 999.99,
    "quantity": 10,
    "isFeatured": True,
    "tags": ["electronics", "computers"],
    "description": "A high-performance laptop."
}
print(validate_product(product))