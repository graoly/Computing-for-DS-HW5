from abc import ABCMeta, abstractmethod


class DataReader(metaclass=ABCMeta):

    @abstractmethod
    def read(self):
        return NotImplementedError
