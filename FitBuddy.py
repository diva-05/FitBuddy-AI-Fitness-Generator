!pip install -q google-generativeai

import google.generativeai as genai

# உங்கள் Gemini API Key-ஐ இங்கே கொடுக்கவும்
API_KEY = "YOUR_API_KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")

print("=== FitBuddy: AI Fitness Plan Generator ===")
age = input("Enter Age: ")
weight = input("Enter Weight in kg: ")
height = input("Enter Height in cm: ")
goal = input("Fitness Goal (Weight Loss / Muscle Gain): ")
diet = input("Diet Preference (Veg / Non-Veg): ")

prompt = f"""
Create a customized workout and diet plan for:
- Age: {age}
- Weight: {weight} kg
- Height: {height} cm
- Goal: {goal}
- Food Preference: {diet}

Please include a 7-day workout plan and daily meal suggestion (Breakfast, Lunch, Dinner).
"""

response = model.generate_content(prompt)
print("\n=== Your AI Generated Fitness & Diet Plan ===\n")
print(response.text)
