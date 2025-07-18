from flask import Blueprint,request,jsonify
from app.GoogleOAuth.googleOAuthRequired import google_auth_required


route=Blueprint('token',__name__)


@route.route("/google-signin",methods=['POST','GET'])
# Verify client access tokens
@google_auth_required
def google_oauth():
    try:
        # getting the user data after verifying it 
        data=request.user_data
        if data['status']:
            return jsonify(data)
        else:
            return jsonify({'status':False})
        
    except:
        return  jsonify({'status':False})
    