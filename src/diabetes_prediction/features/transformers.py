"""Categorical feature transformations inspired by the HW4 analysis."""

import pandas as pd

from .base import FeatureTransformer


class OneHotFeature(FeatureTransformer):
    """One-hot encode a column, preserving the training columns at prediction time."""

    def __init__(self, column: str) -> None:
        self._column = column
        self._categories: list[object] | None = None
        self._dummy_columns: list[str] | None = None

    def fit(self, data: pd.DataFrame) -> "OneHotFeature":
        self._require_column(data)
        self._categories = list(data[self._column].dropna().unique())
        categorical = pd.Categorical(data[self._column], categories=self._categories)
        self._dummy_columns = list(
            pd.get_dummies(categorical, prefix=self._column, dtype=int).columns
        )
        return self

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        self._require_column(data)
        if self._categories is None or self._dummy_columns is None:
            raise RuntimeError("OneHotFeature must be fitted before transform")
        result = data.drop(columns=[self._column]).copy()
        category = pd.Categorical(data[self._column], categories=self._categories)
        dummies = pd.get_dummies(category, prefix=self._column, dtype=int)
        dummies.columns = self._dummy_columns
        dummies.index = data.index
        return pd.concat([result, dummies], axis=1)

    def _require_column(self, data: pd.DataFrame) -> None:
        if self._column not in data.columns:
            raise ValueError(f"Required column {self._column!r} is missing")


class BinarizeFeature(FeatureTransformer):
    """Replace a column with 1 for a selected value and 0 for all others."""

    def __init__(self, column: str, positive_value: object) -> None:
        self._column = column
        self._positive_value = positive_value

    def fit(self, data: pd.DataFrame) -> "BinarizeFeature":
        if self._column not in data.columns:
            raise ValueError(f"Required column {self._column!r} is missing")
        return self

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        if self._column not in data.columns:
            raise ValueError(f"Required column {self._column!r} is missing")
        result = data.copy()
        result[self._column] = (result[self._column] == self._positive_value).astype(int)
        return result
