from abc import ABCMeta, abstractmethod


class Preprocessor(metaclass=ABCMeta):

    def __init__(self, columns):
        self._columns = columns

    def fit(self, df):
        pass

    @abstractmethod
    def transform(self, df):
        return NotImplementedError
