"""Load the diabetes dataset and make a reproducible train/test split."""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


class DiabetesDataLoader:
    """Load a CSV and return train and test dataframes."""

    def __init__(
        self,
        file_path: str | Path,
        test_size: float = 0.2,
        random_state: int = 42,
    ) -> None:
        self._file_path = Path(file_path)
        self._test_size = test_size
        self._random_state = random_state

    def load(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """Read the CSV and return its train and test splits."""
        return self.split(self.read())

    def read(self) -> pd.DataFrame:
        """Read the CSV; its first column is a saved row index."""
        return pd.read_csv(self._file_path, index_col=0)

    def split(self, data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        """Split a dataframe into reproducible train and test dataframes."""
        train, test = train_test_split(
            data,
            test_size=self._test_size,
            random_state=self._random_state,
        )
        return train.copy(), test.copy()
