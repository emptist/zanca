import streamlit as st
import numpy as np
import cv2
# this can also be used in swift https://github.com/scott0123/Tesseract-macOS
import pytesseract
import re

# Usage
#image_path = 'path/to/your/image.jpg'
#detect_numbers_on_bricks(image_path)
def detect_numbers_on_bricks(image):
    # Read the image
    #image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to preprocess the image
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    # Perform text extraction
    text = pytesseract.image_to_string(threshold, config='--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789')
        
    # Extract numbers from the text
    numbers = [int(num) for num in re.findall(r'\d+', text)]
    
    # Print extracted numbers
    st.write(f"Detected numbers: {numbers}")
    
    return numbers
    # Print extracted text
    #st.write(f"Detected numbers: {text}")


st.set_page_config(page_title='zancalun',page_icon='dpad.right.filled',layout='centered')

img_file_buffer = st.camera_input(label='Pa',key='taking picture')

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    #st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
    numbers = detect_numbers_on_bricks(cv2_img)
    st.write(numbers)    

