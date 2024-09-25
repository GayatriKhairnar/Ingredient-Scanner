# 🍽️ Ingredient Scanner for Dietary Preferences

This is a **Streamlit** web application that allows users to scan ingredient lists of products and check if they meet specific dietary restrictions. The app uses **PaddleOCR** for Optical Character Recognition (OCR) to extract text from images (such as ingredient labels), then checks the extracted ingredients against user-selected dietary preferences. The app highlights ingredients that conflict with the selected preferences and provides visual feedback.

## 📸 Features

- **OCR-based Ingredient Scanning**: Automatically extracts ingredients from a photo taken by your device.
- **Highlight Problematic Ingredients**: Visually highlights any ingredients that do not meet your dietary preferences.
- **Multiple Dietary Preferences**: Supports the following dietary restrictions:
  - Gluten-Free
  - Lactose Intolerant
  - Nut Allergies
  - Shellfish Allergy
  - Egg Allergy
  - Soy Allergy
  - Dairy Allergy
  - Vegetarian
  - Vegan
  - FODMAPs Intolerance
  - Paleo
  - Keto
- **Mobile-Friendly Interface**: Optimized for use on both mobile and desktop devices, with automatic layout adjustments.
- **Dark Mode**: Aesthetic dark theme with readable text and intuitive user interface.

## 🚀 Demo

Check out the [live demo](https://huggingface.co/spaces/Gayatrikh16/ingredient-scanner1) to see the app in action!

## 📂 Project Structure

```bash
.
├── app.py                    # Main Streamlit app
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .streamlit
    └── config.toml           # Streamlit theming and config file
