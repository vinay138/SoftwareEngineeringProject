import requests

url = "https://api.trello.com/1/boards/tBmYPSYe?fields=id,name,idOrganization,dateLastActivity&lists=open&list_fields=id,name"
url2="https://api.trello.com/1/actions/592f11060f95a3d3d46a987a"
url3="https://api.trello.com/1/boards/560bf4298b3dda300c18d09c?fields=name,url&key={40226b3424f20d50c5726e367398e923}&token={6ac6c6417861cd3ff423020ce6d6949a7b81a463ad79a0deb6a0a49fea643d87}"

response = requests.request("GET", url3)



print(response.text)