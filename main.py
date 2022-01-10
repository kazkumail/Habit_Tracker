import requests
from datetime import datetime

TOKEN = "nfnklnfneilnf78278"
USERNAME ="kazkumail786"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph3",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/graph3"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "39"
}

response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
