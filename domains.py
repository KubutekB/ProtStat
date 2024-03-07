import matplotlib.pyplot as plt
import os
import re
import sys
import funcs
from prettytable import PrettyTable
import pandas as pd


domain_files = ["total_Archaea.fasta", "total_Bacteria.fasta","total_Eukaryota.fasta","total_Viruses.fasta"]

tables_dir = "tables/"
if not os.path.exists(tables_dir):
    os.makedirs(tables_dir)

#Table 1

domains_aa_cont = funcs.calc_stat_domain(domain_files, funcs.aa_cont)
aminoacids = []
for name in  domains_aa_cont:
    aminoacids += domains_aa_cont[name].keys()

aminoacids = list(set(aminoacids))
aminoacids.sort()
table_rows = []

for k in domains_aa_cont:
    row = [k]
    for a in aminoacids:
        if a not in domains_aa_cont[k]:
            row.append(0)
        else:
            row.append(domains_aa_cont[k][a])

    table_rows.append(row)

field_names1 = ["Domain"] + aminoacids
t1 = PrettyTable()
t1.field_names = field_names1

for r in table_rows:
    t1.add_row(r)

with open(tables_dir + "domains_aa_cont.txt", 'w') as f:
    f.write(t1.get_string())
print(t1)


#Table 2

domains_lengths = funcs.calc_stat_domain(domain_files, funcs.avg_prot_len)

t2 = PrettyTable()
t2.field_names = ["Domain", "Avg protein length"]

for k in domains_lengths:
    t2.add_row([k, domains_lengths[k]])

print(t2)
with open(tables_dir + "domains_avg_prot_len.txt", 'w') as f:
    f.write(t2.get_string())

#Plots
plots_dir = "plots/"
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)


print("Plotting lengths of domains: ")
domains = ["Archaea", "Bacteria", "Eukaryota", "Viruses"]
bar_all_domains = [funcs.avg_prot_len(i) for i in domain_files]
plt.figure(figsize=(16,8))
plt.title("Average protein length")
plt.bar(range(len(bar_all_domains)), bar_all_domains, tick_label=domains)
plt.savefig(plots_dir + "domains_avg_prot_len.png")

domains_histogram_length_vals = funcs.calc_stat_domain(domain_files, funcs.all_lengths)

for i in domains_histogram_length_vals:
    plt.figure()
    plt.title("Protein lengths of " + i)
    plt.hist(domains_histogram_length_vals[i],bins=80, edgecolor='black')
    plt.xlabel("prot lengths")
    plt.ylabel("total count")
    plt.savefig(plots_dir + "histogram_prot_lengths_" + i + ".png")

