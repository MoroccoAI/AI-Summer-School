from flask import Flask, request, render_template, jsonify
from ocr import *


app = Flask(__name__)

def correspond(drug):
    drug["name"] = drug.pop("Name")
    drug["price"] = drug.pop("PH")
    drug["description"] = ""
    drug["reimbursement"] = drug.pop("TAUX_REMBOURSEMENT")
    return drug
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    files = request.files
    file = files.get('file')
    image_file = request.files.get('image', '')
    drugs = list(ocr(image_file))
    drugs = list(map(correspond, drugs))
    return jsonify(drugs)
