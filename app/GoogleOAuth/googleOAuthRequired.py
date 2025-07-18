from flask import request,jsonify
from dotenv import load_dotenv
import os
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from functools import wraps 
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("FLASK_SECRET_KEY")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
# print("Google Client Id : ",GOOGLE_CLIENT_ID)
def google_auth_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        try:
            # create google request object 
            request_object = google_requests.Request()
            # get the client tokens
            id_token_from_client=request.get_json()  
            # print(id_token_from_client) 
            # if not exist return with clear message  
            if not id_token_from_client:
                return jsonify({'status':False,"message": "ID token missing"}), 401
            try:
                # verify client tokens by encoding( decoding it to understand object encoded into access_token)
                id_token_from_client=id_token_from_client['tokenId'].encode('utf-8')
                # verify the tokens
                idinfo = id_token.verify_oauth2_token(id_token_from_client,request_object, GOOGLE_CLIENT_ID)
                
                print(idinfo)
                # User Details
                userid = idinfo['sub'] 
                email = idinfo['email']
                name = idinfo.get('name', '')
                picture = idinfo.get('picture', '')
                request.user_data= {
                    'google_id': userid,
                    'email': email,
                    'name': name,
                    'picture': picture,
                    'status':True
                }
            except ValueError as e:
                # print(f"ID token verification failed: {e}")
                return jsonify({'status':False,"message": "Invalid ID token", "error": str(e)}), 401
            except Exception as e:
                # print(f"An unexpected error occurred during verification: {e}")
                return jsonify({'status':False,"message": "Authentication failed", "error": str(e)}), 500
            # return the request to head over to actual function 
            return f(*args, **kwargs)
        except:
              return jsonify({"status":False})
    return decorated_function