"""Dataframe cleaning components for the diabetes dataset."""

from collections.abc import Sequence

import pandas as pd


class DropMissingRows:
    

    def __init__(self, columns: Sequence[str] = ("age", "gender", "ethnicity")) -> None:
        self._columns = tuple(columns)

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        missing = set(self._columns) - set(data.columns)
        if missing:
            raise ValueError(f"Required columns are missing: {sorted(missing)}")
        return data.dropna(subset=list(self._columns)).copy()


class MeanImputer:
    

    def __init__(self, columns: Sequence[str] = ("height", "weight")) -> None:
        self._columns = tuple(columns)
        self._means: pd.Series | None = None

    def fit(self, data: pd.DataFrame) -> "MeanImputer":
    
        missing = set(self._columns) - set(data.columns)
        if missing:
            raise ValueError(f"Required columns are missing: {sorted(missing)}")
        self._means = data.loc[:, list(self._columns)].mean()
        return self

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
      
        if self._means is None:
            raise RuntimeError("MeanImputer must be fitted before transform")
        missing = set(self._columns) - set(data.columns)
        if missing:
            raise ValueError(f"Required columns are missing: {sorted(missing)}")
        result = data.copy()
        result.loc[:, list(self._columns)] = result.loc[:, list(self._columns)].fillna(self._means)
        return result

    def fit_transform(self, data: pd.DataFrame) -> pd.DataFrame:
      
        return self.fit(data).transform(data)
