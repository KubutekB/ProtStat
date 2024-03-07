import requests
import re
import random
import os


#Get urls to all sample proteomes
url = "https://ftp.uniprot.org/pub/databases/uniprot/knowledgebase/reference_proteomes/"
domains = ["Archaea", "Bacteria", "Eukaryota", "Viruses"]
full_proteomes = {}
for k in range(len(domains)):
    response = requests.get(url + domains[k], allow_redirects=True)
    search = re.findall("UP[0-9]*/", response.text)
    full_proteomes[domains[k]] = list(set(search))

print("All sample urls collected")




#Choose a 100 samples from each kingdom
chosen = {}
for k in range(len(domains)):

    total_num_of_samples = len(full_proteomes[domains[k]])
    counter = 100

    if total_num_of_samples < counter:
        counter = total_num_of_samples
        print("Cannot choose 100 samples as there are only " + str(total_num_of_samples))

    taken = []
    chosen[domains[k]] = []

    while counter > 0:
        randomed_num = random.randint(0, total_num_of_samples-1)
        if randomed_num not in taken:
            taken.append(randomed_num)
            counter -= 1
            chosen[domains[k]].append(url + domains[k] + "/" + full_proteomes[domains[k]][randomed_num])
        else:
            pass

print("Random 100 samples chosen")


#Get the fasta files and download them
for k in range(len(domains)):
    counter = 1  #Count the downloads
    for url in chosen[domains[k]]:

        timeout = 1
        while timeout:
            try:
                r = requests.get(url, allow_redirects=True)
                timeout = 0
            except:
                print("Website timed out, retrying...")

        download_link = url + re.search(r"UP[\d_]*.fasta.gz", r.text).group()
        timeout = 1
        while timeout:
            try:
                r2 = requests.get(download_link, allow_redirects=True)
                timeout = 0
            except:
                print("Website timed out, retrying...")

        print(domains[k], counter)
        counter += 1

        directory = domains[k] + "_chosen/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(directory + url[-12:-1] + ".zip", 'wb') as file:
            file.write(r2.content)










