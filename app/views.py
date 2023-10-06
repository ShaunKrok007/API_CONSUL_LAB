from app import app
 
@app.route('/')
def home():
  return "Our Flask application is running!"
