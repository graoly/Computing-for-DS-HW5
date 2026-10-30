from diabetes_prediction.preprocessing.preprocessor import Preprocessor


class MissingRowsRemover(Preprocessor):

    def transform(self, df):
        return df.dropna(subset=self._columns)


class MeanImputer(Preprocessor):

    def __init__(self, columns):
        super().__init__(columns)
        self._means = None

    def fit(self, df):
        self._means = df[self._columns].mean()

    def transform(self, df):
        if self._means is None:
            raise Exception("MeanImputer must be fitted before calling transform.")
        return df.fillna(self._means)
