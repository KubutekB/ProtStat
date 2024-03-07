# ProtStat
Calculations of basic statistics (avg protein length and aminoacid content) from a proteome dataset (from UniProt)
- from selected organisms (Arabidopsis thaliana, Bacillus subtilis, Caenorhabditidis elegans, Danio rerio, Drosophila melanogaster, Escherichia coli, Mus musculus, Saccharomyces cerevisiae)
- from randomly selected 100 samples from different domains (Eukaryota, Bacteria, Archaea, Viruses)

### Required modules
-requests
-matplotlib
-pandas
-prettytable


### Scripts
- *download_extract_selected_organisms.py*: download and extract proteomes from 8 organisms
- *download_domain_samples.py*: download 100 proteome samples from 4 domains
- *extract_domain_samples.py*: extract downloaded samples
- *join_samples.py*: for each domain join every .fasta file from 100 samples into one big file 
- *selected_organisms_statistics.py / domains_statistics.py*: calculate aminoacid content and average protein lengths from selected organisms / between domains ; make tables and plots
- *funcs.py*: functions for calculating statistics

### Order
-**Selected ogranisms** 

*download_extract_selected_organisms.py* -> *selected_organisms_statistics.py*

-**Domains** 

*download_domain_samples.py* -> *extract_domain_samples.py* -> *join_samples.py* -> *domains_statistics.py*


# Results

### Selected ogranisms

**Tables**

[Aminoacid content table](tables/selected_organisms_aa_cont.txt)

[Average protein length table](tables/selected_organisms_avg_prot_len.txt)

**Plots**

![Avg prot len](plots/selected_organisms_avg_prot_len.png)
![hist_1](plots/histogram_prot_lengths_Arabidopsis.png)
![hist_2](plots/histogram_prot_lengths_Bacillus.png)
![hist_3](plots/histogram_prot_lengths_Caenorhabditis.png)
![hist_4](plots/histogram_prot_lengths_Danio.png)
![hist_5](plots/histogram_prot_lengths_Drosophila.png)
![hist_6](plots/histogram_prot_lengths_Escherichia.png)
![hist_7](plots/histogram_prot_lengths_Homo.png)
![hist_8](plots/histogram_prot_lengths_Mus.png)
![hist_9](plots/histogram_prot_lengths_Saccharomyces.png)

### Domains

**Tables**

[Aminoacid content table](tables/domains_aa_cont.txt)

[Average protein length table](tables/domains_avg_prot_len.txt)

![Avg prot len](plots/domains_avg_prot_len.png)
![hist_10](plots/histogram_prot_lengths_Archaea.png)
![hist_11](plots/histogram_prot_lengths_Bacteria.png)
![hist_12](plots/histogram_prot_lengths_Eukaryota.png)
![hist_13](plots/histogram_prot_lengths_Viruses.png)


