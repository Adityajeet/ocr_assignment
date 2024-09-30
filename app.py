import streamlit as st
from ocr import easyocr_ocr
from PIL import Image

st.title("Hindi-English OCR with Keyword Search (EasyOCR)")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    uploaded_file.seek(0)  
    ocr_output = easyocr_ocr(uploaded_file)  

    if ocr_output["status"] == "success":
        extracted_text = ocr_output["extracted_text"]
        

        st.text_area("Extracted Text", extracted_text, height=200)
        st.json(ocr_output)
        
        keyword = st.text_input("Search within the extracted text")
        if keyword:
            st.write("Search Results:")
            results = [line for line in extracted_text.split('\n') if keyword.lower() in line.lower()]
            if results:
                for result in results:
                    st.write(result)
            else:
                st.write("No matching results found.")
    else:
        st.error(f"Error: {ocr_output['message']}")