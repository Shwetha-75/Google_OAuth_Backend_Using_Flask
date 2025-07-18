from app import createApp 
from dotenv import load_dotenv
load_dotenv()
from flask_cors import CORS
import os

app=createApp()

CORS(app,supports_credentials=True, origins={r'/*':{"origins":
    [
      os.getenv("API_GATEWAY_URL"),
     os.getenv("API_GATEWAY_URL_CERTIFICATE")
    ]
    }})
# if __name__=='__main__':
#    app.run(port=os.getenv('PORT'),debug=True)
