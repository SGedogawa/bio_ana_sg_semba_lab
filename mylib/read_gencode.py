from settings import const

from gtfparse import read_gtf
import pandas as pd


class GencodeDF(object):

    def __init__(self, df):
        self.gencode_df = df
        self.shape = df.shape


class CreateDF(object):

    def __init__(self, data_path=const.gencode_data_path):
        self.gencode_df = read_gtf(data_path)

    def to_gencode_df(self) -> GencodeDF:

        return GencodeDF(df=self.gencode_df)
