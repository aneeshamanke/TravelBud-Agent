import openai
import os

openai.api_key=os.getenv("OPEN_API_KEY")

def get_travel_ideas(interests,budget=None,season=None):
    prompt=f"Suggest 3 travel destinations for someone interested in {interests}"
    if budget:
        prompt+=f"with a budget of {budget}"
    if season:
        prompt+=f"during {season}"
    else:
        prompt+="."
        
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        max_tokens=150,
        temperature=0.8
    )
    
    return response.choices[0].message['content'].strip()

