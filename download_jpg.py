import random
import urllib.request
def download_image(url):
    name = random.randrange(1,10)
    full_name= str(name)+'.jgp'
    return urllib.request.urlretrieve(url,full_name)


download_image('http://www.asciify.net/ascii/thumb/4454/asdasd.png')