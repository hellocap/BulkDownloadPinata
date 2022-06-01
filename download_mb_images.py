import requests
from PIL import Image

for i in range(1, 6969):
    print(f"Downloading image n°{i}...")
    img_data = requests.get(f"https://midnightbreeze.mypinata.cloud/ipfs/QmVcZrjzmT7CMa2nkgLN5nXVaydxtwPoyUdofNDLwzFTS8/{i}.png").content
    with open(f"{i}.png", 'wb') as handler:
        handler.write(img_data)
    print(f"Image {i} downloaded.")

    #Create an Image Object from an Image
    im = Image.open(f"{i}.png")

    rgb_im = im.convert('RGB')
    rgb_im.save(f"{i}.jpg")

