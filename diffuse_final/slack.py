import requests
from os.path import splitext
import sys

def send(file) :

	my_file = {
	  'file' : (file, open(file, 'rb'), file.split('/')[-1].split('.')[1])
	}

	payload={
	  "filename":file, 
	  "token":"xoxp-50234857284-50245035351-218969695537-ce2a65eeac99331c0e70ad3fd8bacf93", 
	  "channels":['#general'], 
	}

	r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)

if __name__ == "__main__":
    send(sys.argv[1])
    
