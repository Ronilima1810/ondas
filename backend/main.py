"""API demonstrativa do Wave Control. Nenhuma integração com WMS real."""
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="Wave Control Demo API",version="1.0.0")
class Wave(BaseModel):
    code:str
    channel:str
    orders:int
    units:int
    status:str
    priority:str

DEMO=[
  Wave(code="ONDA-DEMO-001",channel="E-commerce",orders=45,units=430,status="Em separação",priority="Alta"),
  Wave(code="ONDA-DEMO-002",channel="Atacado",orders=18,units=845,status="Aguardando impressão",priority="Média"),
  Wave(code="ONDA-DEMO-003",channel="Marketplace",orders=67,units=302,status="Liberada",priority="Alta"),
]
@app.get("/api/health")
def health():
    return {"ok":True,"mode":"synthetic","connected_to_production":False}
@app.get("/api/waves",response_model=list[Wave])
def waves():
    return DEMO
