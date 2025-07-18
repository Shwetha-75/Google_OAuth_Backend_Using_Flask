from app import createApp 
from dotenv import load_dotenv
load_dotenv()
import os 

app=createApp()
# if __name__=='__main__':
#    app.run(port=os.getenv('PORT'),debug=True)
