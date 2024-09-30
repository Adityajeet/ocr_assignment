import easyocr
import numpy as np
from PIL import Image
import io

def easyocr_ocr(image_file):
    img = Image.open(image_file)
    img_array = np.array(img)

    reader = easyocr.Reader(['en', 'hi'])  
    result = reader.readtext(img_array, detail=0)  

    if result:
        return {
            "status": "success",
            "extracted_text": '\n'.join(result)
        }
    else:
        return {
            "status": "error",
            "message": "Could not extract text from the image"
        }