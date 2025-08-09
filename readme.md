BASIC DETAILS

PROJECT NAME
Hair counter - Automated hair strand detection and counting system

TEAM NAME
The innovators

TEAM MEMBERS
Member1- Esha fathima
Member2- Ahlam salim

PROJECT DESCRIPTION
The hair counter is an image processing based system designed to automatically detect and count the number of hair strands in a given image.

THE PROBLEM
Nobody ever asked for it,but we made it anyway.the world is full of problems.. and counting hair in a picture is not one of them.still, we decided to solve this"problem" no one cares about_ just so you can finally know exactly how many hairs are in that photo you will never look at again.

THE SOLUTION
We built the most unnecessary invention of the century- a hair counter.just upload a photo,and our program will stare at it like a detective,hunting down every single hair strand and counting them for you. why no reason at all.. but now you can finally know there are exactly 347 hairs on your blurry photo. because the world didn't ask for it.. so of corse we made it.

TECHNICAL DETAILS

Technologies or components used
for software:

Languages Used:

HTML – Structure of the upload interface and result display.
CSS – Styling for layout, buttons, and images.
C++ – Backend image processing, hair detection, and JSON response.

Frameworks / Integration:

CGI (Common Gateway Interface) – To connect the browser frontend with the C++ backend executable.

Libraries Used:

OpenCV (C++ backend) – For reading the image, converting to grayscale, noise removal, edge detection (Canny), contour detection, and drawing annotated images.
Base64 Encoding (custom) – To send annotated images as text in JSON.
Standard Template Library (STL) – For strings, vectors, and file handling.

Tools Used:

VS Code – Code writing and debugging.
g++ Compiler – To compile C++ code with OpenCV support (pkg-config --cflags --libs opencv4).
Web Browser – For running and testing the web interface.
pkg-config – For linking OpenCV libraries during compilation.

for hardware:

Web Server Machine (PC/Laptop/Raspberry Pi) – To host the HTML frontend and run the C++ backend.
Camera / Smartphone – To capture high-resolution hair images.
Storage Device – To store the uploaded images temporarily during processing.
Internet / Local Network Connection – For browser-to-server communication.

Implementation
for software:

1. Frontend (HTML, CSS, JavaScript)

HTML: Designed the upload interface with a file input, preview area, and result display section.
CSS: Styled the interface for clean presentation and responsive design.
JavaScript:
Handled image preview before upload.
Sent the selected file to the backend using fetch() and FormData.
Parsed the JSON response from the backend.
Displayed the hair count, annotated image, and raw server data.

2. Backend (C++ with OpenCV)

Multipart Parser: Extracted the uploaded image from HTTP POST requests (multipart/form-data).
Image Processing Steps:
Convert image to grayscale.
Enhance contrast using CLAHE.
Remove noise with fastNlMeansDenoising.
Detect edges using Canny Edge Detection.
Apply morphological closing to join broken edges.
Erode to reduce noise and keep thin structures.
Find contours representing possible hair strands.

Counting Algorithm: Counted only contours above a certain length threshold to reduce false positives.
Annotation: Drew red outlines around detected hairs.
Output: Encoded the annotated image as Base64 and sent JSON with count, annotated_image, and notes.

3. Server-Side Integration

Deployed the backend executable as a CGI script in Apache’s cgi-bin directory.
Configured server to allow execution of CGI programs.
Used correct MIME type (application/json) for responses.

4. Testing and Debugging

Verified uploads worked in multiple browsers.
Adjusted contour thresholds for more accurate counts.
Tested with various image resolutions and lighting conditions.