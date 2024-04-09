# Import packages
import google.generativeai as genai
from typing import List, Tuple
import json

# function to call the model to generate
def interact_summarization(model, prompt: str, paper: str, temp = 1.0) -> str:
    '''
      * Arguments

        - prompt: the prompt that we use in this section

        - paper: the article to be summarized

        - temp: the temperature parameter of this model. Temperature is used to control the output of the chatbot.
                The higher the temperature is, the more creative response you will get.
    '''
    input = f"{prompt}\n{paper}"
    response = model.generate_content(
      input,
      generation_config=genai.types.GenerationConfig(temperature=temp),
      safety_settings=[
          {"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_NONE",},
          {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_NONE",},
          {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_NONE",},
          {"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_NONE",},
          ],
      stream = False
    )

    return response.text

def save_result(text: str, fn = "default"):
    
    file = f"results/{fn}.txt"
    with open(file, 'w') as f:
        f.write(text)
    


# Set up Gemini API key
GOOGLE_API_KEY=""
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Check if you have set your Gemini API successfully
try:
    model.generate_content(
      "test",
    )
    print("Set Gemini API sucessfully!!")
except:
    print("There seems to be something wrong with your Gemini API. Please follow our demonstration in the slide to get a correct one.")

prompt_file = "prompts/prompt1.txt"
paper_file = "TXT/2404.02831v1.Empowering_Biomedical_Discovery_with_AI_Agents.txt"
with open(prompt_file, 'r') as f:
    prompt = f.read()
with open(paper_file, 'r') as f:
    paper = f.read()


result = interact_summarization(model, prompt, paper)
save_result(result)