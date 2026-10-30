import pandas as pd
from sklearn.model_selection import train_test_split

from diabetes_prediction.data.reader import DataReader


class CSVReader(DataReader):

    def __init__(self, file_path, test_size=0.2, random_state=1928):
        self._file_path = file_path
        self._test_size = test_size
        self._random_state = random_state

    def read(self):
        df = self._load()
        return self._split(df)

    def _load(self):
        return pd.read_csv(self._file_path, index_col=0)

    def _split(self, df):
        train_df, test_df = train_test_split(
            df, test_size=self._test_size, random_state=self._random_state
        )
        return train_df, test_df
