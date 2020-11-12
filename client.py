import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'YOUR ACCOUNT CREDENTIALS'

DIALOGFLOW_PROJECT_ID = 'YOUR PROJECT NAME'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'random'

print("Press 'q' to quit.")
print("########################")

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

while(True):
    text_to_be_analyzed = input('User: ')
    if not text_to_be_analyzed.lower() == 'q': 
        text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
            print('Bot: ' + response.query_result.fulfillment_text)
        except InvalidArgument:
            print("Please give an input or press 'q' to quit..")
    else:
        break
