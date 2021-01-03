from mylib import merge_data

import numpy as np
import scipy.stats


class Calc(object):

    def __init__(self):
        self.info = merge_data.CreateDF().to_target_info()
        self.cell_line = self.info.cell_line
        self.gene_id = self.info.gene_id
        self.rnaseq = self.info.rnaseq_df.values
        self.ic50 = self.info.ic50_df.values

    def calc_cor(self):
        cor_list = np.empty(len(self.gene_id))

        for i in range(len(self.gene_id)):
            auc = self.ic50[:, 2]
            rnaseq = self.rnaseq[i, :]

            res = np.corrcoef(auc.astype(np.float64), rnaseq)
            cor_list[i] = res[0, 1]
        # 0での割り算はnan

        return cor_list

    def calc_zscore(self):
        cor_list = self.calc_cor()
        # nan to 0
        cor_list = np.nan_to_num(cor_list)
        zscore_list = scipy.stats.zscore(cor_list)

        return zscore_list

    def find_r_gene(self, zscore):
        zscore_list = self.calc_zscore()
        gene_list = []
        for i, v in enumerate(zscore_list):
            if v >= zscore:
                gene_list.append(self.gene_id[i])

        return gene_list

    def find_s_gene(self, zscore):
        zscore_list = self.calc_zscore()
        gene_list = []
        for i, v in enumerate(zscore_list):
            if v <= zscore:
                gene_list.append(self.gene_id[i])

        return gene_list
