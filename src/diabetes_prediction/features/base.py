"""Abstract base class for feature transformers."""

from abc import ABC, abstractmethod

import pandas as pd


class FeatureTransformer(ABC):
    """Common fit/transform interface for feature transformations."""

    @abstractmethod
    def fit(self, data: pd.DataFrame) -> "FeatureTransformer":
        """Learn any values needed to apply this transformation."""

    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Return a transformed copy of the dataframe."""

    def fit_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Fit the transformation and apply it to the same dataframe."""
        return self.fit(data).transform(data)
