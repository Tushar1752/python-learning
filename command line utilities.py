#command line utilities is a module that provides command line utilities for downloading files from the internet.   


import argparse
import requests

def download_file(url,local_name):
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(local_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return local_name

parser=argparse.ArgumentParser()
parser.add_argument("Url",help="Url of file to download")
parser.add_argument("Output",help="by which name do you want to save the file")
args=parser.parse_args()
print(args.Url)
print(args.Output)
print(args.Output,type(args.Output))
download_file(args.Url,args.Output) 