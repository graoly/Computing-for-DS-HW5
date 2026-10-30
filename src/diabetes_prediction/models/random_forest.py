from sklearn.ensemble import RandomForestClassifier

from diabetes_prediction.models.model import Model


class RandomForestModel(Model):

    def __init__(self, feature_columns, target_column, hyperparameters=None):
        super().__init__(feature_columns, target_column, hyperparameters)
        self.model = RandomForestClassifier(**self._hyperparameters)

    def train(self, df):
        self.model.fit(self._get_features(df), df[self._target_column])

    def predict(self, df):
        return self.model.predict_proba(self._get_features(df))

    def _get_features(self, df):
        return df[self._feature_columns]
