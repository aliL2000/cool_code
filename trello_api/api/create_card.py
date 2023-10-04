import requests
import json
from assets import info

#This method accepts the id of the column on the board, and ID(s) of the label to be added to the card (by default, no labels will be given)
def create_card_with_labels(id,labels=[]):
  #Code is derived from:
  #https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
  url = "https://api.trello.com/1/cards"

  headers = {
    "Accept": "application/json"
  }

  query = {
    'idList': id,
    'key': info.APIKEY,
    'token': info.APITOKEN,
    'idLabels':labels
  }

  response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
  )

  return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
