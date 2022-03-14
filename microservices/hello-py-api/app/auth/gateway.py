import os
import jwt
import time
import base64
import traceback
from fastapi import Request
from fastapi import HTTPException

def gateway_auth(request: Request) -> dict:
    try:
        encoded = request.headers['gw-jwt']
        jwt_header = jwt.get_unverified_header(encoded)
        public_key = base64.b64decode(jwt_header['x5c'][0].encode('utf-8') + b"==")
        return jwt.decode(encoded, public_key, algorithms=["RS256"], audience=os.environ.get('AUDIENCE').split(","))
    except:
        traceback.print_exc()
        raise HTTPException(
          status_code=401,
          detail="Access Denied",
          headers={"WWW-Authenticate": "X-Userinfo"})
