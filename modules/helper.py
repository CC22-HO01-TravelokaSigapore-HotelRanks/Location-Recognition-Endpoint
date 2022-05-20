import numpy as np
from typing import List
import tensorflow as tf


def search_positive_location(prediction: np.ndarray) -> List[int]:
  idx = []
  for i in range(len(prediction)):
    if prediction[i] == 1:
      idx.append(i)
  return idx

def get_prediction(text: str, model: tf.keras.Model) -> np.ndarray:              
    prediction = model.predict([text])[0]
    prediction = tf.math.argmax(prediction, axis=1)
    return prediction

def post_process_prediction(text:str, prediction: np.ndarray, vectorizer, vocabulary) -> List[str]:
    index_location = search_positive_location(prediction)
    vectorized = vectorizer([text])[0]

    attention = []
    for i in index_location:
        attention.append(vectorized[i])
    
    final_list = []
    for i in attention:
        location = vocabulary[i] 
        
        if location == "[UNK]":
            continue
        
        if len(location.strip()) != 0: 
            final_list.append(location)
            
    return final_list