import requests
from io import BytesIO
from PIL import Image

resonse = requests.get(url='https://c-ssl.duitang.com/uploads/item/201606/02/20160602205156_NwG25.jpeg')
img = Image.open(BytesIO(resonse.content))
img.save('../data/a.jpeg')