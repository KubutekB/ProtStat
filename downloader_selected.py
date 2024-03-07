import requests
import re
import random
import os
import sys
import gzip

url_main = "https://ftp.uniprot.org/pub/databases/uniprot/knowledgebase/reference_proteomes/"
Eukaryota = ["UP000000437","UP000000589", "UP000000803","UP000001940","UP000002311","UP000005640","UP000006548"]
Bacteria = ["UP000000625", "UP000001570"]
directory = "selected_ogranisms/"
if not os.path.exists(directory):
    os.makedirs(directory)

for e in Eukaryota:
    url = url_main + "Eukaryota/" + e + "/"
    response = requests.get(url)
    download_link = url + re.search(r"UP[\d_]*.fasta.gz", response.text).group()
    sample = requests.get(download_link)
    with open(directory + url[-12:-1] + ".zip", 'wb') as file:
        file.write(sample.content)

for b in Bacteria:
    url = url_main + "Bacteria/" + b + "/"
    response = requests.get(url)
    download_link = url + re.search(r"UP[\d_]*.fasta.gz", response.text).group()
    sample = requests.get(download_link)
    with open(directory + url[-12:-1] + ".zip", 'wb') as file:
        file.write(sample.content)


for filename in os.listdir(directory):

    if filename.endswith(".zip"):
        file = os.path.join(directory, filename)

        with gzip.open(file, 'rt') as gz_file:
            content = gz_file.read()

        path_to_save = filename.replace(".zip", ".fasta")
        #print(path_to_save)

        with open(directory + path_to_save, 'w') as output_file:
            output_file.write(content)
            print(f"Extracted to  {directory + path_to_save}")