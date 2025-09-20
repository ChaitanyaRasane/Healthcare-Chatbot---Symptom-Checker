import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

class SymptomCheckerModel:
    def __init__(self):
        self.training_data = pd.read_csv('data/Training.csv')
        self.cols = self.training_data.columns[:-1]
        self.label_encoder = preprocessing.LabelEncoder()
        self.model = DecisionTreeClassifier()
        self.train_model()

    def train_model(self):
        x = self.training_data[self.cols]
        y = self.label_encoder.fit_transform(self.training_data['prognosis'])
        self.model.fit(x, y)

    def predict(self, symptoms):
        input_data = np.zeros(len(self.cols))
        for symptom in symptoms:
            if symptom in self.cols:
                input_data[self.cols.get_loc(symptom)] = 1
        pred_encoded = self.model.predict([input_data])[0]
        return self.label_encoder.inverse_transform([pred_encoded])[0]

