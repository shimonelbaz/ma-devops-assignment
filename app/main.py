from fastapi import FastAPI, Response
import os
import requests

#os.environ["API_URL"]= "https://api.chucknorris.io/jokes/random"
#os.environ["API_URL"]= "https://uselessfacts.jsph.pl/api/v2/facts/random"
fastapp = FastAPI()


@fastapp.get("/ready")
def is_ready():
    return 200

@fastapp.get("/")
def call_service(raw :str="false"):
    api_call = requests.get(url=os.getenv("API_URL"))
    if raw == "true":
        return Response(status_code=200, content=api_call.text)
    elif raw == "false":
        content = api_call.text
        try:
            content = (api_call.json().get("text") or api_call.json().get("value"))
        except (IndexError, KeyError) as error:
            print(error)
        finally:
            return Response(status_code=api_call.status_code , content=content)
    else:
        return Response(status_code=400, content="Bad Request")