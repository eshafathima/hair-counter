from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import base64
from io import BytesIO

app = Flask(_name_)

def process_image(image_bytes):
    # Read image from bytes
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        return None, "Failed to decode image"

    # Resize if too large
    max_dim = 1024
    h, w = img.shape[:2]
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        img = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_AREA)

    # Grayscale + CLAHE + denoise
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    gray = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)

    # Edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Morph close
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=1)

    # Erode to thin edges
    eroded = cv2.erode(closed, kernel)

    # Find contours
    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Count contours longer than minLen
    minLen = 30
    count = sum(1 for c in contours if len(c) >= minLen)

    # Annotate contours on image (red lines)
    annotated = img.copy()
    for c in contours:
        if len(c) >= minLen:
            cv2.drawContours(annotated, [c], -1, (0,0,255), 1)

    # Encode annotated image to PNG and base64
    _, buffer = cv2.imencode('.png', annotated, [cv2.IMWRITE_PNG_COMPRESSION, 3])
    b64_img = base64.b64encode(buffer).decode('utf-8')

    return {
        "count": count,
        "annotated_image": b64_img,
        "notes": "Estimate based on Canny + contour-length heuristic. Accuracy varies with image quality."
    }, None

@app.route('/')
def index():
    return render_template('index.html')  # Your frontend HTML file

@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    file = request.files['image']
    image_bytes = file.read()
    result, error = process_image(image_bytes)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(result)

if _name_ == '_main_':
    app.run(debug=True)