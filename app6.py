import google.generativeai as genai
genai.configure(api_key="AIzaSyD2vFLALuze7LIfDt1uFuU1bBegrUIUFQY")
for m in genai.list_models():
    print(m.name)