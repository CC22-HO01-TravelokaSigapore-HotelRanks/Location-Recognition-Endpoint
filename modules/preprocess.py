import re
import numpy as np

def remove_space_start_end(text:str):
  return text.strip()

def lowercase(text:str):
  return text.lower()

def only_alphabets(text:str):
  text = re.sub("[\.]", "", text)
  text = re.sub('[^a-zA-Z]',' ',text) 
  text = re.sub(' (rd|th|st) '," ", text)
  return text

def remove_multiple_space(text:str):
  return " ".join(text.split())

def preprocess_text(text:str) -> str | None:
  text = str(text)
  text = lowercase(text)
  text = only_alphabets(text)
  text = remove_multiple_space(text)
  if len(text.split()) == 0:
    return None
  return text