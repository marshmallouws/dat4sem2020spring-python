#Write a module webget.py that exposes a function to download a file from the web in case 
# it does not exist locally already. The function shall have the following signature 
# download(url, to=None) where the keyword argument to specifies where to save a file locally and with which name. 
# If to == None then the file shall be saved in the current working directory ./ with the same name as it has at its origin. 
# For example, calling your program as in the following

#import webget

#url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
#webget.download(url)
#will download the remote file to ./befkbhalderstatkode.csv.

#Likely, you will need functions from the standard library modules os, and urllib. For example, read the doc strings 
# for the following functions and implement the given function stub with help of them.

#os.path.isfile
#os.path.join
#os.path.basename?
#urllib.parse?
#urllib.request.urlretrieve?
#import os
#import urllib.request as req
#from urllib.parse import urlparse
import os.path
import urllib.parse
import urllib.request
import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
    """Download a remote file specified by a URL to a 
    local directory.

    :param url: str
        URL pointing to a remote file.
        
    :param to: str
        Local path, absolute or relative, with a filename 
        to the file storing the contents of the remote file.
    """
    with req.urlopen(url) as response:
        data = response.readlines()

    filename = os.path.basename(url)
    if to is not None:
        filename = to
    with open(filename, 'wb') as f:
        f.writelines(data)

if __name__ == "__main__":
    url = 'https://admin.opendata.dk/dataset/0cd08120-3fb4-4ab9-8b8b-2817ca190e2f/resource/6c5badab-8d8d-40cc-a382-50bdcfb77317/download/udlansdatacodes.csv'
    download(url, './my_modules/petererdejlig.csv')