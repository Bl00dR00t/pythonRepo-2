import requests

url = "https://api.breakingbadquotes.xyz/v1/quotes"

def getInfo(id):
    urlfetch = f"{url}/{id}"
    responseap = requests.get(urlfetch)
    
    if(responseap.status_code==200):
        jsondata = responseap.json()
        return jsondata
    else:
        print(f"Failed to load {responseap.status_code}")
        
charId = input("enter the id for the quote")
charinfo = getInfo(charId)

print(charinfo)

print("https://api.batmanapi.com/v1/characters/1")