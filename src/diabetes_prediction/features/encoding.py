from diabetes_prediction.features.feature import Feature


class BinaryFeature(Feature):

    def __init__(self, column, positive_value):
        super().__init__(column)
        self._positive_value = positive_value

    def transform(self, df):
        transformed_df = df.copy()
        transformed_df[self._column] = (df[self._column] == self._positive_value).astype(int)
        return transformed_df


class OneHotEncodingFeature(Feature):

    def __init__(self, column):
        super().__init__(column)
        self._categories = None

    def fit(self, df):
        self._categories = sorted(df[self._column].dropna().unique())

    def transform(self, df):
        if self._categories is None:
            raise Exception("OneHotEncodingFeature must be fitted before calling transform.")
        transformed_df = self._create_dummy_columns(df)
        return transformed_df.drop(columns=[self._column])

    def _create_dummy_columns(self, df):
        transformed_df = df.copy()
        for category in self._categories:
            dummy_column = f"{self._column}_{category}"
            transformed_df[dummy_column] = (df[self._column] == category).astype(int)
        return transformed_df
