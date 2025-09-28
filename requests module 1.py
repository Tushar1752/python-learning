#request module is used to make HTTP requests and handle responses 

#get requests module
import requests
response=requests.get("https://www.google.com")
print(response.text)

#example 2:

import requests

url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"Tushar",
    "body":"I am learning requests moddule",
    "userId":1,

}
headers={
    "Content-type":"application/json;charset=UTF-8",

}

response=requests.post(url,headers=headers,json=data)
print(response.text)
print(response.status_code)
print(response.headers)



#Post request


#example 3:
import requests

url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}
data = {
    "username": "my_username",
    "password": "my_password"
}

response = requests.post(url, headers=headers, json=data)

print("Text:", response.text)
print("Status Code:", response.status_code)
print("Headers:", response.headers)
print("JSON:", response.json())



#example 4:



import requests

url="https://api.example.com/login"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like GEcko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type":"application/json"
  }
data={
    "username":"my username",
    "password":"my password",

}
response=requests.post(url,headers=headers,json=data)
print(response.text)
print(response.status_code)
print(response.headers)
print(response.json())  #if response is in json format
