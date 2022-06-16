OCR with OpenCV and Tesseract
=============================

This Python script utilizes OpenCV and Tesseract OCR to detect and extract text from images. It overlays bounding boxes around detected text regions and displays the result in a window using OpenCV.

Installation
------------

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. Install the required dependencies  
``` bash
    pip install pytesseract opencv-python
```

3. Clone the repository

```bash  
    git clone https://github.com/yactam/text_recogntion.git
```    

Usage
-----

1.  Place your image file in the same directory as the script or provide the correct path to the image file in the script.
    
2.  Run the script
```bash
  python main.py
```
    
3. The script will display the image with bounding boxes around detected text regions. Press 'q' to quit and close the window.
    

Dependencies
------------

*   pytesseract: Python wrapper for Google's Tesseract-OCR Engine.
    
*   opencv-python: OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.
