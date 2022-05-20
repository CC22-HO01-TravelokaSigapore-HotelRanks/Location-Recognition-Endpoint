import tensorflow_text as tf_t
import tensorflow as tf

from modules.helper import *
from modules.preprocess import preprocess_text

from fastapi import FastAPI, Response
from pydantic import BaseModel
import uvicorn

# Load a model
model = tf.keras.models.load_model("./saved_model")
vectorizer = model.get_layer("text_vectorization")
vocabulary = vectorizer.get_vocabulary()

# Init API
app = FastAPI()
class RequestText(BaseModel):
    text:str
    
@app.get("/")
async def index():
    return "Hello from location recognition endpoint"

@app.post("/")
async def predict(req: RequestText, response: Response):
    try:
        text = req.text
        text = preprocess_text(text)
        
        if text is None:
            return []
        
        model_prediction = get_prediction(text, model)
        location = post_process_prediction(text, model_prediction, vectorizer, vocabulary)
        
        return location
        
    except Exception as e:
        print(e)
        response.status_code = 500
        return "Internal Server Error"
    
port = 8001
print(f"Listening to http://0.0.0.0:{port}")
uvicorn.run(app, host='0.0.0.0',port=port)
