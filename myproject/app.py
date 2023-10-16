import slack
import os
from pathlib import Path
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams, ReturnOptions
from dotenv import load_dotenv
from flask import Flask, request


load_dotenv()

app = Flask("WatsonX K8s answerbot")


api_key = os.getenv("GENAI_KEY", None)
api_endpoint = os.getenv("GENAI_API", None)

params = GenerateParams(
    decoding_method="greedy",
    max_new_tokens=150,
    min_new_tokens=50,
    stream=False,
    temperature=0.7,
    top_k=50,
    top_p=1,
    return_options=ReturnOptions(input_text=False, input_tokens=True),
)

creds = Credentials(api_key, api_endpoint)
model = Model("google/flan-ul2", params=params, credentials=creds)

# Q1 = "What is a Kubernetes application?"

# Q2 = "How to create kubernetes secrets?"





client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#testing', text="Welcome to Kubernetes Answerbot")
client.chat_postMessage(channel='#testing', text="How can I help you ...")

# max_questions = 10
# qno = 0
# while qno < max_questions:
#     qno +=1
#     question = input("Enter you question - ")
#     print(f"Q{qno} - {question}")

#     responses = model.generate([question])
#     for response in responses:
#         print(f"Ans: {response.generated_text}")

@app.route('/', methods=['POST'])
def QA():
    data = request.get_json()
    print(data.get('msg'))
    responses = model.generate([data.get('msg')])
    for response in responses:
        return(f"Ans: {response.generated_text}")    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    