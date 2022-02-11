from sklearn.model_seletion import train_test_split


def preprocessing(data)
    X = data.drop(['Id', 'Species'], axis=1)
    y = data['Species']
    return train_test_split(X, y, test_size=0.4, random_state=5)

