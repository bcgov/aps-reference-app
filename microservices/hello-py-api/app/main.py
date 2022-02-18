from fastapi import FastAPI, Depends
from app.auth.gateway import gateway_auth
from app.auth.userinfo import userinfo_auth

app = FastAPI()

@app.get("/")
async def root(userinfo: dict = Depends(userinfo_auth), gateway: dict = Depends(gateway_auth)):
    return {"message": "Hello %s" % userinfo['preferred_username'], "gateway": gateway}

@app.post("/")
async def root(userinfo: dict = Depends(userinfo_auth), gateway: dict = Depends(gateway_auth)):
    return {"message": "Hello %s" % userinfo['preferred_username'], "gateway": gateway}
