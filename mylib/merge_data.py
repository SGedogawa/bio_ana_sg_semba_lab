from mylib import read_ic50, read_rnaseq, input_info


class TargetInfo(object):

    def __init__(self, info, cell_line, rnaseq_df, ic50_df):
        self.drug_name = info.drug_name
        self.tissue = info.tissue
        self.cancer_species = info.cancer_species
        self.gene_id = info.gene_id
        self.cell_line = cell_line
        self.rnaseq_df = rnaseq_df
        self.ic50_df = ic50_df


class CreateDF(object):

    def __init__(self):
        self.info = input_info.input_info()

        self.rnaseq_df = read_rnaseq.CreateDF(info=self.info).to_rnaseq_df()
        self.ic50_df = read_ic50.CreateDF(info=self.info).to_ic50df()

    def get_cell_line(self):
        cell_line = []
        for i in self.rnaseq_df.cell_line:
            if (i in self.ic50_df.cell_line) is True:
                cell_line.append(i)
        return cell_line

    def to_target_info(self) -> TargetInfo:
        cell_line = self.get_cell_line()
        rnaseq_df = self.rnaseq_df.rnaseq_df.loc[:, cell_line]

        ic50_df = self.ic50_df.ic50df[['cell_line', 'IC50', 'AUC']]
        ic50_df = ic50_df[ic50_df['cell_line'].isin(cell_line)]
        ic50_df = ic50_df.sort_values('cell_line')

        return TargetInfo(info=self.info,
                          cell_line=cell_line,
                          rnaseq_df=rnaseq_df,
                          ic50_df=ic50_df
                          )
