from __future__ import print_function

import json

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)

form_service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Request body for creating a form
NEW_FORM = {
    "info": {
        "title": "Quickstart form",
    }
}

# Request body to add a multiple-choice question
NEW_QUESTION = {
    "requests": [{
        "createItem": {
            "item": {
                "title": "In what year did the United States land a mission on the moon?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "1965"},
                                {"value": "1967"},
                                {"value": "1969"},
                                {"value": "1971"}
                            ],
                            "shuffle": True
                        }
                    }
                },
            },
            "location": {
                "index": 0
            }
        }
    }]
}

# Creates the initial form
# result = form_service.forms().create(body=NEW_FORM).execute()

# Adds the question to the form
# question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

# Prints the result to show the question has been added
# get_result = form_service.forms().get(formId=result["formId"]).execute()

get_info_form_template = form_service.forms().get(formId="1Nfuk6r3GJliXVcJZqNxDPLaBqtzthRueDj8A6SHpYc8").execute()
print(get_info_form_template)
# info = str(get_info_form_template["info"]).replace("[TEMPLATE]", "SNCF TEST").replace("'", '"')
info_title_get = str(get_info_form_template["info"]['title'])

# Request body for creating a form
info_title_send = {
    "info": {
        "title": info_title_get,
    }
}

result = form_service.forms().create(body=info_title_send).execute()
