import json
from api import create_card,update_card

id_column =  input("Enter ID of column:")
id_labels = input("Enter a comma-seperated list of the label ID(s) you want to add to the card:").split(",")
comment = input("Enter comment to add to card:")

if not id_column:
    print("Please ensure you've properly entered the ID of the column")
    exit()

try:
  create_card_response=create_card.create_card_with_labels(id_column,id_labels)
  print("You have succesfully created your card")
  card_id=json.loads(create_card_response)['id']
  updated_card_json_response=update_card.update_card_with_comment(card_id,comment)
  print("You have succesfully updated your card")
except Exception as e:
   print("An error has occured, did you enter your ID's correctly?")
