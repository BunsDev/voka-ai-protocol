import base64

def base64ToImg(id: int, content: str):
    imgdata = base64.b64decode(content)
    
    f = open("../web/assets/covers/{0}.png".format(id), "wb")
    f.write(imgdata)
    f.close()

