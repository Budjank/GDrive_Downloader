#!/usr/bin/python2.7
import requests, argparse, os

parser = argparse.ArgumentParser(description="GDrive Downloader")
parser.add_argument("-v", help="Version", action="version", version="%(prog)s 1 0")
parser.add_argument("-x", help="FileId", dest="gdid")
parser.add_argument("-y", help="Filename", dest="name")
args = parser.parse_args()

def puky(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = getok(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    sare(response, destination)

def getok(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
        
    return None

def sare(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

if __name__ == "__main__":
    #gdid = raw_input("[*] Input Id => ")
    gdid = args.gdid
    file_id = str(gdid)
    #name = raw_input("[*] Filename => ")
    name = args.name
    destination = str(name)
    puky(file_id, destination)
    size = os.path.getsize(name)
    try:
        gblk = "Successfully"
    except:
        gblk = "Failed Gan!!"
    yx = "{: <38}".format(name)
    yy = "{: <38}".format(gdid)
    yz = "{: <38}".format(size)
    print """
    +---------------------------------------------------+
    |                 GDrive Downloader                 |
    +---------------------------------------------------+
    | FileId   : """+yy+""" |
    | Filename : """+yx+""" |
    | FileSize : """+yz+""" |
    +---------------------------------------------------+
    |                    """+gblk+"""                   |
    +---------------------------------------------------+
    """
exit()
