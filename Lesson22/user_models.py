from pydantic import BaseModel, conint, constr
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = 15
    email: Optional[str] = None

user1 = User(id=2, name="John Doe", email="Johndoe@example.com")
print(user1)
