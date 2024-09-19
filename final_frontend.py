import streamlit as st
from paddleocr import PaddleOCR
import cv2
import numpy as np
#from io import BytesIO

# Initialize PaddleOCR
ocr = PaddleOCR(lang='en')

# Define a function to highlight specific words in an image
def highlight_specific_words(image, boxes, texts, target_words, color=(255, 0, 0), thickness=3):
    for box, text in zip(boxes, texts):
        if any(word.lower() in text.lower() for word in target_words):
            word_box = [tuple(map(int, point)) for point in box]
            cv2.polylines(image, [np.array(word_box)], isClosed=True, color=color, thickness=thickness)
    return image

# Define a function to check if the ingredient list meets dietary preferences and return problematic words
def check_dietary_preference(ingredients, preference):
    if preference == 'Gluten-Free':
        gluten_keywords = ['wheat', 'barley', 'rye', 'oats']
        problematic_words = [word for word in gluten_keywords if any(word in ingredient.lower() for ingredient in ingredients)]
    elif preference == 'Lactose Intolerant':
        lactose_keywords = ['milk', 'lactose', 'cheese', 'butter', 'cream']
        problematic_words = [word for word in lactose_keywords if any(word in ingredient.lower() for ingredient in ingredients)]
    else:
        return True, []
    
    return len(problematic_words) == 0, problematic_words

# Streamlit app
st.title('Ingredient Scanner for Dietary Preferences')

# Camera input
st.write("Capture an image of the ingredient list using your camera:")
camera_image = st.camera_input("Click to take a picture")

if camera_image is not None:
    # Read the image from the camera input
    image = np.array(bytearray(camera_image.read()), dtype=np.uint8)
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Perform OCR
    result = ocr.ocr(img)
    boxes = [res[0] for res in result[0]]
    texts = [res[1][0] for res in result[0]]
    scores = [res[1][1] for res in result[0]]

    # Extract ingredients text
    ingredients_text = ' '.join(texts)
    
    # User dietary preference
    preference = st.selectbox(
        'Select your dietary preference:',
        ['Gluten-Free', 'Lactose Intolerant']
    )
    
    # Check if the ingredients meet the preference and get problematic words
    is_acceptable, problematic_words = check_dietary_preference(texts, preference)
    
    # Highlight problematic words
    highlighted_img = highlight_specific_words(img, boxes, texts, problematic_words)
    
    # Display the image with bounding boxes
    st.image(highlighted_img, caption='Highlighted Ingredients', use_column_width=True)
    
    # Display ingredient text and preference result
    st.write(f"Ingredients detected: {ingredients_text}")
    if is_acceptable:
        st.success(f"The product is suitable for your {preference} preference.")
    else:
        st.error(f"The product is NOT suitable for your {preference} preference.")
        st.write(f"Problematic ingredients: {', '.join(problematic_words)}")
