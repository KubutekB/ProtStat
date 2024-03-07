import os

def join_samples(path):
    total = 1
    for f in os.listdir(path):
        if f.endswith(".fasta"):

            #For some reason it was always throwing permission errors somewhere in the middle of the loop.
            #Forcing it to just try again fixed it - no idea why it was even doing that in the first place
            permissionError = 1
            while permissionError:
                try:
                    with open("total_" + path[:-7] +".fasta", "a") as file:
                        file.write(open(path + "\\" + f).read())
                    permissionError = 0
                except:
                    print("Error " + str(total))
                    total += 1

path_ar = "Archaea_chosen"
path_eu = "Eukaryota_chosen"
path_bac = "Bacteria_chosen"
path_vir = "Viruses_chosen"

join_samples(path_ar)
join_samples(path_eu)
join_samples(path_bac)
join_samples(path_vir)