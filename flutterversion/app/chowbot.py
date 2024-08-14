from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
import google.generativeai as genai

# Load the saved fine-tuned model
model = load_model('fine_tuned_mobilenet_v2.h5')

class_labels = {0: 'apple', 1: 'banana', 2: 'beans', 3: 'beef', 4: 'chicken', 5: 'cucumber', 6: 'egg', 7: 'fried_rice', 8: 'goat_meat', 9: 'grape', 10: 'jollof_rice', 11: 'mango', 12: 'noodles', 13: 'orange', 14: 'pawpaw', 15: 'pear', 16: 'pineapple', 17: 'plantain', 18: 'sardine_fish', 19: 'titus_fish', 20: 'turkey', 21: 'white_rice', 22: 'yam'}

def predict_from_image(image_path):
    image = Image.open(image_path)
    img = image.convert('RGB')
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    return class_labels[predicted_class_index]

def analyze_with_gemini(api_key, food_item):
    genai.configure(api_key=api_key)
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
    prompt = f"""
    Analyze the following food item: {food_item}
    1. Provide a detailed nutritional breakdown, including:
       - Calories
       - Macronutrients (carbs, proteins, fats)
       - Key vitamins and minerals
    2. Suggest 3 recipes that incorporate {food_item} or have a similar nutritional profile.
    3. Offer 2-3 health benefits of consuming {food_item}.
    """
    response = model_gemini.generate_content(prompt)
    return response.text
