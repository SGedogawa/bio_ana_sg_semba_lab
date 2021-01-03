from settings import const

import pandas as pd


class Info(object):

    def __init__(self, cancer_species, drug_name, tissue, gene_id):
        self.drug_name = drug_name
        self.tissue = tissue
        self.cancer_species = cancer_species
        self.gene_id = gene_id


def input_info() -> Info:

    cancer_species = "cancer species"
    cancer_species_num = input("cancer species num ? ")
    for k, v in const.species.items():
        if v == int(cancer_species_num):
            cancer_species = k
            break
    if cancer_species == "cancer species":
        print("not found")

    drug_name = input("drug name ? ")
    tissue = input("tissue ? ")

    tpm_df = pd.read_table(const.tpm_data_path)
    gene_id = tpm_df.loc[:, ['gene_id']].values

    return Info(cancer_species=cancer_species,
                drug_name=drug_name,
                tissue=tissue,
                gene_id=gene_id)
