from abc import ABCMeta, abstractmethod


class Model(metaclass=ABCMeta):

    def __init__(self, feature_columns, target_column, hyperparameters=None):
        if hyperparameters is None:
            hyperparameters = {}
        self._feature_columns = feature_columns
        self._target_column = target_column
        self._hyperparameters = hyperparameters

    @abstractmethod
    def train(self, df):
        return NotImplementedError

    @abstractmethod
    def predict(self, df):
        return NotImplementedError
