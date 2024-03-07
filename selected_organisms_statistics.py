import matplotlib.pyplot as plt
import os
import re
import sys
import funcs
from prettytable import PrettyTable
import pandas as pd


path = "selected_organisms"
orgs = []

for f in os.listdir(path):
    if f.endswith(".fasta"):
        orgs.append(path + "/" + f)


tables_dir = "tables/"
if not os.path.exists(tables_dir):
    os.makedirs(tables_dir)

#Table 1

orgs_aa_cont = funcs.calc_stat(orgs, funcs.aa_cont)
aminoacids = []

for name in  orgs_aa_cont:
    aminoacids += orgs_aa_cont[name].keys()

aminoacids = list(set(aminoacids))
aminoacids.sort()
table_rows = []

for k in orgs_aa_cont:
    row = [k]
    for a in aminoacids:
        if a not in orgs_aa_cont[k]:
            row.append(0)
        else:
            row.append(orgs_aa_cont[k][a])

    table_rows.append(row)

field_names1 = ["Organism"] + aminoacids
t1 = PrettyTable()
t1.field_names = field_names1

for r in table_rows:
    t1.add_row(r)

with open(tables_dir + "selected_organisms_aa_cont.txt", 'w') as f:
    f.write(t1.get_string())
print(t1)


#Table 2

orgs_lengths = funcs.calc_stat(orgs, funcs.avg_prot_len)

t2 = PrettyTable()
t2.field_names = ["Organism", "Avg protein length"]

for k in orgs_lengths:
    t2.add_row([k,orgs_lengths[k]])

print(t2)
with open(tables_dir + "selected_organisms_avg_prot_len.txt", 'w') as f:
    f.write(t2.get_string())

#Plots
plots_dir = "plots/"
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)


print("Plotting lengths of selected organisms: ")
orgs_lengths = {key.replace(" ", "\n"): value for key, value in orgs_lengths.items()}

n = list(orgs_lengths.keys())
v = list(orgs_lengths.values())
cat = ["Vertebrates","Vertebrates","Bacteria","Invertebrates","Bacteria","Nematoda","Fungi","Vertebrates","Plantae"]

plt.figure(figsize=(16,8))
data = [[n[i], cat[i], v[i]] for i in range(len(n))]
data = pd.DataFrame(data, columns = ['Organism', 'Category', 'Length'])

colors = {'Vertebrates':'red', 'Bacteria':'green', 'Invertebrates': 'black', 'Nematoda': "blue", 'Fungi': 'orange', 'Plantae': 'cyan'}
c = data['Category'].apply(lambda x: colors[x])
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]

plt.legend(handles, labels, loc='upper right')
plt.xlabel("Organism")
plt.ylabel("seq length")
plt.title("Average protein length")
plt.bar(data['Organism'], data['Length'],  color=c, label=colors)
plt.savefig(plots_dir + "selected_organisms_avg_prot_len.png")

orgs_histogram_length_vals = funcs.calc_stat(orgs, funcs.all_lengths)

for i in orgs_histogram_length_vals:
    plt.figure()
    plt.title("Protein lengths of " + i)
    plt.hist(orgs_histogram_length_vals[i],bins=80, edgecolor='black')
    plt.xlabel("prot lengths")
    plt.ylabel("total count")
    i = i.replace("/", "")
    plt.savefig(plots_dir + "histogram_prot_lengths_" + i + ".png")

