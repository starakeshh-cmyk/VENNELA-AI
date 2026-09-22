import google.generativeai as genai

API_KEY = "AQ.Ab8RN6LdQCrUL1PRPaxFddkVwfKWIDaRItWJumwcTHcQj1QBhw"

genai.configure(api_key=API_KEY)

for model in genai.list_models():
    print(model.name)