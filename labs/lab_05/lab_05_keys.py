import requests
import urllib.parse
from config import config as cfg

targetURL = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html"

apiKey = cfg["htmltopdfkey"]
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetURL, 'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl + "?" + parsedparams

response = requests.get(requestUrl)
print (response.status_code)
result =response.content






