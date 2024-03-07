import os
import gzip

domains = ["Archaea", "Bacteria", "Eukaryota", "Viruses"]
for k in domains:
    directory = k + "_chosen/"

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




