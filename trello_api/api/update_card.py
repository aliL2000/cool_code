import requests
import json
from assets import info

#This method accepts the id of the card, and the comment (by default, an empty string is given)
def update_card_with_comment(id,comment=" "):
  #Ensure a non-emptry string is given to the API (causes error's otherwise)
  comment = " " if len(comment)<1 else comment
  #Code is derived from:
  #https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-actions-comments-post
  url = "https://api.trello.com/1/cards/"+id+"/actions/comments"
  headers = {
    "Accept": "application/json"
  }

  query = {
    'text': comment,
    'key': info.APIKEY,
    'token': info.APITOKEN
  }

  response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
  )
  
  return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
