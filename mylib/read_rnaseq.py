from settings import const

import pandas as pd


class RNAseq_df(object):

    def __init__(self, info, cell_line, rnaseq_df):
        self.drug_name = info.drug_name
        self.tissue = info.tissue
        self.cancer_species = info.cancer_species
        self.cell_line = cell_line
        self.rnaseq_df = rnaseq_df


class CreateDF(object):

    def __init__(self, info):
        self.info = info
        self.tpm_df = pd.read_table(const.tpm_data_path)
        self.rnaseq_df = self.tpm_df.loc[:, self.tpm_df.columns.str.contains(self.info.cancer_species)]

    def to_rnaseq_df(self) -> RNAseq_df:
        cell_line = self.rnaseq_df.columns.tolist()

        return RNAseq_df(info=self.info,
                         cell_line=cell_line,
                         rnaseq_df=self.rnaseq_df)
