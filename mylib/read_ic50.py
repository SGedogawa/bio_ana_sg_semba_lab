from settings import const

import pandas as pd


class IC50_df(object):

    def __init__(self, info, cell_line, ic50df):
        self.drug_name = info.drug_name
        self.tissue = info.tissue
        self.cancer_species = info.cancer_species
        self.cell_line = cell_line
        self.ic50df = ic50df


class CreateDF(object):

    def __init__(self, info):
        self.info = info
        ic50_df = pd.read_csv(const.ic50_data_path + self.info.drug_name + ".csv")
        cell_line = ic50_df['Cell line'].values.tolist()
        l = []
        for i in cell_line:
            new_cell_line = i.replace('-', '')
            new_cell_line = new_cell_line.upper() + '_' + self.info.cancer_species
            l.append(new_cell_line)
        ic50_df['cell_line'] = l
        self.cell_line = ic50_df['cell_line'].values.tolist()
        self.ic50_df = ic50_df

    def to_ic50df(self) -> IC50_df:

        return IC50_df(info=self.info,
                       cell_line=self.cell_line,
                       ic50df=self.ic50_df)
