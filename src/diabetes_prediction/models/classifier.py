"""Sklearn model wrapper for diabetes mellitus classification."""

from collections.abc import Sequence
from typing import Any

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class DiabetesClassifier:
    """Fit a classifier on selected dataframe columns and predict probabilities."""

    def __init__(
        self,
        feature_columns: Sequence[str],
        target_column: str,
        model: Any | None = None,
        **model_parameters: Any,
    ) -> None:
        if not feature_columns:
            raise ValueError("At least one feature column is required")
        self._feature_columns = tuple(feature_columns)
        self._target_column = target_column
        self._model_parameters = dict(model_parameters)
        self.model = model if model is not None else RandomForestClassifier(
            random_state=42,
            **model_parameters,
        )

    def train(self, train_data: pd.DataFrame) -> None:
        """Fit the public sklearn model using configured feature and target columns."""
        required = set(self._feature_columns) | {self._target_column}
        missing = required - set(train_data.columns)
        if missing:
            raise ValueError(f"Required columns are missing: {sorted(missing)}")
        self.model.fit(train_data.loc[:, self._feature_columns], train_data[self._target_column])

    def predict(self, data: pd.DataFrame) -> pd.Series:
        """Return predicted probabilities for class 1, keeping the input index."""
        missing = set(self._feature_columns) - set(data.columns)
        if missing:
            raise ValueError(f"Required feature columns are missing: {sorted(missing)}")
        probabilities = self.model.predict_proba(data.loc[:, self._feature_columns])
        classes = list(self.model.classes_)
        positive_index = classes.index(1) if 1 in classes else len(classes) - 1
        return pd.Series(probabilities[:, positive_index], index=data.index, name="predictions")
