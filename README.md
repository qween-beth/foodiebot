# 🍽️ AI Food Analyzer

Welcome to the **AI Food Analyzer** application, a Streamlit-based app designed to analyze food images using machine learning and generative AI. This app identifies food items from images, provides a nutritional breakdown, and suggests recipes using state-of-the-art AI models.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the App](#running-the-app)
  - [Uploading an Image](#uploading-an-image)
  - [Viewing Results](#viewing-results)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Food Identification**: Predicts the food item in an uploaded image using a fine-tuned MobileNetV2 model.
- **Nutritional Analysis**: Provides a detailed nutritional breakdown of the identified food item.
- **Recipe Suggestions**: Suggests recipes with similar nutritional profiles using Gemini AI.
- **User-Friendly Interface**: Simple, intuitive interface built with Streamlit.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher installed on your system.
- Basic understanding of Python and machine learning.
- Access to a Google Cloud API Key with permissions for Google's Generative AI (Gemini).

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai-food-analyzer.git
   cd ai-food-analyzer
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Pre-trained Model**

   Place the pre-trained MobileNetV2 model (`fine_tuned_mobilenet_v2.h5`) in the root directory of the project.

## Usage

### Running the App

To start the Streamlit app, run the following command in your terminal:

```bash
streamlit run app.py
```

This command will launch the application in your default web browser.

### Uploading an Image

1. **Enter Your Gemini API Key**: In the text field provided, input your Gemini API key. This key is necessary to access Google's Generative AI services.

2. **Upload an Image**: Click on the "Choose an image of food" button to upload a food image (supported formats: `.jpg`, `.jpeg`, `.png`).

### Viewing Results

After uploading the image, the app will:

1. Display the uploaded image.
2. Predict the food item using MobileNetV2.
3. Generate a nutritional breakdown and recipe suggestions using Gemini AI.
4. Present the results clearly on the right-hand side of the interface.

## Project Structure

```plaintext
ai-food-analyzer/
│
├── app.py                  # Main Streamlit application
├── fine_tuned_mobilenet_v2.h5  # Pre-trained MobileNetV2 model file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation (this file)
```

## Model Information

### MobileNetV2

- **Purpose**: Identifies food items from images.
- **Training**: Fine-tuned on a dataset of food images with 23 different classes.
- **Input**: Preprocessed 224x224 RGB images.
- **Output**: Predicted food item label.

### Gemini AI

- **Purpose**: Provides nutritional information and recipe suggestions.
- **Model**: Google's Generative AI (Gemini-1.5-flash).
- **Configuration**: Adjustable parameters such as temperature, top_p, and top_k to customize output generation.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your forked repository.
4. Open a pull request, describing the changes you have made.

Please ensure your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Thank you for checking out the AI Food Analyzer! If you have any questions or feedback, feel free to reach out or open an issue on the GitHub repository. Happy coding! 🎉
