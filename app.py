import streamlit as st
import google.generativeai as genai
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model

# Load the saved fine-tuned model
model = load_model('fine_tuned_mobilenet_v2.h5')

# Class labels
class_labels = {0: 'apple', 1: 'banana', 2: 'beans', 3: 'beef', 4: 'chicken', 5: 'cucumber', 6: 'egg', 7: 'fried_rice', 8: 'goat_meat', 9: 'grape', 10: 'jollof_rice', 11: 'mango', 12: 'noodles', 13: 'orange', 14: 'pawpaw', 15: 'pear', 16: 'pineapple', 17: 'plantain', 18: 'sardine_fish', 19: 'titus_fish', 20: 'turkey', 21: 'white_rice', 22: 'yam'}

# Streamlit UI
st.set_page_config(page_title="Food Analyzer", layout="wide")
st.title("🍽️ ChowBot | AI Food Analyzer")

# API Key input
api_key = st.text_input("Enter your Gemini API Key", type="password")

if api_key:
    # Configure Gemini AI
    genai.configure(api_key=api_key)

    # Gemini model setup
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
    }

    model_gemini = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    def predict_from_image(image):
        # Ensure image is in RGB format
        img = image.convert('RGB')
        # Resize and preprocess the image
        img = img.resize((224, 224))
        img_array = np.array(img)
        img_array = preprocess_input(img_array)
        img_array = np.expand_dims(img_array, axis=0)
        
        # Make prediction
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions[0])
        food_item = class_labels[predicted_class_index]
        
        return food_item

    def analyze_with_gemini(food_item):
        prompt = f"""
        Analyze the following food item: {food_item}
        1. Provide a detailed nutritional breakdown, including:
           - Calories
           - Macronutrients (carbs, proteins, fats)
           - Key vitamins and minerals
        2. Suggest 3 recipes that incorporate {food_item} or have a similar nutritional profile.
        3. Offer 2-3 health benefits of consuming {food_item}.

        Format the output clearly with headers for each section.
        """
        response = model_gemini.generate_content(prompt)
        return response.text

    st.markdown("""
    This app uses AI to analyze food images. Upload a picture of your meal to get:
    - Identification of food items
    - Nutritional breakdown
    - Recipe suggestions
    - Health benefits
    """)

    uploaded_file = st.file_uploader("Choose an image of food", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        col1, col2 = st.columns(2)

        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=True)

        with col2:
            with st.spinner("Analyzing your meal..."):
                # Predict food item using local model
                predicted_food = predict_from_image(image)
                st.write(f"Predicted food item: {predicted_food}")

                # Analyze with Gemini
                analysis = analyze_with_gemini(predicted_food)

            st.success("Analysis complete!")

        st.markdown("## Analysis Results")
        st.markdown(analysis)

else:
    st.warning("Please enter your Gemini API Key to use the app.")

st.sidebar.header("About")
st.sidebar.info("""
This app uses a local MobileNetV2 model to identify food items and Google's Gemini AI to provide nutritional information, recipe suggestions, and health benefits.
""")

st.sidebar.header("Tips")
st.sidebar.info("""
- Upload clear, well-lit images for best results
- Make sure the food item is centered and visible in the image
- The AI can analyze one food item at a time
""")