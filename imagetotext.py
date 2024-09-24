import streamlit as st
from PIL import Image
import pytesseract

# Function to extract text from an image using pytesseract
def extract_text_from_image(image):
    # Convert image to grayscale for better OCR results
    image = image.convert('L')
    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(image)
    return text

# Streamlit app interface
st.title("Image to Text Converter")

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Open the image using PIL
    image = Image.open(uploaded_image)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text from the image
    with st.spinner("Extracting text..."):
        extracted_text = extract_text_from_image(image)

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(extracted_text)
