"""
from PIL import Image
import base64
import numpy as np
import io
import pytesseract

import cv2 

def ocr_transcribe(img):
  # Load image
  img = Image.open(io.BytesIO(img.read()))
  img = np.array(img)
  # Convert image to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Apply threshold to convert to binary image
  threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

  # Pass the image through pytesseract
  text = pytesseract.image_to_string(threshold_img)

  # Print the extracted text
  return text
"""
from sys import exc_info
import spacy
from fuzzywuzzy import fuzz
from PIL import Image
import cv2
import pytesseract
import json
import pandas as pd
import io
import numpy as np
def read_excel_to_dataframe(file_path):
    try:
        # Read the Excel file into a DataFrame
        print("1")
        df = pd.read_excel(file_path)
        print("2")
        return df
    except Exception as e:
        print(f"Error: {e} ")
        return None
file_path='/'
data_frame=read_excel_to_dataframe("./models/drug.xlsx")
print(data_frame)
nlp = spacy.load("en_core_web_sm")
def ocr_transcribe(img):
  # Load image
  img = Image.open(io.BytesIO(img.read()))
  img = np.array(img)
  #img = cv2.resize(img, (364, 500))
  img = cv2.resize(img, (500, 364))
  # Convert image to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Apply threshold to convert to binary image
  threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

  # Pass the image through pytesseract
  text = pytesseract.image_to_string(threshold_img, lang='fra')

  # Print the extracted text
  return text
l=data_frame['NOM'].tolist()
drug_names = l

def fuzzy_match(text, target_list):
    # Apply fuzzy matching and find the best match
    best_match = None
    best_ratio = 0

    for target in target_list:
        ratio = fuzz.partial_ratio(text.lower(), target.lower())
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = target

    return best_match, best_ratio

def extract_drug_names(text):
    doc = nlp(text)
    extracted_drugs = []

    for ent in doc.ents:
        # Check if the entity label is 'DRUG' and if the entity text is in the drug database
        if ent.label_ == "DRUG" and ent.text.upper() in drug_names:
            extracted_drugs.append(ent.text.upper())
        else:
            # Apply fuzzy matching to handle missing characters in drug names
            best_match, ratio = fuzzy_match(ent.text, drug_names)
            if ratio >= 4:  # You can adjust this threshold as needed
                extracted_drugs.append(best_match)

    return extracted_drugs
def druginfo(drug_names):
  drug_info=[]
  for i in range(len(drug_names)):
    for j in range(len(data_frame['NOM'])):
      
      if drug_names[i]==data_frame['NOM'][j]:
        drug_info.append([data_frame['NOM'][j],data_frame['PH'][j],data_frame['TAUX_REMBOURSEMENT'][j]])
  
  drug_info = pd.DataFrame(drug_info, columns=['Name', 'PH', 'TAUX_REMBOURSEMENT']) 
  result = drug_info.to_json(orient="index")
  parsed = json.loads(result)
  result =parsed.values()

  
 
  #drug_info=drug_info.to_json()
  #drug_info=json.dumps(drug_info)

  return result
def ocr(img):
  text= ocr_transcribe(img)
  
  new_string=""
  for i in text:
   if ord(i) >=97 and ord(i)< 123:

    new_string+=chr(ord(i)-32)
  else:
    new_string+=i
    
  new = ' '.join(new_string.split())
  separated_text = new.replace(' ', ', ')
  separated_text.upper()

  drug_names=extract_drug_names(separated_text)
  result=druginfo(drug_names)
  print(result)
  return result

