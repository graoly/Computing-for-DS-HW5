"""Class based components for diabetes mellitus data analysis."""

from .data import DiabetesDataLoader, DropMissingRows, MeanImputer
from .features import BinarizeFeature, FeatureTransformer, OneHotFeature
from .models import DiabetesClassifier

__all__ = [
    "DiabetesDataLoader",
    "DropMissingRows",
    "MeanImputer",
    "FeatureTransformer",
    "BinarizeFeature",
    "OneHotFeature",
    "DiabetesClassifier",
    "main",
]


def main() -> None:
    print("Hello from diabetes-prediction!")
