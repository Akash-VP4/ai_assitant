import requests

data = requests.get("https://docs.langchain.com/llms.txt")
print("this is working",data.content[0])
