

import json
import base64

data = {}
with open('a_jpge.jpg', mode='rb') as file:
    img = file.read()

data['img'] = base64.b64encode(img)
print(json.dumps(data))