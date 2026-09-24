from pydantic import BaseModel

class  User (BaseModel):
    id: int
    Name: str = "Madhav"
    sign_ts: str | None = None
    isActive:bool
    email:
    
    objUser = User ( id=30 , Name="Madhav")
    print (objUser)