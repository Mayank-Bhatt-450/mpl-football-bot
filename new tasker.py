from bs4 import BeautifulSoup
import requests
x=100
y=100
source = requests.get(f'http://192.168.0.100:1817/?message={x},{y}').text 
print(source) 
