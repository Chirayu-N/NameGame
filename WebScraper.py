# Runs initially to fill in faces dataset
# Adapted from https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c

import requests
import shutil
import time

url = "https://thispersondoesnotexist.com/image"
r = requests.get(url, stream = True)

n = 5 # Number of faces

for i in range(0, n):
    file_name = f"faces/face{n}.jpg"
    if r.status_code == 200: # Successfully retrieved
        # Set decode_content value to True (otherwise the downloaded image file's size will be zero)
        r.raw.decode_content = True
        with open(file_name,'wb') as f: # open local file (wb)
            shutil.copyfileobj(r.raw, f)
    
