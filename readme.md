<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />

# Hair Counter  
**Automated Hair Strand Detection and Counting System**

## Team Details
**Team Name:** The Innovators  
**Members:**  
- Esha Fathima  
- Ahlam Salim

## Project Description
The Hair Counter is an image processing system designed to automatically detect and count the number of hair strands in a given image.

## The Problem
Nobody ever asked for it, but we made it anyway. The world is full of problems — and counting hair in a picture isn’t really one of them. Still, we decided to solve this “problem” no one cares about, just so you can finally know exactly how many hairs are in that photo you will never look at again.

## The Solution
We built the most unnecessary invention of the century — a hair counter. Just upload a photo, and our program will stare at it like a detective, hunting down every single hair strand and counting them for you. Why? No reason at all. But now you can finally know there are exactly 347 hairs on your blurry photo. Because the world didn’t ask for it, so of course, we made it.

## Technical Details

### Technologies and Components

#### Software

- **Languages Used:**  
  - HTML (upload interface & result display)  
  - CSS (styling and layout)  
  - C++ (backend image processing, hair detection, JSON response)  

- **Frameworks / Integration:**  
  - CGI (Common Gateway Interface) — connects frontend with C++ backend executable  

- **Libraries:**  
  - OpenCV (C++) — image processing: grayscale, noise removal, edge detection, contour detection, annotation  
  - Base64 Encoding (custom) — encode annotated images for JSON transfer  
  - STL (Standard Template Library) — for strings, vectors, and file handling  

- **Tools:**  
  - VS Code (coding & debugging)  
  - g++ Compiler (compile with OpenCV support)  
  - pkg-config (manage OpenCV linking)  
  - Web Browser (testing frontend)  
#### Hardware
- Web Server Machine (PC/Laptop/Raspberry Pi) — host frontend & run backend  
- Camera / Smartphone — capture high-resolution hair images  
- Storage Device — temporary image storage  
- Internet / Local Network — browser-server communication  

## Implementation

### Software

1. **Frontend (HTML, CSS, JavaScript):**  
   - File upload interface with preview and results display  
   - JavaScript handles image preview, upload via fetch + FormData, parses JSON response, displays count and annotated image  

2. **Backend (C++ with OpenCV):**  
   - Parse multipart/form-data POST to extract image  
   - Process image:  
     - Convert to grayscale  
     - Enhance contrast (CLAHE)  
     - Remove noise (fastNlMeansDenoising)  
     - Edge detection (Canny)  
     - Morphological closing  
     - Erosion to remove noise, preserve hair strands  
     - Contour detection  
   - Count contours longer than threshold to avoid false positives  
   - Annotate image with red outlines on detected hairs  
   - Encode annotated image to Base64  
   - Return JSON with hair count, annotated image, notes  

3. **Server-Side Integration:**  
   - Deploy C++ backend as CGI script on Apache (cgi-bin)  
   - Configure Apache to execute CGI scripts  
   - Set HTTP response MIME type as application/json  

4. **Testing & Debugging:**  
   - Tested on multiple browsers  
   - Tuned thresholds for accurate hair detection  
   - Validated on varied image resolutions and lighting conditions  

## How to Use

1. Open the web interface in a browser.  
2. Upload a hair image using the file input.  
3. Preview the image before submission.  
4. Submit the image and wait for processing.  
5. View the hair count and annotated image results.  

---


