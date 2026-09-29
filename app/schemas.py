
from pydantic import BaseModel

class Message(BaseModel):
    message: str
    message: str

class AdicionarioUsuario(BaseModel):
    usuario: str
    email: str
    password: str
    idade: int

class ObterUsuario(AdicionarioUsuario):
    codigo: int    
