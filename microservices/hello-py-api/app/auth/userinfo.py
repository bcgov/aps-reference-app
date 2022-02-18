import time
import json
import base64
from typing import Optional
import traceback
from fastapi import FastAPI, HTTPException, Request, Header, Depends
from fastapi.responses import JSONResponse

async def userinfo_auth(request:Request):
    try:
      return json.loads(base64.b64decode(request.headers['X-Userinfo']))
    except:
      traceback.print_exc()
      raise HTTPException(
        status_code=401,
        detail="Access Denied",
        headers={"WWW-Authenticate": "X-Userinfo"})
