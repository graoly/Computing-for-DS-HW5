from abc import ABCMeta, abstractmethod


class Feature(metaclass=ABCMeta):

    def __init__(self, column):
        self._column = column

    def fit(self, df):
        pass

    @abstractmethod
    def transform(self, df):
        return NotImplementedError
