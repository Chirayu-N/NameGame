# Runs initially to fill in faces dataset
# Adapted from https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c

import requests
import shutil
import time

url = "https://thispersondoesnotexist.com/image"

n = 30 # Number of faces

for i in range(n):
    time.sleep(1) # allows time to reload page + avoids repeats
    
    file_name = f"faces/face-{i}.jpg"

    r = requests.get(url, stream = True)
    if r.status_code == 200: # Successfully retrieved
        # Set decode_content value to True (otherwise the downloaded image file's size will be zero)
        r.raw.decode_content = True
        with open(file_name,'wb') as f: # open local file (wb)
            shutil.copyfileobj(r.raw, f)

    